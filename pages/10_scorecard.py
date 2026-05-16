import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
sys.path.append('.')
from utils.styles import apply_sidebar

NAVY = '#0C447C'
BLUE = '#185FA5'
SKY = '#378ADD'
RED = '#E24B4A'
DEEP_RED = '#A32D2D'
OFF_WHITE = '#F1EFE8'

st.set_page_config(page_title="Province Scorecard | RoadGuard Pakistan",
                   page_icon="📋", layout="wide")

apply_sidebar()

st.title("📋 Province Scorecard")
st.markdown("#### Detailed road safety scorecard for each province")
st.divider()

@st.cache_data
def load_data():
    df_main = pd.read_csv('data/cleaned/cleaned_main.csv')
    return df_main

df_main = load_data()
df_provinces = df_main[df_main['Province'] != 'Pakistan (National)'].copy()

# ── Province selector ──
selected = st.selectbox(
    "🏙️ Select Province",
    options=df_provinces['Province'].unique().tolist()
)

df_prov = df_provinces[df_provinces['Province'] == selected].copy()
df_prov = df_prov.sort_values('Year_Numeric')

# ── KPI Cards ──
st.divider()
total_acc = int(df_prov['Total_Accidents'].sum())
total_killed = int(df_prov['Killed'].sum())
total_injured = int(df_prov['Injured'].sum())
avg_severity = df_prov['Severity_Index'].mean()
avg_fatality = df_prov['Fatality_Rate'].mean()
worst_year = df_prov.loc[df_prov['Killed'].idxmax(), 'Year_Numeric']
best_year = df_prov.loc[df_prov['Killed'].idxmin(), 'Year_Numeric']

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🚗 Total Accidents", f"{total_acc:,}")
with col2:
    st.metric("💀 Total Killed", f"{total_killed:,}")
with col3:
    st.metric("🏥 Total Injured", f"{total_injured:,}")
with col4:
    st.metric("📊 Avg Severity Index", f"{avg_severity:.2f}")

col5, col6, col7, col8 = st.columns(4)
with col5:
    st.metric("📉 Avg Fatality Rate", f"{avg_fatality:.1f}")
with col6:
    st.metric("📅 Years of Data", f"{len(df_prov)}")
with col7:
    st.metric("⚠️ Worst Year", f"{worst_year}")
with col8:
    st.metric("✅ Best Year", f"{best_year}")

st.divider()

# ── Safety Grade ──
if avg_severity < 2.0:
    grade, grade_color, grade_text = "A", SKY, "Good"
elif avg_severity < 2.3:
    grade, grade_color, grade_text = "B", BLUE, "Average"
elif avg_severity < 2.6:
    grade, grade_color, grade_text = "C", '#C9A800', "Below Average"
else:
    grade, grade_color, grade_text = "D", RED, "Poor"

col_grade, col_trend = st.columns([1, 3])

with col_grade:
    st.markdown(f"""
    <div style='background:{grade_color}; padding:30px; border-radius:16px;
                text-align:center;'>
        <div style='font-size:72px; font-weight:700; color:white;
                    line-height:1;'>{grade}</div>
        <div style='color:white; font-size:16px; margin-top:8px;'>
            Safety Grade
        </div>
        <div style='color:rgba(255,255,255,0.8); font-size:13px;
                    margin-top:4px;'>{grade_text}</div>
    </div>
    """, unsafe_allow_html=True)

with col_trend:
    st.subheader(f"Accident Trend — {selected}")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df_prov['Year_Numeric'], y=df_prov['Total_Accidents'],
        name='Total Accidents', mode='lines+markers',
        line=dict(width=3, color=BLUE), marker=dict(size=8)
    ))
    fig1.add_trace(go.Scatter(
        x=df_prov['Year_Numeric'], y=df_prov['Killed'],
        name='Killed', mode='lines+markers',
        line=dict(width=3, color=RED), marker=dict(size=8)
    ))
    fig1.update_layout(
        plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
        xaxis_title='Year', yaxis_title='Count',
        hovermode='x unified'
    )
    st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ── vs National Average ──
st.subheader("📊 Province vs National Average")
df_national = df_main[df_main['Province'] == 'Pakistan (National)'].copy()

nat_avg_accidents = df_national['Total_Accidents'].mean()
nat_avg_killed = df_national['Killed'].mean()
nat_avg_severity = df_national['Severity_Index'].mean()

col_n1, col_n2, col_n3 = st.columns(3)

with col_n1:
    diff_acc = ((df_prov['Total_Accidents'].mean() - nat_avg_accidents) 
                / nat_avg_accidents * 100)
    st.metric(
        "Avg Annual Accidents vs National",
        f"{int(df_prov['Total_Accidents'].mean()):,}",
        delta=f"{diff_acc:+.1f}% vs national avg",
        delta_color="inverse"
    )

with col_n2:
    diff_killed = ((df_prov['Killed'].mean() - nat_avg_killed) 
                   / nat_avg_killed * 100)
    st.metric(
        "Avg Annual Killed vs National",
        f"{int(df_prov['Killed'].mean()):,}",
        delta=f"{diff_killed:+.1f}% vs national avg",
        delta_color="inverse"
    )

with col_n3:
    diff_sev = ((df_prov['Severity_Index'].mean() - nat_avg_severity) 
                / nat_avg_severity * 100)
    st.metric(
        "Avg Severity vs National",
        f"{df_prov['Severity_Index'].mean():.2f}",
        delta=f"{diff_sev:+.1f}% vs national avg",
        delta_color="inverse"
    )

st.divider()
# ── Row 2 ──
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("Severity Index Over Years")
    fig2 = px.area(df_prov, x='Year_Numeric', y='Severity_Index',
                   color_discrete_sequence=[BLUE])
    fig2.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Year', yaxis_title='Severity Index')
    fig2.update_traces(line=dict(width=2, color=NAVY),
                       fillcolor='rgba(24, 95, 165, 0.2)')
    avg_line = df_prov['Severity_Index'].mean()
    fig2.add_hline(y=avg_line, line_dash='dash', line_color=RED,
                   annotation_text=f'Avg: {avg_line:.2f}')
    st.plotly_chart(fig2, use_container_width=True)

with col_r:
    st.subheader("Fatality Rate Over Years")
    fig3 = px.bar(df_prov, x='Year_Numeric', y='Fatality_Rate',
                  color='Fatality_Rate',
                  color_continuous_scale=[[0, SKY], [0.5, BLUE], [1, NAVY]])
    fig3.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Year', yaxis_title='Fatality Rate',
                       coloraxis_showscale=False)
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ── Year by year table ──
st.subheader(f"📋 Year-by-Year Data — {selected}")
display_cols = ['Year', 'Total_Accidents', 'Fatal_Accidents',
                'Killed', 'Injured', 'Severity_Index',
                'Fatality_Rate', 'Severity_Label']
st.dataframe(
    df_prov[display_cols].sort_values('Year', ascending=False),
    use_container_width=True,
    hide_index=True
)

st.divider()
st.caption(f"Data source: NTRC & PBS · {selected} Province · RoadGuard Pakistan")