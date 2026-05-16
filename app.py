import streamlit as st
import sys
sys.path.append('.')
from utils.styles import apply_sidebar

st.set_page_config(
    page_title="RoadGuard Pakistan",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_sidebar()

# ── Hero Banner ──
st.markdown("""
<div style='background:linear-gradient(135deg, #0C447C 0%, #185FA5 100%);
            padding:48px 40px; border-radius:20px; margin-bottom:28px;
            text-align:center;'>
    <div style='font-size:64px; margin-bottom:12px;'>🛡️</div>
    <h1 style='color:white; margin:0; font-size:42px; font-weight:700;
               letter-spacing:0.02em;'>RoadGuard Pakistan</h1>
    <p style='color:#B5D4F4; font-size:18px; margin:12px 0 0 0;'>
        Data-driven road safety intelligence for Pakistan
    </p>
    <p style='color:rgba(255,255,255,0.6); font-size:13px; margin:8px 0 0 0;'>
        BS Data Science Project · 2026 · 🇵🇰
    </p>
</div>
""", unsafe_allow_html=True)

# ── KPI Stats ──
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("📊 EDA Charts", "15+")
with col2:
    st.metric("🗺️ Maps", "3")
with col3:
    st.metric("🤖 ML Models", "2")
with col4:
    st.metric("📋 Policy Recs", "7")
with col5:
    st.metric("🌍 Countries Compared", "11")

st.divider()

# ── Section title ──
st.markdown("""
<h2 style='color:#0C447C; text-align:center; margin-bottom:24px;'>
    🧭 Explore the Dashboard
</h2>
""", unsafe_allow_html=True)

# ── Page cards row 1 ──
col_a, col_b, col_c, col_d = st.columns(4)

cards = [
    ("📊", "Overview", "KPI cards showing total accidents, fatalities and injuries across Pakistan", "#185FA5"),
    ("🗺️", "Accident Map", "Interactive heatmap and choropleth maps of accident hotspots", "#0C447C"),
    ("📈", "EDA & Trends", "15+ charts with year range filter and province selection", "#185FA5"),
    ("🏙️", "Province Comparison", "Side-by-side radar chart and trend analysis per province", "#0C447C"),
]

for col, (icon, title, desc, color) in zip([col_a, col_b, col_c, col_d], cards):
    with col:
        st.markdown(f"""
        <div style='background:#F1EFE8; padding:20px; border-radius:14px;
                    border-top:4px solid {color}; height:160px;
                    margin-bottom:16px;'>
            <div style='font-size:32px; margin-bottom:8px;'>{icon}</div>
            <div style='font-weight:600; color:#0C447C; font-size:15px;
                        margin-bottom:6px;'>{title}</div>
            <div style='color:#5F5E5A; font-size:12px; line-height:1.5;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Page cards row 2 ──
col_e, col_f, col_g, col_h = st.columns(4)

cards2 = [
    ("🤖", "ML Predictions", "Predict accident severity and fatality risk using trained models", "#E24B4A"),
    ("🌍", "Int'l Benchmark", "Compare Pakistan road safety against 11 countries worldwide", "#185FA5"),
    ("🧮", "Risk Calculator", "Calculate your personal road accident risk score", "#0C447C"),
    ("⚠️", "Dangerous Roads", "Top 10 most dangerous highways mapped across Pakistan", "#E24B4A"),
]

for col, (icon, title, desc, color) in zip([col_e, col_f, col_g, col_h], cards2):
    with col:
        st.markdown(f"""
        <div style='background:#F1EFE8; padding:20px; border-radius:14px;
                    border-top:4px solid {color}; height:160px;
                    margin-bottom:16px;'>
            <div style='font-size:32px; margin-bottom:8px;'>{icon}</div>
            <div style='font-weight:600; color:#0C447C; font-size:15px;
                        margin-bottom:6px;'>{title}</div>
            <div style='color:#5F5E5A; font-size:12px; line-height:1.5;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Page cards row 3 ──
col_i, col_j, col_k, col_l = st.columns(4)

cards3 = [
    ("📋", "Province Scorecard", "Safety grade A-D with year-by-year breakdown per province", "#185FA5"),
    ("📋", "Policy Insights", "7 data-backed recommendations for Pakistan road safety", "#0C447C"),
    ("👤", "About", "Project background, team members and data sources", "#185FA5"),
    ("", "", "", ""),
]

for col, (icon, title, desc, color) in zip([col_i, col_j, col_k, col_l], cards3):
    with col:
        if icon:
            st.markdown(f"""
            <div style='background:#F1EFE8; padding:20px; border-radius:14px;
                        border-top:4px solid {color}; height:160px;
                        margin-bottom:16px;'>
                <div style='font-size:32px; margin-bottom:8px;'>{icon}</div>
                <div style='font-weight:600; color:#0C447C; font-size:15px;
                            margin-bottom:6px;'>{title}</div>
                <div style='color:#5F5E5A; font-size:12px; line-height:1.5;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# ── Crisis banner ──
st.markdown("""
<div style='background:#FCEBEB; padding:20px 28px; border-radius:12px;
            border-left:5px solid #E24B4A; margin-bottom:20px;'>
    <h4 style='color:#A32D2D; margin:0 0 6px 0;'>
        🚨 Pakistan Road Safety Crisis
    </h4>
    <p style='color:#5F5E5A; margin:0; font-size:14px; line-height:1.6;'>
        Pakistan records over <b>25,000–30,000 road fatalities annually</b>,
        making it one of the most dangerous countries for road users in Asia.
        <b>RoadGuard Pakistan</b> was built to bring transparency, data analysis,
        and predictive intelligence to this critical public safety issue.
    </p>
</div>
""", unsafe_allow_html=True)

st.caption("RoadGuard Pakistan · BS Data Science · 2026 · 🇵🇰 Pakistan")