import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. UI: "The Bloomberg Strategist" Theme
st.set_page_config(page_title="THE MORAL LEDGER v6.0", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #050a10; color: #d1d5db; }
    .stMetric { background-color: #111827; border: 1px solid #1f2937; border-radius: 4px; padding: 20px; }
    [data-testid="stMetricValue"] { color: #34d399 !important; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #f3f4f6; font-family: 'Helvetica Neue', sans-serif; letter-spacing: -0.5px; }
    .sidebar .sidebar-content { background-image: linear-gradient(#111827,#111827); color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar: Professional Alignment (Kekuatan Anda)
st.sidebar.title("STRATEGIC AUDITOR")
st.sidebar.markdown(f"""
---
**Mohd Khairul Ridhuan bin Mohd Fadzil**
*Researcher in Management & Theology*

**Audit Pillars:**
- ⚖️ **Theological Integrity:** Maqasid-based Risk
- 📈 **Corporate Sustainability:** Long-term Human Capital
- 🧠 **Cognitive Audit:** Decision-Maker Resilience
- 💻 **HCI:** Strategic Information Design
""")

st.title("🏛️ THE MORAL LEDGER: Geopolitical Management Entropy")
st.markdown("##### *Quantifying the 'Underexplored' Hidden Costs of Conflict on Institutional Integrity*")

# 3. The "Overlooked" Variables (Inputs)
st.sidebar.divider()
st.sidebar.subheader("Conflict Audit Parameters")
institutional_decay = st.sidebar.slider("Institutional Entropy (Management Decay)", 0, 100, 35)
moral_debt_index = st.sidebar.slider("Generational Moral Debt", 0, 100, 50)
transparency_leak = st.sidebar.slider("Information Integrity Leakage", 0, 100, 25)

# 4. Logic: The Entropy Formula
# Expert Concept: Moral Attrition is a result of Management Decay + Lack of Transparency
stability_score = 100 - (institutional_decay * 0.4 + moral_debt_index * 0.4 + transparency_leak * 0.2)
recovery_years = (institutional_decay / 10) * 3  # Every 10% decay takes 3 years to recover

# 5. Visual 1: Institutional Integrity Flow (Sankey)
fig_flow = go.Figure(data=[go.Sankey(
    node = dict(pad = 15, thickness = 20, line = dict(color = "black", width = 0.5),
      label = ["Ethical Capital", "Management Integrity", "Strategic Purpose", "Institutional Decay", "Sustainability Gap"],
      color = ["#3b82f6", "#10b981", "#6366f1", "#ef4444", "#f59e0b"]),
    link = dict(
      source = [0, 1, 1, 2, 2], 
      target = [1, 3, 2, 4, 3],
      value = [100, institutional_decay, 100-institutional_decay, moral_debt_index, institutional_decay*0.5]
  ))])
fig_flow.update_layout(title_text="<b>Institutional Energy Leakage: How Conflict Erodes Purpose</b>", 
                       template="plotly_dark", font_size=12, height=400, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# 6. Visual 2: The Sustainability Radar (Audit Framework)
categories = ['Ethical Leadership', 'Strategic Clarity', 'Human Dignity', 'Financial Integrity', 'Generational Trust']
audit_values = [
    100 - institutional_decay,
    100 - transparency_leak,
    100 - moral_debt_index,
    80 - (institutional_decay * 0.5),
    100 - (moral_debt_index * 0.8)
]

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(r=audit_values, theta=categories, fill='toself', name='Current Audit',
                                   line_color='#34d399', fillcolor='rgba(52, 211, 153, 0.2)'))
fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100], gridcolor="#374151")),
                        showlegend=False, template="plotly_dark", height=450, title="<b>Audit Result: Resilience vs Entropy</b>",
                        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# Layout
c1, c2 = st.columns([1.2, 0.8])
with c1:
    st.plotly_chart(fig_flow, use_container_width=True)
with c2:
    st.plotly_chart(fig_radar, use_container_width=True)

# 7. Professional Metrics (Audit Summary)
st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Institutional Stability", f"{stability_score:.1f}%", "-Low" if stability_score < 50 else "Stable")
m2.metric("Moral Recovery Period", f"{recovery_years:.1f} Years", "Generational Gap")
m3.metric("Management Entropy", f"{institutional_decay}%", "Critical" if institutional_decay > 60 else "Rising")

# 8. Expert Commentary: The Overlooked Perspective
st.divider()
st.subheader("🕵️ Analyst Insight: The Theology of Global Risk")
st.markdown(f"""
Most geopolitical models overlook the **Generational Moral Debt** created during a crisis. As a researcher in **Management and Theology**, I look at the 'Internal Border' of an organization.

1. **Management Entropy:** Conflict forces institutions to abandon long-term **Sustainability (Maqasid)** for short-term survival. This creates a decay in institutional soul that takes approximately **{recovery_years:.1f} years** to fix.
2. **The Integrity Leak:** When transparency drops by **{transparency_leak}%**, the 'Management Integrity' flow redirects into **'Systemic Risk'**.
3. **The Sustainability Gap:** Geopolitics is not about who wins today; it is about who maintains the **Generational Trust** required for tomorrow's economy.

**Transparency is not just a policy; it is the preservation of the Intellectual and Moral Soul (Aql & Nafs) of an institution.**
""")

st.markdown("<div style='text-align: center; color: #4b5563; padding: 20px;'>Mohd Khairul Ridhuan | Interdisciplinary Strategic Audit v6.0</div>", unsafe_allow_html=True)
