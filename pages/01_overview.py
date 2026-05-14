import streamlit as st
import pandas as pd
import plotly.express as px
import sys
sys.path.append('.')
from utils.styles import apply_sidebar
# Brand colours
NAVY = '#0C447C'
BLUE = '#185FA5'
RED = '#E24B4A'
OFF_WHITE = '#F1EFE8'

st.set_page_config(page_title="Overview | RoadGuard Pakistan", 
                   page_icon="📊", layout="wide")
apply_sidebar()

st.title("📊 Overview")
st.markdown("#### Key Performance Indicators — Pakistan Road Safety")
st.divider()

# Load data
@st.cache_data
def load_data():
    df_main = pd.read_csv('data/cleaned/cleaned_main.csv')
    df_national = pd.read_csv('data/cleaned/cleaned_national.csv')
    df_punjab = pd.read_csv('data/cleaned/cleaned_punjab.csv')
    return df_main, df_national, df_punjab

df_main, df_national, df_punjab = load_data()
df_national_only = df_main[df_main['Province'] == 'Pakistan (National)'].copy()
df_provinces = df_main[df_main['Province'] != 'Pakistan (National)'].copy()

# KPI Cards
total_accidents = int(df_national_only['Total_Accidents'].sum())
total_killed = int(df_national_only['Killed'].sum())
total_injured = int(df_national_only['Injured'].sum())
worst_province = df_provinces.groupby('Province')['Killed'].sum().idxmax()
avg_severity = df_provinces['Severity_Index'].mean()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🚗 Total Accidents", f"{total_accidents:,}")
with col2:
    st.metric("💀 Total Killed", f"{total_killed:,}")
with col3:
    st.metric("🏥 Total Injured", f"{total_injured:,}")
with col4:
    st.metric("⚠️ Worst Province", worst_province)
with col5:
    st.metric("📊 Avg Severity Index", f"{avg_severity:.2f}")

st.divider()

# Two column layout
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Accident Trend Over Years")
    df_trend = df_national_only.sort_values('Year_Numeric')
    fig = px.line(df_trend, x='Year_Numeric', y='Total_Accidents',
                  markers=True, color_discrete_sequence=[BLUE])
    fig.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                      xaxis_title='Year', yaxis_title='Total Accidents')
    fig.update_traces(line=dict(width=3), marker=dict(size=8, color=RED))
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("Fatalities by Province")
    df_killed = df_provinces.groupby('Province')['Killed'].sum().reset_index()
    df_killed = df_killed.sort_values('Killed', ascending=True)
    fig2 = px.bar(df_killed, x='Killed', y='Province', orientation='h',
                  color='Killed',
                  color_continuous_scale=[[0, '#FCEBEB'], [0.5, RED], [1, '#A32D2D']])
    fig2.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Severity distribution
st.subheader("Severity Label Distribution Across Provinces")
df_sev = df_provinces['Severity_Label'].value_counts().reset_index()
df_sev.columns = ['Severity_Label', 'Count']
fig3 = px.pie(df_sev, names='Severity_Label', values='Count', hole=0.4,
              color='Severity_Label',
              color_discrete_map={'Low': '#378ADD', 'Medium': BLUE, 'High': RED})
fig3.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig3, use_container_width=True)