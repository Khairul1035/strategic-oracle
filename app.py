import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 1. HCI Configuration: "Intelligence Command Centre" Feel
st.set_page_config(page_title="NEURO-STRAT v5.0", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e0e0e0; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar: Interdisciplinary Identity
st.sidebar.title("Strategic Architect")
st.sidebar.info("Mohd Khairul Ridhuan bin Mohd Fadzil")
st.sidebar.markdown("""
**Interdisciplinary Lens:**
- 🏛️ **Theology:** Maqasid Stability Framework
- 💼 **Management:** Ethical Decision Windows
- 🧠 **Neuroscience:** Cognitive Fatigue Modeling
- 💻 **HCI:** Intuitive Risk Visualization
""")

st.title("🧠 NEURO-STRAT v5.0: The Moral-Cognitive Intelligence Suite")
st.caption("Exploring Underexplored Dimensions: Moral Attrition & Ethical Decision Windows")

# 2. Interactive Inputs: Setting the "Moral Climate"
st.subheader("⚙️ Global Ethical-Cognitive Parameters")
col_input1, col_input2, col_input3 = st.columns(3)

with col_input1:
    conflict_intensity = st.slider("Conflict Duration (Months)", 1, 48, 12)
with col_input2:
    resource_scarcity = st.select_slider("Resource Scarcity Level", options=["Low", "Moderate", "High", "Critical"], value="Moderate")
with col_input3:
    diplomatic_trust = st.slider("Global Diplomatic Trust (%)", 0, 100, 45)

# 3. Logic: Calculating "Ethical Decision Window" & "Moral Attrition"
# Concept: As conflict duration increases and trust decreases, the time a leader takes to make an ethical choice shrinks.
scarcity_map = {"Low": 1, "Moderate": 2, "High": 3, "Critical": 4}
decision_window = max(5, 100 - (conflict_intensity * 1.5) - (scarcity_map[resource_scarcity] * 10) + (diplomatic_trust * 0.2))
moral_attrition = min(100, (conflict_intensity * 2) + (scarcity_map[resource_scarcity] * 15) - (diplomatic_trust * 0.3))

# 4. Visualization 1: Maqasid Stability Star (Radar Chart)
# We map the 5 pillars of Maqasid to show global stability beyond GDP.
maqasid_labels = ['Faith (Religion)', 'Life (Soul)', 'Intellect', 'Progeny', 'Wealth']
maqasid_values = [
    max(20, diplomatic_trust), # Faith/Trust
    max(10, 100 - moral_attrition), # Life
    max(10, decision_window), # Intellect/Logic
    max(30, 80 - (conflict_intensity * 0.5)), # Progeny/Future
    max(10, 90 - (scarcity_map[resource_scarcity] * 20)) # Wealth
]

fig_star = go.Figure()
fig_star.add_trace(go.Scatterpolar(
      r=maqasid_values,
      theta=maqasid_labels,
      fill='toself',
      name='Stability Profile',
      line_color='#00ffcc',
      fillcolor='rgba(0, 255, 204, 0.3)'
))
fig_star.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100], gridcolor="#30363d")),
    showlegend=False, template="plotly_dark", height=450, title="Maqasid Stability Star (Holistic Resilience)"
)

# 5. Visualization 2: The Ethical Flow (Sankey Diagram)
# Visualizing how "Integrity" flows into "Risk" or "Resilience"
fig_sankey = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15, thickness = 20, line = dict(color = "black", width = 0.5),
      label = ["Global Integrity", "Ethical Decision", "Unethical Shortcut", "Resilience", "Systemic Risk", "Moral Attrition"],
      color = ["#3366cc", "#10b981", "#ef4444", "#10b981", "#f59e0b", "#ef4444"]
    ),
    link = dict(
      source = [0, 0, 1, 1, 2, 2],
      target = [1, 2, 3, 5, 4, 5],
      value = [decision_window, 100-decision_window, decision_window*0.8, decision_window*0.2, (100-decision_window)*0.7, (100-decision_window)*0.3]
  ))])
fig_sankey.update_layout(title_text="The Flow of Ethical Capital under Geopolitical Stress", template="plotly_dark", height=400)

# 6. Final Dashboard Layout
st.divider()
c1, c2 = st.columns([1, 1])
with c1:
    st.plotly_chart(fig_star, use_container_width=True)
with c2:
    st.plotly_chart(fig_sankey, use_container_width=True)

# Professional Metrics
st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Ethical Decision Window", f"{decision_window:.1f} Sec", "Shrinking" if decision_window < 50 else "Stable")
m2.metric("Moral Attrition Rate", f"{moral_attrition:.1f}%", "Rising" if moral_attrition > 40 else "Low")
m3.metric("Maqasid Stability Index", f"{sum(maqasid_values)/5:.1f}/100")

# 7. Strategic Reflection: The "Fresh" Narrative
st.markdown("### 🏛️ Strategic Narrative: Beyond the Battlefield")
st.write(f"""
Projek ini menyelami dimensi yang sering diabaikan: **Resiliensi Rohani dan Kognitif.**

1. **Maqasid Stability Star:** Kita tidak melihat berapa banyak misil yang ada, tetapi sejauh mana **'Intellect' (Aql)** dan **'Life' (Nafs)** masih terpelihara. Apabila 'Star' ini mengecil, itu adalah tanda keruntuhan tamadun, bukan sekadar kekalahan tentera.
2. **Ethical Decision Window:** Data menunjukkan bahawa di bawah stres geopolitik yang ekstrem, pemimpin beralih kepada **'System 1 Thinking'** (Intuitif & Impulsif). Ini memendekkan waktu untuk pertimbangan moral, meningkatkan risiko **'Moral Attrition'**.
3. **The Solution:** Untuk memperbaiki dunia, kita tidak perlukan lebih banyak senjata, tetapi peningkatan **'Cognitive Buffer'** melalui pengurusan beretika yang berpaksikan nilai-nilai ketuhanan (Theology).

**Transparency is the antidote to Moral Attrition.** 
""")

st.info("Developed by Mohd Khairul Ridhuan | Bridging Theology, Management, and Neuroscience.")
