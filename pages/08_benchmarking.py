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

st.set_page_config(page_title="Benchmarking | RoadGuard Pakistan",
                   page_icon="🌍", layout="wide")
apply_sidebar()


st.title("🌍 International Benchmarking")
st.markdown("#### Pakistan road safety compared to regional and global standards")
st.divider()

# ── Data — WHO & World Bank road safety statistics ──
df_bench = pd.DataFrame({
    'Country': [
        'Pakistan', 'India', 'Bangladesh', 'Iran',
        'Turkey', 'Malaysia', 'Thailand', 'China',
        'UK', 'Germany', 'Australia', 'Global Average'
    ],
    'Region': [
        'South Asia', 'South Asia', 'South Asia', 'Middle East',
        'Middle East', 'Southeast Asia', 'Southeast Asia', 'East Asia',
        'Europe', 'Europe', 'Oceania', 'Global'
    ],
    'Fatality_Rate_Per_100k': [
        17.4, 16.6, 15.3, 20.5,
        12.0, 23.6, 32.7, 7.3,
        2.8, 3.7, 4.7, 18.2
    ],
    'Annual_Deaths': [
        25781, 153972, 25000, 20000,
        7541, 6915, 22491, 258000,
        1695, 2569, 1195, 1350000
    ],
    'Seatbelt_Law': [
        'Partial', 'Yes', 'Yes', 'Yes',
        'Yes', 'Yes', 'Yes', 'Yes',
        'Yes', 'Yes', 'Yes', '-'
    ],
    'Speed_Camera': [
        'Limited', 'Limited', 'No', 'Yes',
        'Yes', 'Yes', 'Yes', 'Yes',
        'Yes', 'Yes', 'Yes', '-'
    ],
    'Road_Safety_Score': [
        42, 45, 38, 40,
        58, 52, 35, 68,
        85, 88, 82, 50
    ]
})

# ── KPI Cards ──
pak = df_bench[df_bench['Country'] == 'Pakistan'].iloc[0]
global_avg = df_bench[df_bench['Country'] == 'Global Average'].iloc[0]
best = df_bench[df_bench['Fatality_Rate_Per_100k'] == df_bench['Fatality_Rate_Per_100k'].min()].iloc[0]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🇵🇰 Pakistan Fatality Rate",
              f"{pak['Fatality_Rate_Per_100k']} per 100k",
              delta=f"{pak['Fatality_Rate_Per_100k'] - global_avg['Fatality_Rate_Per_100k']:.1f} vs global avg",
              delta_color="inverse")
with col2:
    st.metric("🌍 Global Average",
              f"{global_avg['Fatality_Rate_Per_100k']} per 100k")
with col3:
    st.metric("🏆 Best Performer",
              f"{best['Country']}",
              f"{best['Fatality_Rate_Per_100k']} per 100k")
with col4:
    st.metric("📊 Pakistan Safety Score",
              f"{int(pak['Road_Safety_Score'])}/100",
              delta=f"{int(pak['Road_Safety_Score']) - 50} vs global avg",
              delta_color="inverse")

st.divider()

# ── Row 1 ──
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("Fatality Rate per 100,000 Population")
    df_sorted = df_bench[df_bench['Country'] != 'Global Average'].sort_values(
        'Fatality_Rate_Per_100k', ascending=True)
    colors = [RED if c == 'Pakistan' else
              BLUE if r == 'South Asia' else SKY
              for c, r in zip(df_sorted['Country'], df_sorted['Region'])]
    fig1 = go.Figure(go.Bar(
        x=df_sorted['Fatality_Rate_Per_100k'],
        y=df_sorted['Country'],
        orientation='h',
        marker_color=colors,
        text=df_sorted['Fatality_Rate_Per_100k'],
        textposition='outside'
    ))
    fig1.add_vline(x=global_avg['Fatality_Rate_Per_100k'],
                   line_dash='dash', line_color=NAVY,
                   annotation_text='Global Avg',
                   annotation_position='top right')
    fig1.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Deaths per 100,000 population',
                       height=450)
    st.plotly_chart(fig1, use_container_width=True)

