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

st.set_page_config(page_title="EDA | RoadGuard Pakistan",
                   page_icon="📈", layout="wide")
apply_sidebar()

st.title("📈 Exploratory Data Analysis")
st.markdown("#### 15 charts exploring Pakistan road accident patterns")
st.divider()

@st.cache_data
def load_data():
    df_main = pd.read_csv('data/cleaned/cleaned_main.csv')
    df_punjab = pd.read_csv('data/cleaned/cleaned_punjab.csv')
    return df_main, df_punjab

df_main, df_punjab = load_data()
df_provinces = df_main[df_main['Province'] != 'Pakistan (National)'].copy()
df_national_only = df_main[df_main['Province'] == 'Pakistan (National)'].copy()

# ── Download Data Popover ──
with st.popover("⬇️ Download Data"):
    st.markdown("**Choose dataset to download:**")
    
    csv_main = df_main.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Main Dataset (All Provinces 2006-2023)",
        data=csv_main,
        file_name="pakistan_accidents_main.csv",
        mime="text/csv",
        use_container_width=True
    )
    
    csv_provinces = df_provinces.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Province Level Data",
        data=csv_provinces,
        file_name="pakistan_accidents_provinces.csv",
        mime="text/csv",
        use_container_width=True
    )
    
    csv_punjab = df_punjab.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Punjab District Data",
        data=csv_punjab,
        file_name="pakistan_accidents_punjab.csv",
        mime="text/csv",
        use_container_width=True
    )

# Sidebar filters
st.sidebar.header("Filters")

# Year range filter
min_year = int(df_main['Year_Numeric'].min())
max_year = int(df_main['Year_Numeric'].max())
year_range = st.sidebar.slider(
    "📅 Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

selected_province = st.sidebar.multiselect(
    "Select Provinces",
    options=df_provinces['Province'].unique().tolist(),
    default=df_provinces['Province'].unique().tolist()
)

# Apply both filters
df_filtered = df_provinces[
    (df_provinces['Province'].isin(selected_province)) &
    (df_provinces['Year_Numeric'] >= year_range[0]) &
    (df_provinces['Year_Numeric'] <= year_range[1])
]

df_national_only = df_national_only[
    (df_national_only['Year_Numeric'] >= year_range[0]) &
    (df_national_only['Year_Numeric'] <= year_range[1])
]

# Chart 1 & 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("01 — Accident Trend Over Years")
    df_trend = df_national_only.sort_values('Year_Numeric')
    fig = px.line(df_trend, x='Year_Numeric', y='Total_Accidents',
                  markers=True, color_discrete_sequence=[BLUE])
    fig.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                      xaxis_title='Year', yaxis_title='Total Accidents')
    fig.update_traces(line=dict(width=3), marker=dict(size=8, color=RED))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("02 — Total Accidents by Province")
    df_prov = df_filtered.groupby('Province')['Total_Accidents'].sum().reset_index()
    df_prov = df_prov.sort_values('Total_Accidents', ascending=True)
    fig2 = px.bar(df_prov, x='Total_Accidents', y='Province', orientation='h',
                  color='Total_Accidents',
                  color_continuous_scale=[[0, SKY], [0.5, BLUE], [1, NAVY]])
    fig2.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

# Chart 3 & 4
col3, col4 = st.columns(2)

with col3:
    st.subheader("03 — Fatalities by Province")
    df_killed = df_filtered.groupby('Province')['Killed'].sum().reset_index()
    df_killed = df_killed.sort_values('Killed', ascending=True)
    fig3 = px.bar(df_killed, x='Killed', y='Province', orientation='h',
                  color='Killed',
                  color_continuous_scale=[[0, '#FCEBEB'], [0.5, RED], [1, DEEP_RED]])
    fig3.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       coloraxis_showscale=False)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("04 — Severity Index by Province")
    df_sev = df_filtered.groupby('Province')['Severity_Index'].mean().reset_index()
    df_sev = df_sev.sort_values('Severity_Index', ascending=True)
    fig4 = px.bar(df_sev, x='Severity_Index', y='Province', orientation='h',
                  color='Severity_Index',
                  color_continuous_scale=[[0, SKY], [0.5, RED], [1, DEEP_RED]])
    fig4.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       coloraxis_showscale=False)
    st.plotly_chart(fig4, use_container_width=True)

# Chart 5 & 6
col5, col6 = st.columns(2)

with col5:
    st.subheader("05 — Fatality Rate Trend")
    df_fat = df_national_only.sort_values('Year_Numeric')
    fig5 = px.line(df_fat, x='Year_Numeric', y='Fatality_Rate',
                   markers=True, color_discrete_sequence=[RED])
    fig5.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Year', yaxis_title='Fatality Rate')
    fig5.update_traces(line=dict(width=3), marker=dict(size=8, color=NAVY))
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader("06 — Severity Distribution")
    df_pie = df_filtered['Severity_Label'].value_counts().reset_index()
    df_pie.columns = ['Severity_Label', 'Count']
    fig6 = px.pie(df_pie, names='Severity_Label', values='Count', hole=0.4,
                  color='Severity_Label',
                  color_discrete_map={'Low': SKY, 'Medium': BLUE, 'High': RED})
    fig6.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig6, use_container_width=True)

# Chart 7 & 8
col7, col8 = st.columns(2)

with col7:
    st.subheader("07 — Vehicles Involved Trend")
    df_veh = df_national_only.sort_values('Year_Numeric')
    fig7 = px.area(df_veh, x='Year_Numeric', y='Total_Vehicles_Involved',
                   color_discrete_sequence=[BLUE])
    fig7.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white')
    fig7.update_traces(line=dict(width=2, color=NAVY),
                       fillcolor='rgba(24, 95, 165, 0.2)')
    st.plotly_chart(fig7, use_container_width=True)

