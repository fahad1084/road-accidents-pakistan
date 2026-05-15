import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import sys
sys.path.append('.')
from utils.styles import apply_sidebar

NAVY = '#0C447C'
BLUE = '#185FA5'
SKY = '#378ADD'
RED = '#E24B4A'
OFF_WHITE = '#F1EFE8'

st.set_page_config(page_title="Risk Calculator | RoadGuard Pakistan",
                   page_icon="🧮", layout="wide")
apply_sidebar()

st.title("🧮 Accident Risk Calculator")
st.markdown("#### Estimate your road accident risk based on conditions")
st.divider()

# ── Input form ──
st.subheader("Enter Journey Details")

col1, col2, col3 = st.columns(3)

with col1:
    province = st.selectbox("🏙️ Province", [
        "Punjab", "Sindh", "Khyber Pakhtunkhwa",
        "Balochistan", "Islamabad"])
    road_type = st.selectbox("🛣️ Road Type", [
        "National Highway", "Motorway",
        "City Road", "Rural Road"])
    time_of_day = st.selectbox("🕐 Time of Day", [
        "Morning (6am-9am)", "Daytime (9am-5pm)",
        "Evening (5pm-8pm)", "Night (8pm-6am)"])

with col2:
    weather = st.selectbox("🌤️ Weather", [
        "Clear", "Foggy", "Rainy", "Dusty"])
    vehicle_type = st.selectbox("🚗 Vehicle Type", [
        "Car", "Motorcycle", "Bus/Coach",
        "Truck/HGV", "Rickshaw"])
    speed = st.slider("⚡ Estimated Speed (km/h)", 20, 160, 80)

with col3:
    seatbelt = st.radio("🪢 Seatbelt Worn?", ["Yes", "No"])
    phone = st.radio("📱 Using Phone While Driving?", ["No", "Yes"])
    experience = st.slider("🎓 Driving Experience (years)", 0, 30, 5)

st.divider()

