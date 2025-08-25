import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime, timezone
import pytz

# Fuseau horaire France (CEST)
FRANCE_TZ = pytz.timezone("Europe/Paris")

# Clés API via variables d'environnement
MORALIS_API_KEY = os.getenv("MORALIS_API_KEY", "ta_clé_moralis")
BITQUERY_TOKEN = os.getenv("BITQUERY_TOKEN", "ta_clé_bitquery")
COINGECKO_API = "https://api.coingecko.com/api/v3"
N8N_WEBHOOK = os.getenv("N8N_WEBHOOK", "https://ton-n8n.onrender.com/webhook")
SERVER_JS_API = os.getenv("SERVER_JS_API", "https://crypto-server-js.vercel.app/api")

# Fonction pour tracker grandes transactions (simplifiée)
def track_large_tx(chain):
    try:
        # Exemple requête CoinGecko pour prix en EUR
        url = f"{COINGECKO_API}/simple/price?ids={chain}&vs_currencies=eur"
        response = requests.get(url)
        response.raise_for_status()
        price_data = response.json()
        # Placeholder pour Moralis/Bitquery (à compléter avec tes clés)
        return pd.DataFrame({
            "tx_hash": ["0x123"],
            "amount_eur": [price_data.get(chain, {}).get("eur", 0) * 1000],
            "chain": [chain],
            "timestamp": [datetime.now(FRANCE_TZ).strftime("%Y-%m-%d %H:%M:%S %Z")]
        })
    except Exception as e:
        st.error(f"Erreur tracking {chain}: {str(e)}")
        return pd.DataFrame()

# Fonction pour appeler n8n webhook
def trigger_n8n_workflow(workflow_id, data=None):
    try:
        response = requests.post(f"{N8N_WEBHOOK}/{workflow_id}", json=data or {})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Erreur n8n {workflow_id}: {str(e)}")
        return {}

# Interface Streamlit
st.title("Outil Crypto Sophistiqué")
st.sidebar.header("Fonctionnalités")

# Section Tracker Transactions
if st.sidebar.button("Tracker Grandes Tx"):
    chain = st.selectbox("Chaîne", ["ethereum", "solana", "bitcoin", "bnb"])
    df = track_large_tx(chain)
    if not df.empty:
        st.dataframe(df)
        # Appel n8n pour scraping (ex. explorer blockchain)
        scraped = trigger_n8n_workflow("scrape_http", {"url": f"https://explorer.example.com/{chain}"})
        st.write("Données Scrapées (n8n):", scraped)
    else:
        st.warning("Aucune donnée pour cette chaîne.")

# Section Workflows n8n
st.sidebar.subheader("Workflows n8n")
try:
    workflows = requests.get(f"{SERVER_JS_API}/workflows").json().get("workflows", [])
    for wf in workflows[:5]:
        st.sidebar.write(f"{wf['name']} - {wf['description']}")
except:
    st.sidebar.error("Erreur fetch workflows")

# Info
st.info(f"Connecté à n8n ({N8N_WEBHOOK}) et server.js ({SERVER_JS_API}). Heure: {datetime.now(FRANCE_TZ).strftime('%Y-%m-%d %H:%M:%S %Z')}")
