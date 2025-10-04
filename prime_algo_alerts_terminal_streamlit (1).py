# PrimeAlgo 15x15 Static Alerts Web App for Cloud Deployment
# This version uses Streamlit and connects to your 15x15 Quant Model
# Removed 'colorama' dependency for Streamlit Cloud compatibility

import streamlit as st
from datetime import datetime
import pandas as pd
import time

# ---------- Your 15x15 Quant Model ----------
# Replace this section with your actual 15x15 model function
# The function should return a list of signals as strings

def get_quant_signals():
    # Example: Replace with your real 15x15 strategy signals
    signals = [
        "Strategy 1: BUY XYZ",
        "Strategy 2: SELL ABC",
        "Strategy 3: HOLD LMN"
    ]
    return signals

# ---------- Configuration ----------
SENDER_NAME = "PrimeAlgo Quant"
messages_store = []
FETCH_INTERVAL = 10  # seconds between automatic fetches
MAX_CYCLES = 5       # total number of fetch cycles to avoid infinite loops in cloud

st.set_page_config(page_title="PrimeAlgo Quant Alerts", layout="wide")
st.title("PrimeAlgo 15x15 Quant Alerts")
st.subheader(f"Sender: {SENDER_NAME}")

# Fetch signals function
def fetch_signals():
    signals = get_quant_signals() or ["No new signals from quant model."]
    return signals

# Auto-fetch signals in cloud
for cycle in range(MAX_CYCLES):
    st.write(f"--- Fetch Cycle {cycle+1} ---")
    signals = fetch_signals()
    for message_text in signals:
        msg = {
            'id': str(datetime.now().timestamp()),
            'timestamp': datetime.now().isoformat(),
            'sender': SENDER_NAME,
            'text': message_text
        }
        messages_store.append(msg)
        st.success(f"[{msg['timestamp']}] {msg['sender']}: {msg['text']}")
        time.sleep(0.3)

    # Display last 20 alerts
    st.subheader("Last 20 Alerts")
    for msg in messages_store[-20:]:
        st.write(f"[{msg['timestamp']}] {msg['sender']}: {msg['text']}")

    # Save messages to CSV
    if messages_store:
        df = pd.DataFrame(messages_store)
        df.to_csv("primealgo_quant_alerts_log_cloud.csv", index=False)
        st.info("All alerts saved to primealgo_quant_alerts_log_cloud.csv")

    time.sleep(FETCH_INTERVAL)

st.info("Auto-fetch finished. Deploy this app on Streamlit Cloud: https://share.streamlit.io")
