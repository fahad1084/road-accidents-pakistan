import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import sys
sys.path.append('.')
from utils.styles import apply_sidebar
# Brand colours
NAVY = '#0C447C'
BLUE = '#185FA5'
SKY = '#378ADD'
RED = '#E24B4A'
OFF_WHITE = '#F1EFE8'

st.set_page_config(page_title="Predictions | RoadGuard Pakistan",
                   page_icon="🤖", layout="wide")
apply_sidebar()

st.title("🤖 ML Predictions")
st.markdown("#### Predict accident severity and fatality risk using trained models")
st.divider()

# Load models
@st.cache_resource
def load_models():
    rf_clf = joblib.load('models/severity_classifier_rf.joblib')
    gb_reg = joblib.load('models/fatality_regressor_gb.joblib')
    scaler_clf = joblib.load('models/scaler_classifier.joblib')
    scaler_reg = joblib.load('models/scaler_regressor.joblib')
    le_severity = joblib.load('models/label_encoder_severity.joblib')
    le_province = joblib.load('models/label_encoder_province.joblib')
    return rf_clf, gb_reg, scaler_clf, scaler_reg, le_severity, le_province

rf_clf, gb_reg, scaler_clf, scaler_reg, le_severity, le_province = load_models()

# Two column layout
col_left, col_right = st.columns(2)

# --- CLASSIFIER ---
with col_left:
    st.subheader("🔴 Severity Classifier")
    st.markdown("Predict whether an accident scenario is **Low, Medium or High** severity.")
    st.markdown("")

    province = st.selectbox("Province", le_province.classes_)
    year = st.slider("Year", 2006, 2023, 2018)
    total_accidents = st.number_input("Total Accidents (annual)", 100, 60000, 5000)
    fatal_accidents = st.number_input("Fatal Accidents", 50, 30000, 2000)
    non_fatal = st.number_input("Non Fatal Accidents", 50, 30000, 3000)
    vehicles = st.number_input("Total Vehicles Involved", 100, 70000, 6000)
    fatality_rate = st.slider("Fatality Rate", 0.0, 150.0, 50.0)
    injury_rate = st.slider("Injury Rate", 0.0, 200.0, 80.0)
    fatal_ratio = st.slider("Fatal Accident Ratio", 0.0, 1.0, 0.4)
    veh_per_acc = st.slider("Vehicles Per Accident", 0.5, 3.0, 1.2)

    if st.button("🔍 Predict Severity", use_container_width=True):
        province_enc = le_province.transform([province])[0]
        input_clf = np.array([[province_enc, year, total_accidents,
                               fatal_accidents, non_fatal, vehicles,
                               fatality_rate, injury_rate,
                               fatal_ratio, veh_per_acc]])
        input_scaled = scaler_clf.transform(input_clf)
        prediction = rf_clf.predict(input_scaled)[0]
        probabilities = rf_clf.predict_proba(input_scaled)[0]
        severity_label = le_severity.inverse_transform([prediction])[0]

        # Display result
        color = RED if severity_label == 'High' else (
            BLUE if severity_label == 'Medium' else SKY)
        st.markdown(f"""
        <div style='background:{color}; padding:20px; border-radius:10px;
                    text-align:center; margin-top:10px;'>
            <h2 style='color:white; margin:0;'>⚠️ {severity_label} Severity</h2>
        </div>
        """, unsafe_allow_html=True)

        # Probability bar chart
        fig = go.Figure(go.Bar(
            x=le_severity.classes_,
            y=probabilities,
            marker_color=[RED if c == 'High' else BLUE if c == 'Medium' else SKY
                          for c in le_severity.classes_]
        ))
        fig.update_layout(
            title='Prediction Confidence',
            plot_bgcolor=OFF_WHITE,
            paper_bgcolor='white',
            yaxis_title='Probability',
            yaxis=dict(range=[0, 1])
        )
        st.plotly_chart(fig, use_container_width=True)

# --- REGRESSOR ---
with col_right:
    st.subheader("📈 Fatality Risk Predictor")
    st.markdown("Estimate the **number of people killed** given accident conditions.")
    st.markdown("")

    province_r = st.selectbox("Province ", le_province.classes_)
    year_r = st.slider("Year ", 2006, 2023, 2018)
    total_acc_r = st.number_input("Total Accidents ", 100, 60000, 5000)
    fatal_acc_r = st.number_input("Fatal Accidents ", 50, 30000, 2000)
    non_fatal_r = st.number_input("Non Fatal Accidents ", 50, 30000, 3000)
    vehicles_r = st.number_input("Total Vehicles Involved ", 100, 70000, 6000)
    fatality_rate_r = st.slider("Fatality Rate ", 0.0, 150.0, 50.0)
    injury_rate_r = st.slider("Injury Rate ", 0.0, 200.0, 80.0)
    severity_idx = st.slider("Severity Index", 1.0, 4.0, 2.5)

    if st.button("📊 Estimate Fatality Risk", use_container_width=True):
        province_enc_r = le_province.transform([province_r])[0]
        input_reg = np.array([[province_enc_r, year_r, total_acc_r,
                               fatal_acc_r, non_fatal_r, vehicles_r,
                               fatality_rate_r, injury_rate_r, severity_idx]])
        input_scaled_r = scaler_reg.transform(input_reg)
        prediction_r = gb_reg.predict(input_scaled_r)[0]
        predicted_killed = max(0, round(prediction_r))

        # Display result
        st.markdown(f"""
        <div style='background:{NAVY}; padding:20px; border-radius:10px;
                    text-align:center; margin-top:10px;'>
            <h2 style='color:white; margin:0;'>💀 Estimated Killed: {predicted_killed:,}</h2>
        </div>
        """, unsafe_allow_html=True)

        # Gauge chart
        fig2 = go.Figure(go.Indicator(
            mode='gauge+number',
            value=predicted_killed,
            title={'text': 'Predicted Fatalities'},
            gauge={
                'axis': {'range': [0, 40000]},
                'bar': {'color': RED},
                'steps': [
                    {'range': [0, 10000], 'color': '#E6F1FB'},
                    {'range': [10000, 25000], 'color': '#B5D4F4'},
                    {'range': [25000, 40000], 'color': '#FCEBEB'},
                ],
                'threshold': {
                    'line': {'color': NAVY, 'width': 4},
                    'thickness': 0.75,
                    'value': predicted_killed
                }
            }
        ))
        fig2.update_layout(paper_bgcolor='white', height=300)
        st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.caption("Models: Random Forest Classifier + Gradient Boosting Regressor · RoadGuard Pakistan")