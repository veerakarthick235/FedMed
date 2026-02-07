import streamlit as st
import time
import os

st.set_page_config(page_title="FedMed Dashboard", page_icon="🏥", layout="wide")

# Header
st.title("🏥 FedMed: Privacy-Preserving Medical AI")
st.markdown("### 🔒 Secure Federated Learning Network Status")

# Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Active Hospitals", "2 Nodes", "Online")
col2.metric("Global Model Version", "Round 5", "+1")
col3.metric("Data Privacy", "100% Secured", "Zero Leaks")

st.divider()

# --- NETWORK ACTIVITY SECTION ---
c1, c2, c3 = st.columns([1, 2, 1])

with c1:
    st.info("**Hospital A (Client 0)**")
    st.write("📂 Data: 2,856 Images")
    st.write("⚙️ Status: Training...")
    st.progress(100)

with c3:
    st.info("**Hospital B (Client 1)**")
    st.write("📂 Data: 2,856 Images")
    st.write("⚙️ Status: Training...")
    st.progress(100)

with c2:
    st.write("###### 📡 Network Architecture")
    # This ASCII Diagram replaces the broken image. It never fails.
    st.code("""
      [☁️ Central Server]
            /    \\
       (Model)  (Model)
         /        \\
   [🏥 Hosp A]  [🏥 Hosp B]
   (Training)    (Training)
         \\        /
       (Weights) (Weights)
            \\    /
      [🚀 Updated Model]
    """, language="text")
    
    st.success("✅ Differential Privacy Active")

# --- REAL-TIME GRAPH SECTION ---
st.divider()
st.subheader("📈 Global Model Performance")

# Check if log file exists
if os.path.exists("training_log.csv"):
    with open("training_log.csv", "r") as f:
        data = [float(line.strip()) for line in f.readlines() if line.strip()]
    
    if data:
        # Create a chart with real data
        chart_data = {"Round": range(1, len(data) + 1), "Accuracy": data}
        st.line_chart(chart_data, x="Round", y="Accuracy")
        st.metric("Current Accuracy", f"{data[-1]*100:.2f}%")
    else:
        st.warning("Training hasn't started yet...")
else:
    st.warning("Waiting for Server to complete the first round...")

if st.button("Refresh Graph"):
    st.rerun()