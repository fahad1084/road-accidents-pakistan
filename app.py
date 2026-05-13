"""
RoadGuard Pakistan
==================
Road Traffic Accident Analysis Dashboard
BS Data Science Project | 2026
"""

import streamlit as st

st.set_page_config(
    page_title="RoadGuard Pakistan",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown("## 🛡️ RoadGuard Pakistan")
st.sidebar.markdown("*Data-driven road safety intelligence for Pakistan*")
st.sidebar.divider()

st.title("🛡️ RoadGuard Pakistan")
st.markdown("### Road Traffic Accident Analysis Dashboard")
st.markdown(
    """
    Welcome to **RoadGuard Pakistan** — a data-driven platform for exploring,
    analysing, and predicting road traffic accidents across Pakistan.

    Use the sidebar to navigate between sections:
    - 📊 **Overview** — KPIs and summary statistics
    - 🗺️ **Accident Map** — Interactive hotspot heatmap
    - 📈 **EDA & Trends** — 15+ exploratory charts
    - 🏙️ **Province Comparison** — Regional breakdown
    - 🤖 **ML Predictions** — Severity & fatality predictor
    - 📋 **Policy Insights** — Data-backed recommendations
    """
)

st.divider()
st.caption("BS Data Science Project · April 2026 · Pakistan")
