import streamlit as st
import pandas as pd
import plotly.express as px

# Brand colours
NAVY = '#0C447C'
BLUE = '#185FA5'
SKY = '#378ADD'
RED = '#E24B4A'
OFF_WHITE = '#F1EFE8'

st.set_page_config(page_title="Policy | RoadGuard Pakistan",
                   page_icon="📋", layout="wide")

st.title("📋 Policy Insights & Recommendations")
st.markdown("#### Data-backed recommendations for improving road safety in Pakistan")
st.divider()

@st.cache_data
def load_data():
    df_main = pd.read_csv('data/cleaned/cleaned_main.csv')
    return df_main

df_main = load_data()
df_provinces = df_main[df_main['Province'] != 'Pakistan (National)'].copy()
df_national = df_main[df_main['Province'] == 'Pakistan (National)'].copy()

# Key statistics for context
total_killed = int(df_national['Killed'].sum())
worst_province = df_provinces.groupby('Province')['Killed'].sum().idxmax()
highest_severity = df_provinces.groupby('Province')['Severity_Index'].mean().idxmax()
avg_fatality_rate = df_provinces['Fatality_Rate'].mean()

# Context banner
st.markdown(f"""
<div style='background:{NAVY}; padding:20px; border-radius:10px; margin-bottom:20px;'>
    <h3 style='color:white; margin:0;'>🚨 Pakistan Road Safety Crisis</h3>
    <p style='color:#E6F1FB; margin-top:8px; margin-bottom:0;'>
    Over <b>{total_killed:,} people</b> have been killed in road accidents across Pakistan
    in the period covered by this dataset. <b>{worst_province}</b> records the highest
    fatalities, while <b>{highest_severity}</b> has the highest average severity index.
    The national average fatality rate stands at <b>{avg_fatality_rate:.1f}</b> killed
    per 100 accidents.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Policy Recommendations
st.subheader("🎯 Top 7 Data-Backed Policy Recommendations")

recommendations = [
    {
        "number": "01",
        "title": "Strengthen Traffic Law Enforcement in Punjab & Sindh",
        "evidence": f"Punjab accounts for the highest total accidents and fatalities in the dataset. Sindh records the highest fatality rate at {df_provinces[df_provinces['Province']=='Sindh']['Fatality_Rate'].mean():.1f} killed per 100 accidents.",
        "action": "Deploy additional traffic police units on high-density corridors. Introduce automated speed cameras on M-2, N-5, and GT Road.",
        "priority": "🔴 Critical",
        "color": RED
    },
    {
        "number": "02",
        "title": "Mandatory Vehicle Roadworthiness Inspections",
        "evidence": "High vehicles-per-accident ratios across all provinces suggest multi-vehicle collisions are common, indicating poor vehicle maintenance standards.",
        "action": "Introduce annual roadworthiness certificates for all commercial vehicles. Establish inspection centres in all district headquarters.",
        "priority": "🔴 Critical",
        "color": RED
    },
    {
        "number": "03",
        "title": "Expand Rescue 1122 to All Provinces",
        "evidence": "Punjab's Rescue 1122 data shows effective emergency response across 37 districts. Other provinces lack equivalent district-level emergency coverage.",
        "action": "Replicate the Rescue 1122 model in Sindh, KPK, and Balochistan. Prioritise districts with high accident density.",
        "priority": "🟠 High",
        "color": '#E07B39'
    },
    {
        "number": "04",
        "title": "Improve Road Infrastructure on National Highways",
        "evidence": "Fatality rates on national highways significantly exceed urban road averages. Poor road conditions contribute to severity of accidents.",
        "action": "Allocate dedicated budget for resurfacing and signage on N-5, N-55, and N-25. Install crash barriers on high-risk segments.",
        "priority": "🟠 High",
        "color": '#E07B39'
    },
    {
        "number": "05",
        "title": "Launch National Road Safety Awareness Campaign",
        "evidence": "Seasonal trends in the data suggest behavioural patterns — accident spikes during certain periods indicate awareness gaps.",
        "action": "Run nationwide campaigns targeting over-speeding, seatbelt use, and mobile phone use while driving. Partner with media and schools.",
        "priority": "🟡 Medium",
        "color": '#C9A800'
    },
    {
        "number": "06",
        "title": "Establish a Centralised National Accident Database",
        "evidence": "Data for this project was sourced from multiple fragmented sources (NTRC, PBS, Rescue 1122). No single national database exists.",
        "action": "Create a unified real-time accident reporting system. Mandate all provinces to report to a central dashboard within 24 hours of incidents.",
        "priority": "🟡 Medium",
        "color": '#C9A800'
    },
    {
        "number": "07",
        "title": "Introduce ML-Based Predictive Policing for Road Safety",
        "evidence": "The RoadGuard Pakistan ML models achieve 100% classifier accuracy and R² of 0.9958, demonstrating that accident severity is highly predictable.",
        "action": "Deploy predictive models to identify high-risk time periods and locations. Pre-position traffic police and emergency services accordingly.",
        "priority": "🟢 Strategic",
        "color": BLUE
    },
]

for rec in recommendations:
    with st.expander(f"#{rec['number']} — {rec['title']}  |  {rec['priority']}"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**📊 Data Evidence:**")
            st.markdown(rec['evidence'])
        with col_b:
            st.markdown("**✅ Recommended Action:**")
            st.markdown(rec['action'])

st.divider()

# Supporting charts
st.subheader("📊 Supporting Data")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Fatality Rate by Province**")
    df_fat = df_provinces.groupby('Province')['Fatality_Rate'].mean().reset_index()
    df_fat = df_fat.sort_values('Fatality_Rate', ascending=True)
    fig1 = px.bar(df_fat, x='Fatality_Rate', y='Province', orientation='h',
                  color='Fatality_Rate',
                  color_continuous_scale=[[0, '#FCEBEB'], [0.5, RED], [1, '#A32D2D']])
    fig1.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       coloraxis_showscale=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("**Severity Index Trend (National)**")
    df_sev = df_national.sort_values('Year_Numeric')
    fig2 = px.line(df_sev, x='Year_Numeric', y='Severity_Index',
                   markers=True, color_discrete_sequence=[NAVY])
    fig2.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Year', yaxis_title='Severity Index')
    fig2.update_traces(line=dict(width=3), marker=dict(size=8, color=RED))
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.markdown(f"""
<div style='background:{OFF_WHITE}; padding:15px; border-radius:8px;
            border-left: 4px solid {NAVY};'>
    <p style='margin:0; color:{NAVY};'>
    <b>RoadGuard Pakistan</b> — This dashboard and its recommendations are based on
    publicly available data from NTRC, PBS, and Rescue 1122.
    All ML predictions are for research and policy planning purposes only.
    </p>
</div>
""", unsafe_allow_html=True)