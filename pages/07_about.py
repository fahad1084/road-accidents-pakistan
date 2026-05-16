import streamlit as st
import sys
sys.path.append('.')
from utils.styles import apply_sidebar

st.set_page_config(page_title="About | RoadGuard Pakistan",
                   page_icon="👤", layout="wide")

apply_sidebar()

NAVY = '#0C447C'
BLUE = '#185FA5'
OFF_WHITE = '#F1EFE8'
RED = '#E24B4A'
SKY = '#378ADD'

st.title("👤 About RoadGuard Pakistan")
st.markdown("#### Project background, team, data sources and technical details")
st.divider()

# ── Project overview banner ──
st.markdown(f"""
<div style='background:{NAVY}; padding:28px 32px; border-radius:14px;
            margin-bottom:24px;'>
    <h3 style='color:white; margin:0 0 10px 0;'>🛡️ RoadGuard Pakistan</h3>
    <p style='color:#E6F1FB; margin:0; line-height:1.7; font-size:15px;'>
        Pakistan records over <b>25,000–30,000 road fatalities annually</b> —
        one of the highest rates in Asia — yet no centralised, publicly accessible
        analytical platform existed. <b>RoadGuard Pakistan</b> was built to address
        this gap by transforming raw accident data into actionable insights through
        an interactive web dashboard, machine learning models, and data-backed
        policy recommendations.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Team Members ──
st.subheader("👥 Team Members")

col1, col2, col3 = st.columns(3)

team = [
    ("Muhammad Fahad Noor", "232448", "Team Lead & ML Engineer",
     "Data collection, ML model development, dashboard integration", "🧑‍💻"),
    ("Muhammad Bilal", "232442", "Data Analyst & EDA",
     "Data cleaning, exploratory analysis, chart development", "📊"),
    ("Hussnain Dogar", "232517", "Frontend & Geospatial",
     "Streamlit dashboard, geospatial maps, deployment", "🗺️"),
]

for col, (name, roll, role, contrib, icon) in zip([col1, col2, col3], team):
    with col:
        st.markdown(f"""
        <div style='background:{OFF_WHITE}; padding:24px 20px; border-radius:14px;
                    border-top:4px solid {BLUE}; text-align:center;
                    margin-bottom:16px;'>
            <div style='font-size:48px; margin-bottom:10px;'>{icon}</div>
            <div style='font-weight:600; color:{NAVY}; font-size:16px;
                        margin-bottom:4px;'>{name}</div>
            <div style='color:{BLUE}; font-size:13px; font-weight:500;
                        margin-bottom:4px;'>Roll No: {roll}</div>
            <div style='color:#5F5E5A; font-size:12px; font-weight:500;
                        margin-bottom:8px;'>{role}</div>
            <div style='color:#5F5E5A; font-size:11px; line-height:1.5;
                        border-top:1px solid #D3D1C7; padding-top:8px;'>
                {contrib}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ── Project details & ML ──
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Project Details")
    details = {
        "Project Type": "BS Data Science Group Project",
        "Duration": "8 Weeks (April–May 2026)",
        "Team Size": "3 Members",
        "Dashboard": "Streamlit Web App",
        "Deployment": "Streamlit Community Cloud",
        "Version": "V2.0",
        "Status": "✅ Complete",
        "Live URL": "streamlit.app"
    }
    for key, val in details.items():
        st.markdown(f"""
        <div style='display:flex; justify-content:space-between;
                    padding:8px 12px; border-radius:6px; margin-bottom:4px;
                    background:{OFF_WHITE};'>
            <span style='color:#5F5E5A; font-size:13px;'>{key}</span>
            <span style='color:{NAVY}; font-size:13px; font-weight:500;'>{val}</span>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.subheader("🤖 ML Model Performance")
    models = [
        ("Severity Classifier", "Random Forest", "Accuracy", "100%", "✅"),
        ("Fatality Regressor", "Gradient Boosting", "R²", "0.9958", "✅"),
        ("Baseline Classifier", "Logistic Regression", "Accuracy", "92.31%", "✅"),
        ("Baseline Regressor", "Linear Regression", "R²", "0.9984", "✅"),
    ]
    for name, algo, metric, score, status in models:
        st.markdown(f"""
        <div style='padding:10px 14px; border-radius:8px; margin-bottom:6px;
                    background:{OFF_WHITE}; border-left:4px solid {BLUE};'>
            <div style='font-weight:500; color:{NAVY}; font-size:14px;'>{name}</div>
            <div style='color:#5F5E5A; font-size:12px; margin-top:2px;'>
                {algo} &nbsp;·&nbsp; {metric}:
                <b style='color:{RED};'>{score}</b> &nbsp;{status}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ── Data sources ──
st.subheader("📦 Data Sources")
sources = [
    ("NTRC & PBS via Kaggle",
     "Province-level accident data 2006–2023 across all provinces",
     "https://www.kaggle.com/datasets/ahsanneural/pakistan-traffic-accidents-ntrc-and-pbs"),
    ("Road Accident in Pakistan 2012–2021",
     "Monthly national accident records by province",
     "https://www.kaggle.com/datasets/mohsinali123/road-accident-in-pakistan-2012-2021"),
    ("Rescue 1122 Punjab",
     "District-level emergency call data for 37 Punjab districts",
     "https://www.kaggle.com"),
    ("GADM Shapefiles",
     "Pakistan province & district boundary shapefiles (levels 0–3)",
     "https://gadm.org"),
    ("Open-Meteo API",
     "Free weather API for major Pakistani cities",
     "https://open-meteo.com"),
    ("WHO Global Road Safety Report 2023",
     "International benchmarking data for 11 countries",
     "https://www.who.int/publications/i/item/9789240086517"),
]

for name, desc, url in sources:
    st.markdown(f"""
    <div style='padding:12px 16px; border-radius:8px; margin-bottom:6px;
                background:{OFF_WHITE}; border-left:4px solid {NAVY};'>
        <div style='font-weight:500; color:{NAVY}; font-size:14px;'>{name}</div>
        <div style='color:#5F5E5A; font-size:12px; margin-top:2px;'>{desc}</div>
        <a href='{url}' target='_blank'
           style='color:{BLUE}; font-size:11px;'>🔗 {url}</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── Tech stack ──
st.subheader("🛠️ Tech Stack")
col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("**Dashboard**")
    for lib in ["Streamlit 1.28+", "streamlit-folium", "Plotly", "Seaborn"]:
        st.markdown(f"- {lib}")

with col4:
    st.markdown("**Data & ML**")
    for lib in ["Pandas", "NumPy", "scikit-learn", "XGBoost", "joblib"]:
        st.markdown(f"- {lib}")

with col5:
    st.markdown("**Mapping**")
    for lib in ["Folium", "GeoPandas", "GADM Shapefiles", "Open-Meteo API"]:
        st.markdown(f"- {lib}")

st.divider()

# ── Version history ──
st.subheader("📌 Version History")
versions = [
    ("V1.0", "May 2026",
     "Core dashboard — 15 EDA charts, 3 interactive maps, 2 ML models, 7 policy recommendations, About page"),
    ("V2.0", "May 2026",
     "Enhanced — International benchmarking, Risk calculator, Province scorecard, Dangerous roads map, CSV download, Year filter"),
]
for ver, date, desc in versions:
    st.markdown(f"""
    <div style='padding:12px 16px; border-radius:8px; margin-bottom:6px;
                background:{OFF_WHITE}; border-left:4px solid {BLUE};'>
        <div style='display:flex; justify-content:space-between;'>
            <span style='font-weight:600; color:{NAVY};'>{ver}</span>
            <span style='color:#5F5E5A; font-size:12px;'>{date}</span>
        </div>
        <div style='color:#5F5E5A; font-size:13px; margin-top:4px;'>{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── Footer ──
st.markdown(f"""
<div style='background:{OFF_WHITE}; padding:16px 20px; border-radius:10px;
            border-left:4px solid {NAVY}; text-align:center;'>
    <p style='margin:0; color:{NAVY}; font-size:14px;'>
        <b>RoadGuard Pakistan</b> — BS Data Science Group Project · 2026 🇵🇰
    </p>
    <p style='margin:4px 0 0 0; color:#5F5E5A; font-size:12px;'>
        Muhammad Fahad Noor (232448) · Muhammad Bilal (232442) · Hussnain Dogar (232517)
    </p>
</div>
""", unsafe_allow_html=True)