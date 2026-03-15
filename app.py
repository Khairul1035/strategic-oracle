import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. UI: "The Clean Auditor" Theme (High Readability)
st.set_page_config(page_title="THE MORAL LEDGER v6.1", layout="wide")

st.markdown("""
    <style>
    /* Background and Main Font */
    .main { background-color: #ffffff; color: #1f2937; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* Metrics Box Styling (Sharp & Professional) */
    [data-testid="stMetricValue"] { 
        color: #059669 !important; 
        font-size: 2.8rem !important; 
        font-weight: 800 !important; 
    }
    [data-testid="stMetricLabel"] { 
        color: #4b5563 !important; 
        font-size: 1.1rem !important; 
        font-weight: 600 !important; 
    }
    .stMetric { 
        background-color: #f9fafb; 
        border: 1px solid #e5e7eb; 
        border-radius: 8px; 
        padding: 25px; 
    }

    /* Titles */
    h1, h2, h3 { color: #111827; font-weight: 800; }
    
    /* Sidebar */
    .css-1d391kg { background-color: #111827; }
    .sidebar-text { color: #ffffff; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar: Professional Alignment
st.sidebar.title("STRATEGIC ARCHITECT")
st.sidebar.markdown(f"""
<div class="sidebar-text">
<strong>Mohd Khairul Ridhuan bin Mohd Fadzil</strong><br>
<em>Researcher: Management & Theology</em><br><br>
<strong>Audit Focus:</strong><br>
- ⚖️ Theological Integrity<br>
- 📈 Sustainability Audit<br>
- 🧠 Cognitive Resilience<br>
- 💻 Strategic HCI Design
</div>
""", unsafe_allow_html=True)

st.title("🏛️ THE MORAL LEDGER v6.1: Institutional Integrity Audit")
st.markdown("##### *Quantifying Underexplored Hidden Costs: Management Entropy & Moral Debt*")

# 3. Parameters (The Inputs)
st.divider()
st.subheader("⚙️ Audit Parameters (Geopolitical Stress Factors)")
c_in1, c_in2, c_in3 = st.columns(3)
with c_in1:
    inst_decay = st.slider("Institutional Entropy (Management Decay)", 0, 100, 20)
with c_in2:
    moral_debt = st.slider("Generational Moral Debt Index", 0, 100, 40)
with c_in3:
    trust_leak = st.slider("Information Integrity Leakage", 0, 100, 15)

# 4. Logic: The Integrity Formula
stability = 100 - (inst_decay * 0.4 + moral_debt * 0.4 + trust_leak * 0.2)
recovery = (inst_decay / 10) * 3

# 5. Visual 1: Sankey Diagram (High Contrast Labels)
fig_flow = go.Figure(data=[go.Sankey(
    node = dict(pad = 30, thickness = 30, line = dict(color = "white", width = 2),
      label = ["ETHICAL CAPITAL", "MANAGEMENT INTEGRITY", "STRATEGIC PURPOSE", "INSTITUTIONAL DECAY", "SUSTAINABILITY GAP"],
      color = ["#2563eb", "#10b981", "#6366f1", "#ef4444", "#f59e0b"]),
    link = dict(
      source = [0, 1, 1, 2, 2], 
      target = [1, 3, 2, 4, 3],
      value = [100, inst_decay, 100-inst_decay, moral_debt, inst_decay*0.5]
  ))])
fig_flow.update_layout(title_text="<b>RESOURCE FLOW: How Conflict Erodes Institutional Integrity</b>", 
                       font=dict(size=14, color="black"), height=450, template="plotly_white")

# 6. Visual 2: Radar Chart (Clear & Sharp)
categories = ['Ethical Leadership', 'Strategic Clarity', 'Human Dignity', 'Financial Integrity', 'Generational Trust']
audit_values = [100-inst_decay, 100-trust_leak, 100-moral_debt, 85-(inst_decay*0.5), 100-(moral_debt*0.8)]

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(r=audit_values, theta=categories, fill='toself', name='Audit Score',
                                   line_color='#059669', fillcolor='rgba(5, 150, 105, 0.2)'))
fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100], gridcolor="#e5e7eb")),
                        showlegend=False, template="plotly_white", height=450, 
                        title="<b>AUDIT PROFILE: Institutional Resilience Star</b>",
                        font=dict(size=13, color="black"))

# Executive Layout
col_left, col_right = st.columns([1.2, 0.8])
with col_left:
    st.plotly_chart(fig_flow, use_container_width=True)
with col_right:
    st.plotly_chart(fig_radar, use_container_width=True)

# 7. Metrics (The Dashboard Numbers)
st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("INSTITUTIONAL STABILITY", f"{stability:.1f}%")
m2.metric("MORAL RECOVERY PERIOD", f"{recovery:.1f} YEARS")
m3.metric("MANAGEMENT ENTROPY", f"{inst_decay}%")

# 8. Analyst Narrative (English Corporate Style)
st.divider()
st.subheader("🕵️ Analyst Insight: The Theology of Global Management")
st.markdown(f"""
Traditional geopolitical models focus on external borders; this audit focuses on the **Internal Borders of Integrity.** 
As a researcher bridging **Management and Theology**, I evaluate how conflict decays the 'Institutional Soul.'

1. **Management Entropy:** Geopolitical stress forces institutions to abandon long-term **Sustainability (Maqasid)** for short-term survival. This creates an 'Entropy' that requires approximately **{recovery:.1f} years** of ethical rebuilding.
2. **Generational Moral Debt:** The 'Hidden Cost' of conflict is the erosion of **Human Dignity** and **Generational Trust**. When these scores drop, the 'Sustainability Gap' widens, threatening the future economic order.
3. **The Solution:** True resilience is found in **Ethical Strategic Governance.** We must protect the 'Intellectual and Moral Capital' (Aql & Nafs) of our institutions to ensure long-term survival.

**Transparency is the most strategic form of Charity (Sadaqah) in a crisis.**
""")

st.markdown("<div style='text-align: center; color: #94a3b8; padding: 20px;'>Developed by Mohd Khairul Ridhuan | Interdisciplinary Research v6.1</div>", unsafe_allow_html=True)