with col_r:
    st.subheader("Road Safety Score by Country")
    df_score = df_bench[df_bench['Country'] != 'Global Average'].sort_values(
        'Road_Safety_Score', ascending=True)
    colors2 = [RED if c == 'Pakistan' else BLUE
               for c in df_score['Country']]
    fig2 = go.Figure(go.Bar(
        x=df_score['Road_Safety_Score'],
        y=df_score['Country'],
        orientation='h',
        marker_color=colors2,
        text=df_score['Road_Safety_Score'],
        textposition='outside'
    ))
    fig2.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Safety Score (0-100)',
                       xaxis=dict(range=[0, 100]),
                       height=450)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── Row 2 ──
col_l2, col_r2 = st.columns(2)

with col_l2:
    st.subheader("Regional Comparison — South Asia Focus")
    df_south_asia = df_bench[df_bench['Region'].isin(
        ['South Asia', 'Global'])].copy()
    fig3 = px.bar(df_south_asia, x='Country',
                  y='Fatality_Rate_Per_100k',
                  color='Country',
                  color_discrete_map={
                      'Pakistan': RED,
                      'India': BLUE,
                      'Bangladesh': SKY,
                      'Global Average': NAVY
                  },
                  text='Fatality_Rate_Per_100k')
    fig3.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       yaxis_title='Deaths per 100,000',
                       showlegend=False)
    fig3.update_traces(textposition='outside')
    st.plotly_chart(fig3, use_container_width=True)

with col_r2:
    st.subheader("Road Safety Measures Comparison")
    df_measures = df_bench[df_bench['Country'] != 'Global Average'][
        ['Country', 'Seatbelt_Law', 'Speed_Camera']].copy()
    
    # Convert to numeric for heatmap
    df_measures['Seatbelt'] = df_measures['Seatbelt_Law'].map(
        {'Yes': 2, 'Partial': 1, 'No': 0})
    df_measures['Speed Camera'] = df_measures['Speed_Camera'].map(
        {'Yes': 2, 'Limited': 1, 'No': 0})
    
    fig4 = px.imshow(
        df_measures[['Seatbelt', 'Speed Camera']].set_index(df_measures['Country']).T,
        color_continuous_scale=[[0, '#FCEBEB'], [0.5, SKY], [1, NAVY]],
        text_auto=False,
        aspect='auto'
    )
    fig4.update_layout(paper_bgcolor='white',
                       xaxis_title='Country',
                       yaxis_title='Safety Measure',
                       coloraxis_showscale=False)
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ── Radar chart ──
st.subheader("🕸️ Multi-Country Safety Radar")
selected_countries = st.multiselect(
    "Select countries to compare",
    options=df_bench[df_bench['Country'] != 'Global Average']['Country'].tolist(),
    default=['Pakistan', 'India', 'Bangladesh', 'UK', 'Malaysia']
)

df_radar = df_bench[df_bench['Country'].isin(selected_countries)].copy()

# Normalise metrics 0-100
df_radar['Safety_Norm'] = df_radar['Road_Safety_Score']
df_radar['Fatality_Inv'] = 100 - (
    df_radar['Fatality_Rate_Per_100k'] /
    df_radar['Fatality_Rate_Per_100k'].max() * 100)

categories = ['Safety Score', 'Low Fatality Rate']

fig5 = go.Figure()
for _, row in df_radar.iterrows():
    fig5.add_trace(go.Scatterpolar(
        r=[row['Safety_Norm'], row['Fatality_Inv'],
           row['Safety_Norm'], row['Fatality_Inv']],
        theta=categories + categories,
        fill='toself',
        name=row['Country']
    ))

fig5.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    paper_bgcolor='white',
    showlegend=True,
    height=450
)
st.plotly_chart(fig5, use_container_width=True)

st.divider()

# ── Data table ──
st.subheader("📋 Full Comparison Table")
st.dataframe(
    df_bench.style.highlight_max(
        subset=['Road_Safety_Score'], color='#E6F1FB'
    ).highlight_min(
        subset=['Fatality_Rate_Per_100k'], color='#E6F1FB'
    ),
    use_container_width=True,
    hide_index=True
)

st.divider()
st.caption("Data sources: WHO Global Status Report on Road Safety 2023 · World Bank · RoadGuard Pakistan")