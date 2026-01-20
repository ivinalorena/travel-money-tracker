import requests
import pandas as pd
from datetime import datetime

# URL Base da AwesomeAPI
BASE_URL = "https://economia.awesomeapi.com.br"

def pegar_cotacao_atual(moeda: str) -> dict | None:
    """
    Busca a cotação mais recente de uma moeda específica.
    
    Args:
        moeda (str): O par da moeda (ex: 'USD-BRL').
        
    Returns:
        dict: Dicionário com 'atual', 'var_pct', 'maxima'. Retorna None se falhar.
    """
    try:
        response = requests.get(f"{BASE_URL}/last/{moeda}")
        response.raise_for_status()
        data = response.json()
        
        # A chave do JSON vem como 'USDBRL' (sem traço), então removemos o traço
        chave_json = moeda.replace("-", "")
        item = data[chave_json]
        
        return {
            "atual": float(item["bid"]),
            "var_pct": item["pctChange"],
            "maxima": float(item["high"])
        }
    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
        return None

def pegar_historico(moeda: str, dias: int = 30) -> pd.DataFrame:
    """
    Busca o histórico de cotações dos últimos N dias.
    
    Args:
        moeda (str): O par da moeda (ex: 'USD-BRL').
        dias (int): Quantidade de dias para buscar (Padrão: 30).
        
    Returns:
        pd.DataFrame: DataFrame com colunas 'timestamp' e 'bid' (valor de compra).
    """
    try:
        response = requests.get(f"{BASE_URL}/json/daily/{moeda}/{dias}")
        response.raise_for_status()
        data_lista = response.json()
        
        # Processamento de dados (Data Cleaning)
        dados_processados = []
        for item in data_lista:
            dados_processados.append({
                "timestamp": datetime.fromtimestamp(int(item["timestamp"])),
                "bid": float(item["bid"])
            })
            
        return pd.DataFrame(dados_processados).sort_values(by="timestamp")
    except Exception as e:
        print(f"Erro ao buscar histórico: {e}")
        return pd.DataFrame() # Retorna DF vazio para não quebrar o gráfico