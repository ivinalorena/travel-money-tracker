import streamlit as st
import plotly.express as px
import api_economia

# --- FUNÇÕES AUXILIARES (Lógica separada da Tela) ---
def calcular_custo_efetivo(valor_estrangeiro: float, cotacao: float, spread: float, iof: float) -> tuple:
    """Calcula o custo total em reais e detalha as taxas."""
    cotacao_com_spread = cotacao * (1 + (spread / 100))
    custo_total_unitario = cotacao_com_spread * (1 + iof)
    total_reais = valor_estrangeiro * custo_total_unitario
    
    val_spread = cotacao * (spread / 100)
    val_iof = cotacao_com_spread * iof
    
    return total_reais, custo_total_unitario, val_spread, val_iof

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Travel Money Tracker", 
    page_icon="💸", 
    layout="centered"
)

# --- CABEÇALHO ---
st.title("💸 Travel Money Tracker")
st.markdown("""
    **Monitor de Câmbio Inteligente.** Acompanhe a cotação em tempo real e simule o **Custo Efetivo Total (CET)** da sua compra, incluindo taxas ocultas de banco e governo.
""")
st.divider()

# --- SIDEBAR (CONTROLES) ---
with st.sidebar:
    st.header("✈️ Configuração da Viagem")
    
    # Dicionário de Moedas (Fácil de expandir)
    MOEDAS = {
        "Dólar Americano (USD)": "USD-BRL",
        "Euro (EUR)": "EUR-BRL",
        "Libra Esterlina (GBP)": "GBP-BRL",
        "Bitcoin (BTC)": "BTC-BRL"
    }
    
    moeda_label = st.selectbox("Selecione a Moeda:", list(MOEDAS.keys()))
    par_moeda = MOEDAS[moeda_label]
    simbolo = par_moeda.split("-")[0]
    
    st.markdown("---")
    st.caption("Dados via AwesomeAPI • Desenvolvido por Icaro Souza")

# --- LÓGICA PRINCIPAL ---
dados = api_economia.pegar_cotacao_atual(par_moeda)

if dados:
    # --- BLOCO 1: KPI GERAL ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Cotação Comercial", f"R$ {dados['atual']:.2f}")
    
    var_cor = "normal"
    if float(dados['var_pct']) > 0: var_cor = "off" # Vermelho se subiu 
    else: var_cor = "inverse" # Verde se caiu 
    
    col2.metric("Variação (24h)", f"{dados['var_pct']}%", delta_color=var_cor)
    col3.metric("Máxima do Dia", f"R$ {dados['maxima']:.2f}")

    # --- BLOCO 2: CALCULADORA ---
    st.write("---")
    st.subheader("🧮 Calculadora de Custo Real")
    
    with st.container(border=True):
        c1, c2 = st.columns(2)
        
        valor_viagem = c1.number_input(
            f"Valor para levar ({simbolo}):", 
            min_value=1.0, 
            value=1000.0, 
            step=50.0
        )
        
        metodo = c2.radio(
            "Método de Pagamento:", 
            ["Dinheiro (Espécie)", "Cartão (Crédito/Pré-pago)"]
        )

        # Configuração de Taxas
        st.markdown("#### ⚙️ Taxas Bancárias")
        spread = st.slider(
            "Spread do Banco/Casa de Câmbio (%):", 
            min_value=0.0, 
            max_value=10.0, 
            value=4.0,
            help="Lucro que o banco cobra acima da cotação comercial."
        )

        # Definição do IOF
        if "Dinheiro" in metodo:
            iof_taxa = 0.011
            iof_texto = "1.1% (Espécie)"
        else:
            iof_taxa = 0.0438
            iof_texto = "4.38% (Cartão)"

        # Chamada da Função de Cálculo
        total_reais, custo_unitario, val_spread, val_iof = calcular_custo_efetivo(
            valor_viagem, dados['atual'], spread, iof_taxa
        )

        st.divider()
        
        # --- RESULTADO FINAL (Estilo Recibo) ---
        st.markdown(f"""
        ### 💰 Você pagará: :green[R$ {total_reais:.2f}]
        Efetivamente, cada **1 {simbolo}** vai custar **R$ {custo_unitario:.2f}**.
        """)
        
        with st.expander("🔎 Ver Detalhamento dos Custos"):
            st.markdown(f"""
            | Item | Valor Aproximado |
            | :--- | :--- |
            | **Cotação Base** | R$ {dados['atual']:.2f} |
            | **+ Spread ({spread}%)** | R$ {val_spread:.2f} |
            | **+ IOF ({iof_texto})** | R$ {val_iof:.2f} |
            | **= Custo Final** | **R$ {custo_unitario:.2f}** |
            """)
            st.caption("*Valores estimados. Podem haver variações de arredondamento.*")

    # --- BLOCO 3: GRÁFICO HISTÓRICO ---
    st.write("---")
    st.subheader(f"📈 Evolução do {simbolo} (30 Dias)")
    
    with st.spinner("Carregando histórico..."):
        df = api_economia.pegar_historico(par_moeda)
        
    if not df.empty:
        fig = px.line(
            df, 
            x='timestamp', 
            y='bid', 
            template="plotly_white"
        )
        fig.update_layout(xaxis_title=None, yaxis_title="Reais (R$)")
        st.plotly_chart(fig, width="stretch")

else:
    st.error("⚠️ Erro de conexão com a API. Verifique sua internet.")