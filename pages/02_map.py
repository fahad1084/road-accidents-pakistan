import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap
import sys
sys.path.append('.')
from utils.styles import apply_sidebar
# Brand colours
NAVY = '#0C447C'
BLUE = '#185FA5'
RED = '#E24B4A'
SKY = '#378ADD'
DEEP_RED = '#A32D2D'

st.set_page_config(page_title="Map | RoadGuard Pakistan",
                   page_icon="🗺️", layout="wide")
apply_sidebar()

st.title("🗺️ Accident Hotspot Maps")
st.markdown("#### Interactive geospatial analysis of road accidents across Pakistan")
st.divider()

# Sidebar filters
st.sidebar.header("Map Options")
map_type = st.sidebar.radio(
    "Select Map Type",
    ["National Heatmap", "Province Choropleth", "Punjab Division Map"]
)

@st.cache_data
def load_data():
    df_main = pd.read_csv('data/cleaned/cleaned_main.csv')
    df_punjab = pd.read_csv('data/cleaned/cleaned_punjab.csv')
    return df_main, df_punjab

df_main, df_punjab = load_data()

if map_type == "National Heatmap":
    st.subheader("🔥 National Accident Heatmap")
    st.caption("Heatmap based on major city accident volumes across Pakistan")

    city_coords = [
        [31.5497, 74.3436, 1117490], [31.4504, 73.1350, 428228],
        [30.1978, 71.4711, 327871],  [32.1877, 74.1945, 289230],
        [33.5651, 73.0169, 177337],  [29.3956, 71.6836, 159338],
        [31.9726, 72.6748, 125292],  [32.4945, 74.5229, 133161],
        [34.0151, 71.5249, 85000],   [34.1688, 73.2215, 45000],
        [24.8607, 67.0011, 95000],   [25.3960, 68.3578, 55000],
        [27.5290, 68.7578, 35000],   [30.1798, 66.9750, 42000],
        [33.6844, 73.0479, 120000],
    ]

    df_heat = pd.DataFrame(city_coords, columns=['lat', 'lon', 'weight'])
    df_heat['weight_norm'] = df_heat['weight'] / df_heat['weight'].max()

    m = folium.Map(location=[30.3753, 69.3451], zoom_start=5,
                   tiles='CartoDB positron')

    HeatMap(
        df_heat[['lat', 'lon', 'weight_norm']].values.tolist(),
        min_opacity=0.3, max_opacity=0.9, radius=40, blur=25,
        gradient={0.2: SKY, 0.5: BLUE, 0.7: RED, 1.0: DEEP_RED}
    ).add_to(m)

    for _, row in df_heat.iterrows():
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=5, color=NAVY, fill=True,
            fill_color=RED, fill_opacity=0.7,
            popup=f"Accidents: {int(row['weight']):,}"
        ).add_to(m)

    st_folium(m, width=1200, height=500)

elif map_type == "Province Choropleth":
    st.subheader("🗺️ Province Choropleth — Accidents & Fatalities")
    st.info("Loading saved province map...")
    with open('data/cleaned/map_province_accidents.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=500, scrolling=False)

elif map_type == "Punjab Division Map":
    st.subheader("🏙️ Punjab Division Choropleth")
    st.info("Loading saved Punjab division map...")
    with open('data/cleaned/map_punjab_divisions.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=500, scrolling=False)

st.divider()
st.caption("Maps generated using GADM shapefiles and Folium · RoadGuard Pakistan")