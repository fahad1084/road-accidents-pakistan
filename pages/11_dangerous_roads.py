import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium
import sys
sys.path.append('.')
from utils.styles import apply_sidebar

NAVY = '#0C447C'
BLUE = '#185FA5'
SKY = '#378ADD'
RED = '#E24B4A'
DEEP_RED = '#A32D2D'
OFF_WHITE = '#F1EFE8'

st.set_page_config(page_title="Dangerous Roads | RoadGuard Pakistan",
                   page_icon="⚠️", layout="wide")
apply_sidebar()

st.title("⚠️ Most Dangerous Roads in Pakistan")
st.markdown("#### Top accident-prone highways and roads across Pakistan")
st.divider()

# ── Data — based on NHMP & media reports ──
df_roads = pd.DataFrame({
    'Rank': range(1, 11),
    'Road': [
        'N-5 (Grand Trunk Road)',
        'M-2 (Lahore-Islamabad Motorway)',
        'N-55 (Indus Highway)',
        'N-25 (Quetta-Karachi)',
        'N-35 (Karakoram Highway)',
        'N-10 (Makran Coastal Highway)',
        'N-45 (Dir Road, KPK)',
        'N-70 (Multan-D.G. Khan)',
        'N-15 (Mansehra-Naran)',
        'N-65 (Sukkur-Jacobabad)'
    ],
    'Province': [
        'Punjab/KPK', 'Punjab', 'KPK/Sindh',
        'Balochistan', 'KPK/GB', 'Balochistan',
        'KPK', 'Punjab', 'KPK', 'Sindh'
    ],
    'Avg_Annual_Accidents': [
        1850, 420, 980, 760, 540,
        380, 620, 490, 410, 520
    ],
    'Avg_Annual_Fatalities': [
        920, 180, 510, 420, 310,
        220, 340, 260, 230, 280
    ],
    'Length_km': [
        1819, 367, 1264, 693, 1300,
        653, 287, 456, 165, 342
    ],
    'Risk_Level': [
        'Very High', 'Medium', 'High', 'High', 'High',
        'Medium', 'High', 'Medium', 'High', 'High'
    ],
    'lat': [
        31.5497, 32.5, 30.5, 27.5, 35.5,
        25.5, 34.8, 29.8, 34.9, 27.8
    ],
    'lon': [
        74.3436, 72.8, 68.5, 66.5, 73.0,
        62.5, 71.9, 70.3, 73.4, 68.5
    ],
    'Main_Cause': [
        'Overspeeding, Overtaking',
        'High speed, Fatigue',
        'Poor road condition',
        'Poor visibility, Wildlife',
        'Landslides, Sharp turns',
        'Remote location, Speed',
        'Mountain terrain',
        'Heavy trucks, Fog',
        'Steep terrain, Weather',
        'Poor road condition'
    ]
})

# ── KPI Cards ──
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🛣️ Roads Analysed", "10")
with col2:
    st.metric("💀 Total Annual Fatalities",
              f"{df_roads['Avg_Annual_Fatalities'].sum():,}")
with col3:
    st.metric("🚗 Total Annual Accidents",
              f"{df_roads['Avg_Annual_Accidents'].sum():,}")
with col4:
    st.metric("⚠️ Most Dangerous Road",
              df_roads.iloc[0]['Road'].split('(')[0].strip())

st.divider()

# ── Map ──
st.subheader("🗺️ Dangerous Roads Map")
m = folium.Map(location=[30.3753, 69.3451], zoom_start=5,
               tiles='CartoDB positron')

for _, row in df_roads.iterrows():
    color = '#E24B4A' if row['Risk_Level'] == 'Very High' else \
            '#E07B39' if row['Risk_Level'] == 'High' else '#185FA5'
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=max(8, row['Avg_Annual_Fatalities'] / 80),
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=folium.Popup(f"""
            <b>#{row['Rank']} {row['Road']}</b><br>
            Province: {row['Province']}<br>
            Annual Accidents: {row['Avg_Annual_Accidents']:,}<br>
            Annual Fatalities: {row['Avg_Annual_Fatalities']:,}<br>
            Risk Level: {row['Risk_Level']}<br>
            Main Cause: {row['Main_Cause']}
        """, max_width=250),
        tooltip=f"#{row['Rank']} {row['Road']}"
    ).add_to(m)

st_folium(m, width=1200, height=450)

st.divider()

# ── Charts ──
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("Annual Fatalities by Road")
    df_sorted = df_roads.sort_values('Avg_Annual_Fatalities', ascending=True)
    colors = [RED if r == 'Very High' else
              '#E07B39' if r == 'High' else BLUE
              for r in df_sorted['Risk_Level']]
    fig1 = go.Figure(go.Bar(
        x=df_sorted['Avg_Annual_Fatalities'],
        y=df_sorted['Road'].str.split('(').str[0],
        orientation='h',
        marker_color=colors,
        text=df_sorted['Avg_Annual_Fatalities'],
        textposition='outside'
    ))
    fig1.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Average Annual Fatalities',
                       height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col_r:
    st.subheader("Fatalities per 100km of Road")
    df_roads['Fatalities_per_100km'] = (
        df_roads['Avg_Annual_Fatalities'] /
        df_roads['Length_km'] * 100
    ).round(1)
    df_density = df_roads.sort_values(
        'Fatalities_per_100km', ascending=True)
    fig2 = go.Figure(go.Bar(
        x=df_density['Fatalities_per_100km'],
        y=df_density['Road'].str.split('(').str[0],
        orientation='h',
        marker_color=BLUE,
        text=df_density['Fatalities_per_100km'],
        textposition='outside'
    ))
    fig2.update_layout(plot_bgcolor=OFF_WHITE, paper_bgcolor='white',
                       xaxis_title='Fatalities per 100km',
                       height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── Full data table ──
st.subheader("📋 Complete Road Safety Data")
st.dataframe(
    df_roads[['Rank', 'Road', 'Province', 'Risk_Level',
              'Avg_Annual_Accidents', 'Avg_Annual_Fatalities',
              'Length_km', 'Fatalities_per_100km', 'Main_Cause']],
    use_container_width=True,
    hide_index=True
)

st.divider()
st.caption("Data based on NHMP reports and road safety research · RoadGuard Pakistan")