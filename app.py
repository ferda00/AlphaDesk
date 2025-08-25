import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime, timezone
import pytz
from moralis import evm_api, solana_api

# Fuseau horaire France (CEST)
FRANCE_TZ = pytz.timezone("Europe/Paris")

# Clés API
MORALIS_API_KEY = os.getenv("MORALIS_API_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6ImEzYjA5YzIzLTBmNGMtNDFmNy05OTIzLTRlN2QzNWM5ZDg4ZSIsIm9yZ0lkIjoiNDY3MTAyIiwidXNlcklkIjoiNDgwNTM5IiwidHlwZUlkIjoiMTJiMGM2OTMtZDk4MS00MGVhLWI1NmItZjI3MDg0M2VjMTk1IiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3NTYwOTMxMTYsImV4cCI6NDkxMTg1MzExNn0.TtwuV8TIzKZMDQzc5KEMX5O_xzbCutAAribtowzQ9sc")
BITQUERY_TOKEN = os.getenv("BITQUERY_TOKEN", "ta_clé_bitquery")  # Remplace par ta clé Bitquery
COINGECKO_API = "https://api.coingecko.com/api/v3"
N8N_WEBHOOK = os.getenv("N8N_WEBHOOK", "https://ton-n8n.onrender.com/webhook")
SERVER_JS_API = os.getenv("SERVER_JS_API", "https://crypto-server-js.vercel.app/api")

# Headers pour Bitquery
BITQUERY_HEADERS = {"X-API-KEY": BITQUERY_TOKEN}

# Fonction pour prix Bitcoin via Bitquery
def get_bitcoin_price():
    query = """
    query MyQuery {
      bitcoin {
        outputs(date: {is: "%s"}) {
          value
          usd: value(in: USD)
          expression(get: "usd/value")
        }
      }
    }
    """ % datetime.now(FRANCE_TZ).strftime("%Y-%m-%d")
    try:
        response = requests.post("https://graphql.bitquery.io", json={"query": query}, headers=BITQUERY_HEADERS)
        response.raise_for_status()
        data = response.json()["data"]["bitcoin"]["outputs"]
        return pd.DataFrame([{
            "price_usd": d["usd"],
            "price_per_btc": d["expression"],
            "timestamp": datetime.now(FRANCE_TZ).strftime("%Y-%m-%d %H:%M:%S %Z")
        } for d in data])
    except Exception as e:
        st.error(f"Erreur Bitquery Bitcoin: {str(e)}")
        return pd.DataFrame()

# Fonction pour tracker grandes transactions (Morale + CoinGecko)
def track_large_tx(chain):
    try:
        # Prix via CoinGecko en USD
        url = f"{COINGECKO_API}/simple/price?ids={chain}&vs_currencies=usd"
        price_response = requests.get(url)
        price_response.raise_for_status()
        price_data = price_response.json()
        
        if chain == "solana":
            params = {"network": "mainnet", "limit": 10, "from_date": datetime.now(FRANCE_TZ).isoformat()}
            result = solana_api.account.get_spl_transfers(api_key=MORALIS_API_KEY, params=params)
            return pd.DataFrame([{
                "tx_hash": t["transaction_hash"],
                "amount_usd": float(t["amount"]) * price_data.get(chain, {}).get("usd", 0),
                "chain": chain,
                "timestamp": datetime.fromisoformat(t["block_timestamp"]).astimezone(FRANCE_TZ).strftime("%Y-%m-%d %H:%M:%S %Z")
            } for t in result["result"]])
        else:
            # Placeholder pour Ethereum/Bitcoin (nécessite Bitquery)
            return pd.DataFrame({
                "tx_hash": ["0x123"],
                "amount_usd": [1000 * price_data.get(chain, {}).get("usd", 0)],
                "chain": [chain],
                "timestamp": [datetime.now(FRANCE_TZ).strftime("%Y-%m-%d %H:%M:%S %Z")]
            })
    except Exception as e:
        st.error(f"Erreur tracking {chain}: {str(e)}")
        return pd.DataFrame()

# Fonction pour NFTs via Morale
def get_nfts():
    try:
        params = {"chain": "eth", "format": "decimal", "limit": 10}
        result = evm_api.nft.get_nfts(api_key=MORALIS_API_KEY, params=params)
        return pd.DataFrame([{
            "token_id": nft["token_id"],
            "contract": nft["token_address"],
            "name": nft.get("name", "N/A"),
            "timestamp": datetime.now(FRANCE_TZ).strftime("%Y-%m-%d %H:%M:%S %Z")
        } for nft in result["result"]])
    except Exception as e:
        st.error(f"Erreur NFTs: {str(e)}")
        return pd.DataFrame()

# Fonction n8n webhook
def trigger_n8n_workflow(workflow_id, data=None):
    try:
        response = requests.post(f"{N8N_WEBHOOK}/{workflow_id}", json=data or {})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Erreur n8n {workflow_id}: {str(e)}")
        return {}

# Interface Streamlit
st.title("Outil Crypto Sophistiqué (USD)")
st.sidebar.header("Fonctionnalités")

# Tracker Transactions
if st.sidebar.button("Tracker Grandes Tx"):
    chain = st.selectbox("Chaîne", ["bitcoin", "ethereum", "solana", "bnb"])
    df = track_large_tx(chain)
    if not df.empty:
        st.dataframe(df)
        scraped = trigger_n8n_workflow("scrape_http", {"url": f"https://explorer.example.com/{chain}"})
        st.write("Données Scrapées (n8n):", scraped)
    else:
        st.warning("Aucune donnée pour cette chaîne.")

# Prix Bitcoin
if st.sidebar.button("Prix Bitcoin"):
    df = get_bitcoin_price()
    if not df.empty:
        st.dataframe(df)
    else:
        st.warning("Aucun prix Bitcoin récupéré.")

# NFTs
if st.sidebar.button("Top NFTs"):
    df = get_nfts()
    if not df.empty:
        st.dataframe(df)
    else:
        st.warning("Aucun NFT récupéré.")

# Workflows n8n
st.sidebar.subheader("Workflows n8n")
try:
    workflows = requests.get(f"{SERVER_JS_API}/workflows").json().get("workflows", [])
    for wf in workflows[:5]:
        st.sidebar.write(f"{wf['name']} - {wf['description']}")
except:
    st.sidebar.error("Erreur fetch workflows")

# Info
st.info(f"Connecté à n8n ({N8N_WEBHOOK}) et server.js ({SERVER_JS_API}). Heure: {datetime.now(FRANCE_TZ).strftime('%Y-%m-%d %H:%M:%S %Z')}")
