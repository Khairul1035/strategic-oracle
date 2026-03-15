import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. HCI & Visual Authority: "Executive Slate" Theme
st.set_page_config(page_title="NEURO-STRAT v5.1", layout="wide")

# Custom CSS for Typography and Visual Clarity
st.markdown("""
    <style>
    /* Main Background and Font */
    .main { background-color: #f0f2f6; color: #1e293b; }
    html, body, [class*="css"]  { font-family: 'Inter', sans-serif; font-size: 16px; }
    
    /* Metrics Styling */
    [data-testid="stMetricValue"] { font-size: 2.2rem !important; font-weight: 700 !important; color: #0f172a !important; }
    [data-testid="stMetricLabel"] { font-size: 1.1rem !important; font-weight: 500 !important; color: #475569 !important; }
    
    /* Box Containers */
    .stMetric { 
        background-color: #ffffff; 
        border: 1px solid #e2e8f0; 
        border-radius: 12px; 
        padding: 20px; 
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); 
    }
    
    /* Sidebar Clarity */
    .css-1d391kg { background-color: #1e293b; }
    .sidebar-text { color: #f8fafc; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar: Professional Identity
st.sidebar.title("Strategic Architect")
st.sidebar.markdown(f"""
<div class="sidebar-text">
<strong>Mohd Khairul Ridhuan bin Mohd Fadzil</strong><br><br>
<strong>Interdisciplinary Focus:</strong><br>
- 🏛️ Theology: Maqasid Framework<br>
- 💼 Management: Ethical Governance<br>
- 🧠 Neuroscience: Cognitive Stress<br>
- 💻 HCI: Decision-Support Systems
</div>
""", unsafe_allow_html=True)

st.title("🧠 NEURO-STRAT v5.1: The Moral Resilience Suite")
st.markdown("##### *A Predictive Simulation of Ethical Integrity & Systemic Stability under Geopolitical Stress*")

# 2. Strategic Control Panel (Inputs)
st.divider()
st.subheader("⚙️ Global Ethical-Cognitive Parameters")
col_input1, col_input2, col_input3 = st.columns(3)

with col_input1:
    conflict_intensity = st.slider("Conflict Duration (Months)", 1, 48, 12)
with col_input2:
    resource_scarcity = st.select_slider("Resource Scarcity Level", options=["Low", "Moderate", "High", "Critical"], value="Moderate")
with col_input3:
    diplomatic_trust = st.slider("Global Diplomatic Trust (%)", 0, 100, 45)

# 3. Logic: Quantitative Modeling of Moral Attrition
scarcity_map = {"Low": 1, "Moderate": 2, "High": 3, "Critical": 4}
decision_window = max(5, 100 - (conflict_intensity * 1.5) - (scarcity_map[resource_scarcity] * 10) + (diplomatic_trust * 0.2))
moral_attrition = min(100, (conflict_intensity * 2) + (scarcity_map[resource_scarcity] * 15) - (diplomatic_trust * 0.3))

# 4. Visualization 1: Maqasid Stability Star (High Contrast)
maqasid_labels = ['Faith (Integrity)', 'Life (Humanity)', 'Intellect (Logic)', 'Progeny (Future)', 'Wealth (Econ)']
maqasid_values = [
    max(20, diplomatic_trust), 
    max(10, 100 - moral_attrition), 
    max(10, decision_window), 
    max(30, 80 - (conflict_intensity * 0.5)), 
    max(10, 90 - (scarcity_map[resource_scarcity] * 20))
]

fig_star = go.Figure()
fig_star.add_trace(go.Scatterpolar(
      r=maqasid_values, theta=maqasid_labels, fill='toself',
      name='Resilience Profile', line_color='#2563eb', fillcolor='rgba(37, 99, 235, 0.3)'
))
fig_star.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100], gridcolor="#e2e8f0", tickfont=dict(size=12))),
    showlegend=False, template="plotly_white", height=500, font=dict(size=14, color="#1e293b"),
    title="<b>Maqasid Stability Star: Holistic Resilience</b>"
)

# 5. Visualization 2: The Ethical Flow (Sankey)
fig_sankey = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 20, thickness = 30, line = dict(color = "white", width = 1),
      label = ["Global Integrity", "Ethical Decision", "Unethical Shortcut", "Resilience", "Systemic Risk", "Moral Attrition"],
      color = ["#334155", "#10b981", "#ef4444", "#10b981", "#f59e0b", "#ef4444"]
    ),
    link = dict(
      source = [0, 0, 1, 1, 2, 2],
      target = [1, 2, 3, 5, 4, 5],
      value = [decision_window, 100-decision_window, decision_window*0.8, decision_window*0.2, (100-decision_window)*0.7, (100-decision_window)*0.3]
  ))])
fig_sankey.update_layout(
    title_text="<b>The Flow of Ethical Capital under Geopolitical Stress</b>",
    template="plotly_white", height=450, font=dict(size=14, color="#1e293b")
)

# 6. Executive Layout
st.divider()
c1, c2 = st.columns([1, 1])
with c1:
    st.plotly_chart(fig_star, use_container_width=True)
with c2:
    st.plotly_chart(fig_sankey, use_container_width=True)

# Metrics Section
st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Ethical Decision Window", f"{decision_window:.1f} Sec", delta_color="inverse")
m2.metric("Moral Attrition Rate", f"{moral_attrition:.1f}%", delta_color="normal")
m3.metric("Maqasid Stability Index", f"{sum(maqasid_values)/5:.1f}/100")

# 7. Strategic Narrative (English Corporate Translation)
st.divider()
st.subheader("🏛️ Strategic Intelligence: Beyond the Battlefield")
st.markdown(f"""
This simulation explores an underexplored dimension of global conflict: **The Erosion of Moral and Cognitive Resilience.**

1. **Maqasid Stability Star:** Unlike kinetic data that measures missile counts, this index measures the preservation of the five fundamental pillars of human civilization. A shrinking 'Star' signifies a collapse of civilizational values, which is far more critical than a tactical military defeat.
2. **Ethical Decision Window:** Data suggest that under extreme geopolitical pressure, leaders shift from analytical reasoning to impulsive 'System 1 Thinking.' This shortens the 'Moral Window,' leading to an accelerated **Moral Attrition Rate**.
3. **The Conclusion:** Global restoration requires more than just economic recovery; it requires a **Cognitive Buffer** built upon values-based management (Theology) and data-driven clarity (Management).

**Transparency is the ultimate antidote to Systemic Risk.**
""")

st.markdown("<div style='text-align: center; color: #94a3b8; padding: 20px;'>Developed by Mohd Khairul Ridhuan bin Mohd Fadzil | Interdisciplinary Research v5.1</div>", unsafe_allow_html=True)
