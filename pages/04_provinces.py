import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
sys.path.append('.')
from utils.styles import apply_sidebar
# Brand colours
NAVY = '#0C447C'
BLUE = '#185FA5'
SKY = '#378ADD'
RED = '#E24B4A'
DEEP_RED = '#A32D2D'
OFF_WHITE = '#F1EFE8'

st.set_page_config(page_title="Provinces | RoadGuard Pakistan",
                   page_icon="🏙️", layout="wide")
apply_sidebar()

st.title("🏙️ Province Comparison")
st.markdown("#### Side-by-side road safety analysis across Pakistan's provinces")
st.divider()

@st.cache_data
def load_data():
    df_main = pd.read_csv('data/cleaned/cleaned_main.csv')
    return df_main

df_main = load_data()
df_provinces = df_main[df_main['Province'] != 'Pakistan (National)'].copy()

# Sidebar — Province selector
st.sidebar.header("Select Provinces")
all_provinces = df_provinces['Province'].unique().tolist()
selected = st.sidebar.multiselect(
    "Compare Provinces",
    options=all_provinces,
    default=all_provinces
)

df_filtered = df_provinces[df_provinces['Province'].isin(selected)]

# Summary table
st.subheader("📋 Province Summary Table")
df_summary = df_filtered.groupby('Province').agg(
    Total_Accidents=('Total_Accidents', 'sum'),
    Total_Killed=('Killed', 'sum'),
    Total_Injured=('Injured', 'sum'),
    Avg_Severity_Index=('Severity_Index', 'mean'),
    Avg_Fatality_Rate=('Fatality_Rate', 'mean'),
    Years_Covered=('Year_Numeric', 'nunique')
).reset_index().round(2)

st.dataframe(df_summary, use_container_width=True, hide_index=True)
st.divider()

# Row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("Total Accidents by Province")
    df_acc = df_filtered.groupby('Province')['Total_Accidents'].sum().reset_index()
    df_acc = df_acc.sort_values('Total_Accidents', ascending=True)
    fig1 = px.bar(df_acc, x='Total_Accidents', y='Province', orientation='h',
                  color='Total_Accidents',
                  color_continuous_scale=[[0, SKY], [0.5, BLUE], [1, NAVY]])
    fig1.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       coloraxis_showscale=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Total Killed by Province")
    df_kil = df_filtered.groupby('Province')['Killed'].sum().reset_index()
    df_kil = df_kil.sort_values('Killed', ascending=True)
    fig2 = px.bar(df_kil, x='Killed', y='Province', orientation='h',
                  color='Killed',
                  color_continuous_scale=[[0, '#FCEBEB'], [0.5, RED], [1, DEEP_RED]])
    fig2.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

# Row 2
col3, col4 = st.columns(2)

with col3:
    st.subheader("Severity Index Over Years")
    df_sev_yr = df_filtered.groupby(['Year_Numeric', 'Province'])['Severity_Index'].mean().reset_index()
    fig3 = px.line(df_sev_yr, x='Year_Numeric', y='Severity_Index',
                   color='Province', markers=True)
    fig3.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Year', yaxis_title='Severity Index')
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Fatality Rate Over Years")
    df_fat_yr = df_filtered.groupby(['Year_Numeric', 'Province'])['Fatality_Rate'].mean().reset_index()
    fig4 = px.line(df_fat_yr, x='Year_Numeric', y='Fatality_Rate',
                   color='Province', markers=True)
    fig4.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Year', yaxis_title='Fatality Rate')
    st.plotly_chart(fig4, use_container_width=True)

# Row 3 — Radar chart
st.subheader("Province Comparison Radar Chart")
df_radar = df_filtered.groupby('Province').agg(
    Accidents=('Total_Accidents', 'sum'),
    Killed=('Killed', 'sum'),
    Injured=('Injured', 'sum'),
    Severity=('Severity_Index', 'mean'),
    Fatality_Rate=('Fatality_Rate', 'mean')
).reset_index()

# Normalise 0-1
for col in ['Accidents', 'Killed', 'Injured', 'Severity', 'Fatality_Rate']:
    df_radar[col] = (df_radar[col] - df_radar[col].min()) / (
        df_radar[col].max() - df_radar[col].min() + 1e-9)

categories = ['Accidents', 'Killed', 'Injured', 'Severity', 'Fatality_Rate']
fig5 = go.Figure()
for _, row in df_radar.iterrows():
    fig5.add_trace(go.Scatterpolar(
        r=[row[c] for c in categories] + [row[categories[0]]],
        theta=categories + [categories[0]],
        fill='toself',
        name=row['Province']
    ))

fig5.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
    paper_bgcolor='white',
    showlegend=True
)
st.plotly_chart(fig5, use_container_width=True)

st.divider()
st.caption("Province data from NTRC & PBS · RoadGuard Pakistan")