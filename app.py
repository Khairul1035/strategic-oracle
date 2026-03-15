import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. UI: "The Auditor's Office" (Ultimate High-Contrast)
st.set_page_config(page_title="THE MORAL LEDGER v6.2", layout="wide")

st.markdown("""
    <style>
    /* Main Background */
    .main { background-color: #ffffff; color: #1e293b; }
    
    /* SIDEBAR STYLING - Fixed Contrast */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important; /* Midnight Blue */
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #f8fafc !important;
    }
    .sidebar-content-text {
        color: #e2e8f0 !important; /* Light Grey/White */
        font-size: 1rem;
        line-height: 1.6;
    }
    .sidebar-highlight {
        color: #38bdf8 !important; /* Sky Blue for emphasis */
        font-weight: 700;
    }

    /* Metrics Box Styling */
    [data-testid="stMetricValue"] { 
        color: #059669 !important; 
        font-size: 2.8rem !important; 
        font-weight: 800 !important; 
    }
    [data-testid="stMetricLabel"] { 
        color: #475569 !important; 
        font-size: 1.1rem !important; 
        font-weight: 600 !important; 
    }
    .stMetric { 
        background-color: #f8fafc; 
        border: 1px solid #e2e8f0; 
        border-radius: 8px; 
        padding: 25px; 
    }

    /* Global Typography */
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    h1, h2, h3 { color: #0f172a; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar: Professional Alignment (High Visibility)
st.sidebar.title("STRATEGIC ARCHITECT")
st.sidebar.markdown(f"""
<div class="sidebar-content-text">
    <span class="sidebar-highlight">Mohd Khairul Ridhuan bin Mohd Fadzil</span><br>
    <em>Researcher: Management & Theology</em><br><br>
    <strong>Audit Framework:</strong><br>
    ⚖️ Theological Integrity<br>
    📈 Sustainability Audit<br>
    🧠 Cognitive Resilience<br>
    💻 Strategic HCI Design
</div>
""", unsafe_allow_html=True)

st.title("🏛️ THE MORAL LEDGER v6.2: Institutional Integrity Audit")
st.markdown("##### *Quantifying Hidden Costs: Management Entropy & Moral Debt*")

# 3. Parameters (The Inputs)
st.divider()
st.subheader("⚙️ Strategic Audit Parameters")
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
fig_flow.update_layout(title_text="<b>RESOURCE FLOW: Institutional Integrity Erosion</b>", 
                       font=dict(size=14, color="black"), height=450, template="plotly_white")

# 6. Visual 2: Radar Chart (Clear & Sharp)
categories = ['Ethical Leadership', 'Strategic Clarity', 'Human Dignity', 'Financial Integrity', 'Generational Trust']
audit_values = [100-inst_decay, 100-trust_leak, 100-moral_debt, 85-(inst_decay*0.5), 100-(moral_debt*0.8)]

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(r=audit_values, theta=categories, fill='toself', name='Audit Score',
                                   line_color='#059669', fillcolor='rgba(5, 150, 105, 0.2)'))
fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100], gridcolor="#e5e7eb")),
                        showlegend=False, template="plotly_white", height=450, 
                        title="<b>AUDIT PROFILE: Resilience Framework</b>",
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
2. **Generational Moral Debt:** The 'Hidden Cost' of conflict is the erosion of **Human Dignity** and **Generational Trust**. When ini scores drop, the 'Sustainability Gap' widens.
3. **The Solution:** True resilience is found in **Ethical Strategic Governance.** We must protect the 'Intellectual and Moral Capital' (Aql & Nafs) of our institutions.

**Transparency is the most strategic form of Charity (Sadaqah) in a crisis.**
""")

st.markdown("<div style='text-align: center; color: #94a3b8; padding: 20px;'>Developed by Mohd Khairul Ridhuan | Interdisciplinary Research v6.2</div>", unsafe_allow_html=True)
