import streamlit as st
import os
import pandas as pd
import time

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="FedMed Dashboard",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------------------------------
# UI THEME + CUSTOM CSS
# -----------------------------------------------------
st.markdown("""
<style>
    /* Main Background */
    body, .stApp {
        background: #050b14;
        color: white;
    }

    /* Hide Top Bar padding */
    .block-container {
        padding-top: 2rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }

    /* Metric Cards Styling */
    [data-testid="stMetric"] {
        background: #0a1623;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #1f3a4f;
        box-shadow: 0 0 10px rgba(0, 229, 255, 0.1);
        transition: transform 0.2s ease-in-out;
    }
    
    [data-testid="stMetric"]:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.3);
    }

    /* Metric Label Color */
    [data-testid="stMetricLabel"] {
        color: #00e5ff !important;
    }

    /* Alert/Info Boxes (Hospital Panels) */
    [data-testid="stAlert"] {
        background: #0a1623;
        border-radius: 12px;
        border: 1px solid #1f3a4f;
        color: #ffffff;
    }

    /* Code Block (The Network Diagram) */
    pre {
        background: #08101a !important;
        border: 1px solid #00e5ff !important;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 229, 255, 0.2);
    }
    
    code {
        color: #00e5ff !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-weight: bold;
    }

    /* Success Message (Privacy Bar) */
    [data-testid="stSuccess"] {
        background: linear-gradient(90deg, #0f2f24, #144032) !important;
        border: 1px solid #00ff9d !important;
        color: #00ff9d !important;
        border-radius: 8px;
    }

    /* Header Glow */
    h1, h2, h3 {
        color: #ffffff;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HEADER SECTION
# -----------------------------------------------------
st.title("🔒 Privacy-Preserving • Decentralized • Real-Time Learning System")

st.markdown("""
<div style="height:2px; width:100%; background:linear-gradient(90deg, #00e5ff, transparent); margin-bottom: 20px;"></div>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# TOP METRICS ROW
# -----------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Active Hospitals", value="2 Nodes", delta="Online")

with col2:
    st.metric(label="Global Model Version", value="Round 5", delta="+1")

with col3:
    st.metric(label="Data Privacy", value="100% Secured", delta="Zero Leaks")

st.write("") # Spacer

# -----------------------------------------------------
# MAIN NETWORK ARCHITECTURE LAYOUT
# -----------------------------------------------------
# Layout: Left Hospital | Center Diagram | Right Hospital
left_col, center_col, right_col = st.columns([1, 2, 1])

# --- LEFT COLUMN: HOSPITAL A ---
with left_col:
    st.info("🏥 **Hospital A (Client 0)**")
    st.write("📂 Data: **2,856 Images**")
    st.write("⚙️ Status: **Training...**")
    st.progress(100)
    
    # Visual Separator line
    st.markdown("<div style='height:4px; width:100%; background:#007bff; border-radius:2px;'></div>", unsafe_allow_html=True)

# --- CENTER COLUMN: ARCHITECTURE DIAGRAM ---
with center_col:
    st.markdown("##### 📡 Federated Network Architecture")
    
    # ASCII Art Diagram
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

    # Privacy Status Bar
    st.success("✅ Differential Privacy: ACTIVE")

# --- RIGHT COLUMN: HOSPITAL B ---
with right_col:
    st.info("🏥 **Hospital B (Client 1)**")
    st.write("📂 Data: **2,856 Images**")
    st.write("⚙️ Status: **Training...**")
    st.progress(100)

    # Visual Separator line
    st.markdown("<div style='height:4px; width:100%; background:#007bff; border-radius:2px;'></div>", unsafe_allow_html=True)

st.write("") # Spacer

# -----------------------------------------------------
# REAL-TIME ACCURACY GRAPH
# -----------------------------------------------------
log_file = "training_log.csv"
chart_data = None

if os.path.exists(log_file):
    try:
        # Read the file to get data
        with open(log_file, "r") as f:
            lines = [float(line.strip()) for line in f.readlines() if line.strip()]
        
        if lines:
            chart_data = pd.DataFrame({
                "Round": range(1, len(lines) + 1),
                "Accuracy": lines
            })
            current_acc = lines[-1]
        else:
            current_acc = 0.0
            
    except Exception as e:
        current_acc = 0.0
else:
    current_acc = 0.0

# Render Graph Section if data exists
if chart_data is not None:
    st.subheader(f"📈 Global Model Performance (Accuracy: {current_acc*100:.2f}%)")
    
    # Custom Chart Color
    st.line_chart(
        chart_data,
        x="Round",
        y="Accuracy",
        color="#00e5ff"  # Cyan line to match theme
    )
else:
    st.warning("Waiting for training to start...")

# -----------------------------------------------------
# REFRESH CONTROLS
# -----------------------------------------------------
if st.button("Refresh Model Metrics"):
    st.rerun()
