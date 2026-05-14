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

st.title("🛡️ RoadGuard Pakistan")
st.markdown("### Road Traffic Accident Analysis Dashboard")
st.markdown("""
Welcome to **RoadGuard Pakistan** — use the sidebar to navigate between sections.
""")
st.divider()
st.caption("BS Data Science Project · April 2026 · Pakistan")