if st.button("🧮 Calculate Risk Score", use_container_width=True):

    # ── Risk scoring logic ──
    score = 0

    # Province risk
    province_risk = {
        "Punjab": 25, "Sindh": 30,
        "Khyber Pakhtunkhwa": 20,
        "Balochistan": 22, "Islamabad": 15
    }
    score += province_risk[province]

    # Road type risk
    road_risk = {
        "National Highway": 25, "Motorway": 10,
        "City Road": 20, "Rural Road": 30
    }
    score += road_risk[road_type]

    # Time of day risk
    time_risk = {
        "Morning (6am-9am)": 20, "Daytime (9am-5pm)": 10,
        "Evening (5pm-8pm)": 20, "Night (8pm-6am)": 30
    }
    score += time_risk[time_of_day]

    # Weather risk
    weather_risk = {
        "Clear": 5, "Foggy": 25,
        "Rainy": 20, "Dusty": 15
    }
    score += weather_risk[weather]

    # Vehicle risk
    vehicle_risk = {
        "Car": 10, "Motorcycle": 30,
        "Bus/Coach": 15, "Truck/HGV": 20,
        "Rickshaw": 25
    }
    score += vehicle_risk[vehicle_type]

    # Speed risk
    if speed < 60:
        score += 5
    elif speed < 100:
        score += 15
    elif speed < 130:
        score += 25
    else:
        score += 35

    # Seatbelt
    score += 0 if seatbelt == "Yes" else 20

    # Phone
    score += 0 if phone == "No" else 25

    # Experience
    if experience < 2:
        score += 20
    elif experience < 5:
        score += 10
    else:
        score += 0

    # Normalise to 0-100
    max_possible = 25 + 30 + 30 + 25 + 30 + 35 + 20 + 25 + 20
    risk_score = min(100, int((score / max_possible) * 100))

    # Risk label
    if risk_score < 30:
        risk_label = "🟢 Low Risk"
        risk_color = SKY
        advice = "Good conditions for driving. Stay alert and follow traffic rules."
    elif risk_score < 60:
        risk_label = "🟡 Medium Risk"
        risk_color = '#C9A800'
        advice = "Moderate risk detected. Drive carefully and reduce speed."
    elif risk_score < 80:
        risk_label = "🟠 High Risk"
        risk_color = '#E07B39'
        advice = "High risk conditions. Consider delaying journey or taking precautions."
    else:
        risk_label = "🔴 Very High Risk"
        risk_color = RED
        advice = "Extremely dangerous conditions. Avoid this journey if possible."

    # ── Results ──
    st.subheader("📊 Risk Assessment Results")

    col_res1, col_res2 = st.columns(2)

    with col_res1:
        # Gauge chart
        fig = go.Figure(go.Indicator(
            mode='gauge+number',
            value=risk_score,
            title={'text': 'Risk Score', 'font': {'size': 20}},
            number={'suffix': '/100'},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': risk_color},
                'steps': [
                    {'range': [0, 30], 'color': '#E6F1FB'},
                    {'range': [30, 60], 'color': '#FFF9E6'},
                    {'range': [60, 80], 'color': '#FFF0E6'},
                    {'range': [80, 100], 'color': '#FCEBEB'},
                ],
                'threshold': {
                    'line': {'color': NAVY, 'width': 4},
                    'thickness': 0.75,
                    'value': risk_score
                }
            }
        ))
        fig.update_layout(paper_bgcolor='white', height=300)
        st.plotly_chart(fig, use_container_width=True)

    with col_res2:
        st.markdown(f"""
        <div style='background:{risk_color}; padding:20px; border-radius:12px;
                    text-align:center; margin-bottom:16px;'>
            <h2 style='color:white; margin:0;'>{risk_label}</h2>
            <p style='color:white; margin:8px 0 0 0; font-size:14px;'>{advice}</p>
        </div>
        """, unsafe_allow_html=True)

        # Risk breakdown
        st.markdown("**Risk Factor Breakdown:**")
        factors = {
            "Province": province_risk[province],
            "Road Type": road_risk[road_type],
            "Time of Day": time_risk[time_of_day],
            "Weather": weather_risk[weather],
            "Vehicle Type": vehicle_risk[vehicle_type],
            "Speed": 5 if speed < 60 else 15 if speed < 100 else 25 if speed < 130 else 35,
            "No Seatbelt": 0 if seatbelt == "Yes" else 20,
            "Phone Use": 0 if phone == "No" else 25,
            "Experience": 20 if experience < 2 else 10 if experience < 5 else 0
        }

        for factor, val in factors.items():
            if val > 0:
                bar_width = int((val / 35) * 100)
                color = RED if val >= 25 else BLUE if val >= 15 else SKY
                st.markdown(f"""
                <div style='margin-bottom:6px;'>
                    <div style='display:flex; justify-content:space-between;
                                font-size:13px; margin-bottom:2px;'>
                        <span>{factor}</span><span>{val} pts</span>
                    </div>
                    <div style='background:#E6F1FB; border-radius:4px; height:8px;'>
                        <div style='background:{color}; width:{bar_width}%;
                                    border-radius:4px; height:8px;'></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.divider()

    # Safety tips
    st.subheader("💡 Safety Recommendations")
    tips = []
    if seatbelt == "No":
        tips.append("🪢 **Always wear your seatbelt** — reduces fatality risk by 45%")
    if phone == "Yes":
        tips.append("📵 **Put your phone away** — phone use increases crash risk by 4x")
    if speed > 100:
        tips.append("⚡ **Reduce your speed** — every 10km/h increases fatal crash risk by 25%")
    if weather in ["Foggy", "Rainy"]:
        tips.append(f"🌤️ **Extra caution in {weather.lower()} conditions** — increase following distance")
    if time_of_day == "Night (8pm-6am)":
        tips.append("🌙 **Night driving is high risk** — ensure headlights work and stay alert")
    if vehicle_type == "Motorcycle":
        tips.append("🏍️ **Wear a helmet** — motorcyclists are 29x more likely to die in crashes")
    if experience < 2:
        tips.append("🎓 **New driver detected** — consider advanced driving lessons")
    if not tips:
        tips.append("✅ Good choices! Keep following safe driving practices.")

    for tip in tips:
        st.markdown(f"- {tip}")

st.divider()
st.caption("Risk scores are estimates based on Pakistan road safety statistics · RoadGuard Pakistan")