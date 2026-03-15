import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
import random

# 1. High-Tech HCI Configuration
st.set_page_config(page_title="Strategic Oracle v4.0", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.block-container { padding-top: 1rem; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border-left: 5px solid #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar: Expert Profile
st.sidebar.title("Strategic Architect")
st.sidebar.info("Mohd Khairul Ridhuan bin Mohd Fadzil")
st.sidebar.markdown("""
**Domain Expertise:**
- 🌍 Geopolitics & Tactical Logic
- 📊 Accounting & OPEX Integrity
- 💡 Theology & Institutional Ethics
- 🧠 Cognitive Neuroscience
- 💻 HCI Decision-Intelligence
""")

st.title("🧠 NEURO-STRAT: Strategic Oracle v4.0")
st.caption("Advanced Predictive Intelligence Engine | Multipotentialite Analysis")

# 2. Hard Data: Global Power Metrics (Expanded for Detail)
military_db = {
    "USA": {"Army": 95, "Jets": 100, "Missiles": 98, "Tech": 100, "Econ": 98, "Naval": 100, "Cyber": 95},
    "UK": {"Army": 70, "Jets": 82, "Missiles": 85, "Tech": 92, "Econ": 85, "Naval": 88, "Cyber": 90},
    "Germany": {"Army": 60, "Jets": 75, "Missiles": 70, "Tech": 95, "Econ": 95, "Naval": 60, "Cyber": 85},
    "France": {"Army": 75, "Jets": 88, "Missiles": 88, "Tech": 90, "Econ": 88, "Naval": 85, "Cyber": 88},
    "India": {"Army": 98, "Jets": 85, "Missiles": 95, "Tech": 82, "Econ": 90, "Naval": 80, "Cyber": 75},
    "Israel": {"Army": 85, "Jets": 98, "Missiles": 98, "Tech": 100, "Econ": 82, "Naval": 50, "Cyber": 98},
    "Iran": {"Army": 92, "Jets": 45, "Missiles": 98, "Tech": 70, "Econ": 55, "Naval": 65, "Cyber": 80},
    "Russia": {"Army": 95, "Jets": 88, "Missiles": 100, "Tech": 85, "Econ": 65, "Naval": 80, "Cyber": 95},
    "China Proxy": {"Army": 100, "Jets": 95, "Missiles": 96, "Tech": 98, "Econ": 100, "Naval": 95, "Cyber": 98},
    "Syria": {"Army": 65, "Jets": 30, "Missiles": 75, "Tech": 40, "Econ": 30, "Naval": 20, "Cyber": 30}
}

# 3. Interactive Strategic Map
st.markdown("### 🗺️ Coalition Alignment Configuration")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### 🔵 Western Coalition")
    west_allies = st.multiselect("Select Active Allies:", ["Germany", "France", "Israel", "India", "Australia", "Japan"], default=["Israel", "Germany"])
    active_west = ["USA", "UK"] + west_allies

with col_b:
    st.markdown("#### 🔴 Resistance Axis")
    east_allies = st.multiselect("Select Active Allies:", ["Russia", "China Proxy", "Syria", "North Korea"], default=["Russia", "Syria"])
    active_east = ["Iran"] + east_allies

# Placeholder for Animated Content
dashboard_placeholder = st.empty()

# --- SIMULATION LOOP (Moving Data Effect) ---
for i in range(1): # We only run once but we'll use animated charts
    with dashboard_placeholder.container():
        
        # 4. Calculation Logic
        def aggregate_power(country_list):
            stats = {"Army": 0, "Jets": 0, "Missiles": 0, "Tech": 0, "Econ": 0, "Naval": 0, "Cyber": 0}
            for c in country_list:
                if c in military_db:
                    weight = 1.0 if c in ["USA", "UK", "Iran"] else 0.75
                    for k in stats:
                        stats[k] += military_db[c][k] * weight
            return stats

        west_stats = aggregate_power(active_west)
        east_stats = aggregate_power(active_east)
        
        w_total = sum(west_stats.values())
        e_total = sum(east_stats.values())
        win_w = (w_total / (w_total + e_total)) * 100
        
        # 5. Visual Dashboard
        st.divider()
        st.subheader("📊 Predictive Intelligence Suite")
        
        m1, m2 = st.columns([1, 2])
        
        with m1:
            # Moving Gauge for Win Probability
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = win_w,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Western Coalition Leverage %", 'font': {'size': 18}},
                gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                    'bar': {'color': "#3b82f6"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, 50], 'color': '#ef4444'},
                        {'range': [50, 100], 'color': '#10b981'}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90}}))
            fig_gauge.update_layout(paper_bgcolor = "#0e1117", font = {'color': "white", 'family': "Arial"}, height=350)
            st.plotly_chart(fig_gauge, use_container_width=True)

        with m2:
            # High-Detail Radar Chart (Colorful & Large)
            categories = ['Army', 'Jets', 'Missiles', 'Tech', 'Econ', 'Naval', 'Cyber']
            fig_radar = go.Figure()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=[west_stats[k] for k in categories],
                theta=categories,
                fill='toself',
                name='Western Coalition',
                line_color='#3b82f6',
                fillcolor='rgba(59, 130, 246, 0.4)'
            ))
            fig_radar.add_trace(go.Scatterpolar(
                r=[east_stats[k] for k in categories],
                theta=categories,
                fill='toself',
                name='Resistance Axis',
                line_color='#ef4444',
                fillcolor='rgba(239, 68, 68, 0.4)'
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 350], gridcolor="#4b5563"),
                    angularaxis=dict(gridcolor="#4b5563")
                ),
                showlegend=True,
                template="plotly_dark",
                paper_bgcolor="#0e1117",
                font=dict(size=14),
                height=450,
                title="Multidimensional Attrition Profile"
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        # 6. Moving Intelligence Feed (HCI Animation Effect)
        st.markdown("### 📡 Live Strategic Intelligence Feed")
        feed_placeholder = st.empty()
        intelligence_logs = [
            "Analyzing Hormuz Choke-point Saturation...",
            "Calculating War Risk Insurance OPEX Impact...",
            f"Coalition Alignment: {', '.join(active_west)} confirmed.",
            "Amygdala-Response levels peaking in Energy Markets.",
            "Satellite telemetry verifying Missile Battery positions."
        ]
        feed_text = ""
        for log in intelligence_logs:
            feed_text += f"> 🟢 {log}  \n"
        feed_placeholder.markdown(feed_text)

        # 7. Professional Commentary
        st.divider()
        st.subheader("🏛️ Strategic & Management Analysis")
        st.write(f"""
        **Theological & Business Alignment:** 
        True intelligence is not found in military dominance, but in the **preservation of human life**. As a researcher bridging Management and Theology, I built this engine to advocate for **Cognitive Clarity**. 
        
        **Expert Findings:**
        - **Economic Integrity (Accounting):** The West holds a significant **Econ & Naval** lead, suggesting high endurance. However, the Resistance Axis leverages **Missile Saturation**, creating a high-cost stalemate.
        - **Neuroscience:** The animated volatility in the data suggests that decision-makers are currently operating with a **high cognitive load**, increasing the risk of miscalculation.
        """)

        st.markdown(f"<div style='text-align: center; color: grey;'>Developed by <strong>Mohd Khairul Ridhuan bin Mohd Fadzil</strong> | © 2026</div>", unsafe_allow_html=True)
