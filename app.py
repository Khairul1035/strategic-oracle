import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. Expert HCI Configuration
st.set_page_config(page_title="Strategic Oracle v3.0", layout="wide")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

# Sidebar: Expert Branding
st.sidebar.title("Strategic Analyst")
st.sidebar.info("Mohd Khairul Ridhuan bin Mohd Fadzil")
st.sidebar.markdown("""
**Domain Expertise:**
- 🌍 Geopolitics & Tactical Logic
- 📊 Accounting & Resource Management
- 💡 Theology & Institutional Ethics
- 🧠 Cognitive Neuroscience
- 💻 HCI Decision-Modeling
""")

st.title("🌍 THE STRATEGIC ORACLE v3.0: High-Level Predictive Engine")

# 2. Hard Data: Global Power Metrics
military_db = {
    "USA": {"Army": 95, "Jets": 100, "Missiles": 98, "Tech": 100, "Econ": 98},
    "UK": {"Army": 70, "Jets": 82, "Missiles": 85, "Tech": 92, "Econ": 85},
    "Germany": {"Army": 60, "Jets": 75, "Missiles": 70, "Tech": 95, "Econ": 95},
    "France": {"Army": 75, "Jets": 88, "Missiles": 88, "Tech": 90, "Econ": 88},
    "India": {"Army": 98, "Jets": 85, "Missiles": 95, "Tech": 82, "Econ": 90},
    "Israel": {"Army": 85, "Jets": 98, "Missiles": 98, "Tech": 100, "Econ": 82},
    "Iran": {"Army": 90, "Jets": 45, "Missiles": 98, "Tech": 70, "Econ": 55},
    "Russia": {"Army": 92, "Jets": 88, "Missiles": 100, "Tech": 85, "Econ": 65},
    "China Proxy": {"Army": 100, "Jets": 95, "Missiles": 96, "Tech": 98, "Econ": 100},
    "Syria": {"Army": 60, "Jets": 30, "Missiles": 75, "Tech": 40, "Econ": 30}
}

# 3. Interactive Strategic Map
st.markdown("### 🗺️ Tactical Alignment Configuration")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### 🔵 Western Coalition (US-UK Core)")
    west_allies = st.multiselect("Active Allies:", ["Germany", "France", "Israel", "India", "Australia", "Japan"], default=["Israel", "Germany"])
    active_west = ["USA", "UK"] + west_allies

with col_b:
    st.markdown("#### 🔴 Resistance Axis (Iran Core)")
    east_allies = st.multiselect("Active Allies:", ["Russia", "China Proxy", "Syria", "Iraq Militia", "North Korea"], default=["Russia", "Syria"])
    active_east = ["Iran"] + east_allies

# 4. Expert Algorithmic Calculation
def aggregate_power(country_list):
    stats = {"Army": 0, "Jets": 0, "Missiles": 0, "Tech": 0, "Econ": 0}
    for c in country_list:
        if c in military_db:
            for k in stats:
                # Primary countries contribute 100%, secondary allies contribute 75%
                weight = 1.0 if c in ["USA", "UK", "Iran"] else 0.75
                stats[k] += military_db[c][k] * weight
    return stats

west_stats = aggregate_power(active_west)
east_stats = aggregate_power(active_east)

# Win/Loss Prediction based on Air Superiority and Tech Edge
w_total = sum(west_stats.values())
e_total = sum(east_stats.values())
win_w = (w_total / (w_total + e_total)) * 100
win_e = 100 - win_w

# 5. Expert Dashboard Display
st.divider()
st.subheader("📊 Predictive Intelligence & System Dynamics")

m1, m2, m3 = st.columns(3)
m1.metric("Western Coalition Leverage", f"{win_w:.1f}%")
m2.metric("Resistance Axis Leverage", f"{win_e:.1f}%")
# Global Stress = Total Missile Tech + Tech Complexity
stress = (west_stats["Missiles"] + east_stats["Tech"]) / 15
m3.metric("Global Cognitive Stress Index", f"{stress:.1f} Hz", "High Escalation")

# HCI Innovation: Radar Chart for Multi-Dimensional Analysis
categories = ['Army', 'Jets', 'Missiles', 'Tech', 'Econ']
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[west_stats[k] for k in categories],
      theta=categories, fill='toself', name='Western Coalition'
))
fig.add_trace(go.Scatterpolar(
      r=[east_stats[k] for k in categories],
      theta=categories, fill='toself', name='Resistance Axis'
))

fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, max(w_total, e_total)/2.5])), 
                  showlegend=True, template="plotly_dark", title="Symmetric vs Asymmetric Power Profile")
st.plotly_chart(fig, use_container_width=True)

# 6. Professional Strategic Deep-Dive
st.markdown("### 🏛️ Strategic & Management Commentary")
st.write(f"""
**Coalition Analysis:** 
The Western Bloc currently integrates **{', '.join(active_west)}**. 
The Resistance Axis is reinforced by **{', '.join(active_east)}**.

**Expert Observation:**
1. **Asymmetric Risk:** While the West maintains **Air & Tech Superiority**, the Resistance Axis holds significant leverage through **Missile Saturation** and **Ground Army** density.
2. **Economic Integrity:** From an **Accounting & Sustainability** perspective, the high 'Econ' score of the West suggests a longer 'War Attrition' capability, but a massive hit to global supply chains is inevitable.
3. **Cognitive Neuroscience:** A Stress Index of **{stress:.1f} Hz** indicates that decision-makers are operating in 'Amygdala-High' mode, increasing the risk of miscalculation. 
4. **Theological Alignment:** True victory is not military; it is the **preservation of life**. We use these metrics to visualize the cost of failure, urging for **Ethical Strategic Governance**.
""")

st.info("Developed by Mohd Khairul Ridhuan | Bridging Management, Theology, and Technology.")
