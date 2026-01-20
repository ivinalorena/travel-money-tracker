# 💸 Travel Money Tracker

> A smart currency monitor and real-time cost calculator for international travelers.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## 📌 About the Project

**Travel Money Tracker** is a data-driven dashboard designed to help travelers plan their currency exchange. Unlike simple converters, this tool calculates the **Effective Total Cost (CET)**, considering hidden fees like Bank Spread and IOF (Brazilian Financial Operations Tax).

It consumes real-time data from the **AwesomeAPI** to provide accurate quotations for USD, EUR, GBP, and BTC.

### ✨ Key Features

- **Real-Time Quotation:** Fetches live commercial exchange rates.
- **"Real Cost" Calculator:** Simulates the final price in BRL (Reais) adding:
  - **Spread:** Customizable bank fee slider (0% to 10%).
  - **IOF:** Automatically switches between Cash (1.1%) and Card (4.38%).
- **Interactive Charts:** Visualizes the currency trend over the last 30 days using Plotly.
- **Daily KPIs:** Tracks daily variation, maximum, and minimum values.

---

## 📸 Screenshots

*(Add a screenshot of your dashboard here to show how it looks)*
---

## 🚀 How to Run Locally

Follow these steps to run the application on your machine.

### Prerequisites
- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository**

   git clone [https://github.com/icarodev10/travel-money-tracker.git](https://github.com/icarodev10/travel-money-tracker.git)
   cd travel-money-tracker

Create a Virtual Environment (Optional but Recommended)

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install Dependencies

pip install -r requirements.txt

Run the App
streamlit run app.py

The application will open automatically in your browser at http://localhost:8501.

🛠️ Tech Stack
Frontend: Streamlit (Python-based UI framework)

Data Processing: Pandas

Visualization: Plotly Express

API: AwesomeAPI (Free Open Source Finance API)

📂 Project Structure
travel-money-tracker/
├── app.py              # Main dashboard application (Frontend)
├── api_economia.py     # API connection and Data Cleaning logic (Backend)
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
🤝 Contributing
Feel free to fork this project and submit Pull Requests. Any improvement is welcome!

📞 Contact
Icaro de Souza de Lima

<div align="left">
  <a href="https://github.com/icarodev10" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank" />
  </a>
  <a href="https://www.linkedin.com/in/icaro-souza-ti/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank" />
  </a>
</div>

