import streamlit as st
import pandas as pd
import plotly.express as px

# 1. HCI & UX Configuration
st.set_page_config(page_title="Strategic Oracle v2.0", layout="wide")
st.markdown("<style>div.block-container{padding-top:1.5rem;}</style>", unsafe_allow_html=True)

# Sidebar: Branding & Profile
st.sidebar.title("Strategic Analyst")
st.sidebar.info("Mohd Khairul Ridhuan bin Mohd Fadzil")
st.sidebar.markdown("""
**Expertise Layers:**
- 🌍 Geopolitics (Quantitative)
- 📊 Accounting & Management
- 💡 Business & Theology
- 🧠 Cognitive Neuroscience
- 💻 HCI Modeling
""")

st.title("🌍 THE STRATEGIC ORACLE v2.0")
st.subheader("Predictive Win/Loss Simulation: Iran-West Escalation")

# 2. Hard Data: Military Ratios (Approximated Global Power Index)
# Values represent Power Units (Personnel, Jets, Missile Tech, EW/AI)
military_data = {
    "USA": {"Army": 95, "Jets": 100, "Missiles": 95, "Tech": 100, "Econ": 95},
    "UK": {"Army": 60, "Jets": 75, "Missiles": 80, "Tech": 85, "Econ": 80},
    "Germany": {"Army": 55, "Jets": 70, "Missiles": 65, "Tech": 90, "Econ": 90},
    "France": {"Army": 70, "Jets": 85, "Missiles": 85, "Tech": 88, "Econ": 85},
    "India": {"Army": 90, "Jets": 80, "Missiles": 90, "Tech": 75, "Econ": 85},
    "Iran": {"Army": 85, "Jets": 40, "Missiles": 95, "Tech": 65, "Econ": 50},
    "Russia": {"Army": 90, "Jets": 85, "Missiles": 100, "Tech": 80, "Econ": 60},
    "China Proxy": {"Army": 95, "Jets": 90, "Missiles": 95, "Tech": 95, "Econ": 98},
    "Israel": {"Army": 80, "Jets": 95, "Missiles": 95, "Tech": 98, "Econ": 80}
}

# 3. Interactive Strategic Selection
st.markdown("### 🛠️ Configure War-Gaming Alignment")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### 🔵 Western Bloc (US/UK Core)")
    west_allies = st.multiselect("Select Allies for West:", ["Germany", "France", "Israel", "India", "Australia", "Japan"], default=["Israel"])

with col_b:
    st.markdown("#### 🔴 Resistance Axis (Iran Core)")
    east_allies = st.multiselect("Select Allies for Iran:", ["Russia", "China Proxy", "North Korea", "Syria", "Iraq Militia"], default=["Russia"])

# 4. The Algorithm (Strategic Weighting)
def calculate_score(core_country, allied_list):
    total = military_data[core_country].copy()
    for ally in allied_list:
        if ally in military_data:
            for key in total:
                total[key] += (military_data[ally][key] * 0.6) # Allies provide 60% of their power as support
    
    # Weighted Result: Army(20%), Jets(30%), Missiles(25%), Tech(25%)
    final_score = (total["Army"]*0.2) + (total["Jets"]*0.3) + (total["Missiles"]*0.25) + (total["Tech"]*0.25)
    return final_score, total

west_score, west_stats = calculate_score("USA", west_allies)
east_score, east_stats = calculate_score("Iran", east_allies)

# Normalized Percentage
total_power = west_score + east_score
win_prob_west = (west_score / total_power) * 100
win_prob_east = 100 - win_prob_west

# 5. Simulation Dashboard
st.divider()
st.subheader("📊 Simulation Outcomes & Global Impact")

m1, m2, m3 = st.columns(3)
m1.metric("US-UK Bloc Win Probability", f"{win_prob_west:.1f}%")
m2.metric("Iran Axis Leverage", f"{win_prob_east:.1f}%")
# Global Stress Index based on total Jets and Missiles active
global_stress = (west_stats["Missiles"] + east_stats["Missiles"]) / 10
m3.metric("Global Cognitive Stress Index", f"{global_stress:.1f} Hz", "High Risk")

# Visualizing Power Comparison
df_compare = pd.DataFrame({
    "Category": ["Army", "Jets", "Missiles", "Tech", "Econ"],
    "US-UK Bloc": [west_stats[k] for k in ["Army", "Jets", "Missiles", "Tech", "Econ"]],
    "Iran Axis": [east_stats[k] for k in ["Army", "Jets", "Missiles", "Tech", "Econ"]]
})

fig = px.bar(df_compare, x="Category", y=["US-UK Bloc", "Iran Axis"], barmode='group', 
             title="Comparative Military & Asset Capabilities", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# 6. Strategic Deep-Dive
st.markdown("### 🏛️ Strategic & Management Analysis")
st.write(f"""
The simulation shows a **{win_prob_west:.1f}%** tactical advantage for the Western Bloc, primarily driven by **Jet Superiority** and **Economic Resilience**. 
However, the Iran Axis maintains high leverage through **Asymmetric Missile Capability** ({east_stats['Missiles']} units).

**Global Impact:**
1. **Financial Integrity:** High missile activity suggests a 200% surge in War Risk Insurance premiums.
2. **Cognitive Load:** A stress level of **{global_stress:.1f} Hz** indicates that global decision-makers are nearing 'Cognitive Exhaustion,' which leads to unethical reactive management.
3. **Theological Reflection:** True victory is not in military dominance, but in the preservation of human life and dignity. The goal of this data is to advocate for **Clarity over Chaos**.
""")

st.info("Developed by Mohd Khairul Ridhuan | Bridging Management, Theology, and Technology.")
