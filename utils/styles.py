import streamlit as st


def apply_sidebar():
    """Apply consistent branded sidebar to all pages"""

    st.markdown("""
    <style>
    /* ── Sidebar background ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(160deg, #0C447C 0%, #185FA5 100%) !important;
    }

    /* ── Hide default page nav links ── */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* ── All sidebar text white ── */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div {
        color: #E6F1FB !important;
    }

    /* ── Sidebar divider ── */
    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.15) !important;
        margin: 12px 0 !important;
    }

    /* ── Metric cards ── */
    [data-testid="metric-container"] {
        background: #F1EFE8 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        border-left: 4px solid #185FA5 !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: #185FA5 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        background: #0C447C !important;
        color: white !important;
    }

    /* ── Page titles ── */
    h1 { color: #0C447C !important; }
    h2, h3 { color: #185FA5 !important; }
    </style>
    """, unsafe_allow_html=True)

    # ── Sidebar logo & branding ── (now shows ABOVE nav)
    st.sidebar.markdown("""
    <div style='text-align:center; padding:24px 10px 16px 10px;'>
        <div style='font-size:52px; line-height:1;'>🛡️</div>
        <div style='color:white; font-size:18px; font-weight:600;
                    margin:10px 0 4px 0; letter-spacing:0.02em;'>
            RoadGuard Pakistan
        </div>
        <div style='color:#B5D4F4; font-size:11px; line-height:1.4;'>
            Data-driven road safety intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.divider()

    # ── Navigation label ──
    st.sidebar.markdown("""
    <div style='color:#B5D4F4; font-size:10px; font-weight:600;
                letter-spacing:0.1em; text-transform:uppercase;
                padding: 0 4px 6px 4px;'>
        Navigation
    </div>
    """, unsafe_allow_html=True)

    # ── Navigation links ──
    nav_pages = [
        ("📊", "Overview",                "overview"),
        ("🗺️", "Accident Map",            "map"),
        ("📈", "EDA & Trends",            "eda"),
        ("🏙️", "Province Comparison",     "provinces"),
        ("🤖", "ML Predictions",          "predict"),
        ("📋", "Policy Insights",         "policy"),
        ("🌍", "International Benchmark", "benchmarking"),
        ("🧮", "Risk Calculator",         "calculator"),
        ("📋", "Province Scorecard",      "scorecard"),
        ("⚠️", "Dangerous Roads",         "dangerous_roads"),
        ("👤", "About",                   "about"),
    ]

    for icon, label, page in nav_pages:
        st.sidebar.markdown(f"""
        <a href='/{page}' target='_self' style='text-decoration:none;'>
        <div style='padding:7px 12px; border-radius:7px; margin-bottom:3px;
                    display:block;'>
            <span style='color:white !important; font-size:15px;'>
                {icon}&nbsp;&nbsp;{label}
            </span>
        </div>
        </a>
        """, unsafe_allow_html=True)

    st.sidebar.divider()

    # ── Footer ──
    st.sidebar.markdown("""
    <div style='text-align:center; padding:8px 0;'>
        <div style='color:#B5D4F4; font-size:11px; line-height:1.8;'>
            BS Data Science · 2026<br>
            🇵🇰 Pakistan
        </div>
    </div>
    """, unsafe_allow_html=True)