with col8:
    st.subheader("08 — Killed vs Injured by Province")
    df_ki = df_filtered.groupby('Province')[['Killed', 'Injured']].sum().reset_index()
    fig8 = go.Figure()
    fig8.add_trace(go.Bar(name='Killed', x=df_ki['Province'],
                          y=df_ki['Killed'], marker_color=RED))
    fig8.add_trace(go.Bar(name='Injured', x=df_ki['Province'],
                          y=df_ki['Injured'], marker_color=BLUE))
    fig8.update_layout(barmode='group', plot_bgcolor=OFF_WHITE,
                       paper_bgcolor='white')
    st.plotly_chart(fig8, use_container_width=True)

# Chart 9 — Correlation Heatmap (full width)
st.subheader("09 — Correlation Heatmap")
numeric_cols = ['Total_Accidents', 'Fatal_Accidents', 'Non_Fatal_Accidents',
                'Killed', 'Injured', 'Total_Vehicles_Involved',
                'Fatality_Rate', 'Severity_Index']
corr = df_filtered[numeric_cols].corr().round(2)
fig9 = px.imshow(corr, color_continuous_scale=[[0, OFF_WHITE], [0.5, BLUE], [1, NAVY]],
                 zmin=-1, zmax=1, text_auto=True, aspect='auto')
fig9.update_layout(paper_bgcolor='white', width=900, height=500)
st.plotly_chart(fig9, use_container_width=True)

# Chart 10 & 11
col10, col11 = st.columns(2)

with col10:
    st.subheader("10 — Fatal vs Non-Fatal Trend")
    df_fn = df_national_only.sort_values('Year_Numeric')
    fig10 = go.Figure()
    fig10.add_trace(go.Scatter(x=df_fn['Year_Numeric'], y=df_fn['Fatal_Accidents'],
                               name='Fatal', mode='lines+markers',
                               line=dict(width=3, color=RED), fill='tozeroy',
                               fillcolor='rgba(226, 75, 74, 0.2)'))
    fig10.add_trace(go.Scatter(x=df_fn['Year_Numeric'], y=df_fn['Non_Fatal_Accidents'],
                               name='Non-Fatal', mode='lines+markers',
                               line=dict(width=3, color=BLUE), fill='tozeroy',
                               fillcolor='rgba(24, 95, 165, 0.2)'))
    fig10.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white')
    st.plotly_chart(fig10, use_container_width=True)

with col11:
    st.subheader("11 — Injury Rate by Province")
    df_inj = df_filtered.groupby('Province')['Injury_Rate'].mean().reset_index()
    df_inj = df_inj.sort_values('Injury_Rate', ascending=True)
    fig11 = px.bar(df_inj, x='Injury_Rate', y='Province', orientation='h',
                   color='Injury_Rate',
                   color_continuous_scale=[[0, SKY], [0.5, BLUE], [1, NAVY]])
    fig11.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                        coloraxis_showscale=False)
    st.plotly_chart(fig11, use_container_width=True)

# Chart 12 & 13
col12, col13 = st.columns(2)

with col12:
    st.subheader("12 — Vehicles Per Accident by Province")
    df_vpa = df_filtered.groupby('Province')['Vehicles_Per_Accident'].mean().reset_index()
    df_vpa = df_vpa.sort_values('Vehicles_Per_Accident', ascending=True)
    fig12 = px.bar(df_vpa, x='Vehicles_Per_Accident', y='Province', orientation='h',
                   color='Vehicles_Per_Accident',
                   color_continuous_scale=[[0, SKY], [0.5, BLUE], [1, NAVY]])
    fig12.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                        coloraxis_showscale=False)
    st.plotly_chart(fig12, use_container_width=True)

with col13:
    st.subheader("13 — Top 15 Punjab Districts")
    df_pjb = df_punjab.sort_values('Road_Accidents', ascending=True).tail(15)
    fig13 = px.bar(df_pjb, x='Road_Accidents', y='District', orientation='h',
                   color='Severity_Label',
                   color_discrete_map={'Low': SKY, 'Medium': BLUE, 'High': RED},
                   height=500)
    fig13.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white')
    st.plotly_chart(fig13, use_container_width=True)

# Chart 14 & 15
col14, col15 = st.columns(2)

with col14:
    st.subheader("14 — Top 15 Districts by Accident %")
    df_pct = df_punjab.sort_values('Road_Accident_Pct', ascending=True).tail(15)
    fig14 = px.bar(df_pct, x='Road_Accident_Pct', y='District', orientation='h',
                   color='Road_Accident_Pct',
                   color_continuous_scale=[[0, SKY], [0.5, BLUE], [1, NAVY]],
                   height=500)
    fig14.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                        coloraxis_showscale=False)
    st.plotly_chart(fig14, use_container_width=True)

with col15:
    st.subheader("15 — Killed Per Fatal Accident")
    df_kpf = df_filtered.groupby('Province')['Killed_Per_Fatal_Acc'].mean().reset_index()
    df_kpf = df_kpf.sort_values('Killed_Per_Fatal_Acc', ascending=True)
    fig15 = px.bar(df_kpf, x='Killed_Per_Fatal_Acc', y='Province', orientation='h',
                   color='Killed_Per_Fatal_Acc',
                   color_continuous_scale=[[0, '#FCEBEB'], [0.5, RED], [1, DEEP_RED]])
    fig15.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                        coloraxis_showscale=False)
    st.plotly_chart(fig15, use_container_width=True)

st.divider()
st.caption("All charts built with Plotly · RoadGuard Pakistan")