# 🛡️ RoadGuard Pakistan
### Road Traffic Accident Analysis Dashboard

> *Data-driven road safety intelligence for Pakistan*

🔗 **Live Dashboard:** https://road-accidents-pakistan-mzv8xqsctzm4f9tpa9ntq4.streamlit.app

![Version](https://img.shields.io/badge/version-v2.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red)

---

## Overview

Pakistan records over **30,000 road fatalities annually** — one of the highest rates in Asia — yet no centralised, publicly accessible analytical platform existed. **RoadGuard Pakistan** addresses this gap by transforming raw accident data into actionable insights through an interactive web dashboard, machine learning models, and data-backed policy recommendations.

---

## 🗂️ Dashboard Pages

| Page | Description |
|------|-------------|
| 📊 Overview | KPI summary cards — total accidents, fatalities, injuries |
| 🗺️ Accident Map | Interactive Folium heatmap + province & Punjab choropleth maps |
| 📈 EDA & Trends | 15+ charts with year range filter and CSV download |
| 🏙️ Province Comparison | Side-by-side stats, radar chart, severity trends |
| 🤖 ML Predictions | Severity classifier + fatality risk regressor |
| 📋 Policy Insights | 7 data-backed policy recommendations |
| 🌍 International Benchmark | Pakistan vs India, Bangladesh, UK, global averages |
| 🧮 Risk Calculator | Personal road accident risk score estimator |
| 📋 Province Scorecard | Safety grade and detailed scorecard per province |
| ⚠️ Dangerous Roads | Top 10 most dangerous highways with interactive map |
| 👤 About | Project background, data sources, tech stack |

---

## 🤖 ML Model Performance

| Model | Algorithm | Target | Score | Target Met |
|-------|-----------|--------|-------|------------|
| Severity Classifier | Random Forest | Low / Medium / High | 100% Accuracy | ✅ (>80%) |
| Fatality Regressor | Gradient Boosting | Killed count | R² = 0.9958 | ✅ (>0.70) |
| Baseline Classifier | Logistic Regression | Low / Medium / High | 92.31% Accuracy | ✅ |
| Baseline Regressor | Linear Regression | Killed count | R² = 0.9984 | ✅ |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Dashboard | Streamlit 1.28+ |
| Data | Pandas, NumPy, OpenPyXL |
| Visualisation | Plotly, Seaborn, Matplotlib |
| Mapping | Folium, GeoPandas, streamlit-folium |
| ML | scikit-learn, XGBoost, joblib |
| Deployment | Streamlit Community Cloud |

---

## 📦 Data Sources

| Source | Description |
|--------|-------------|
| NTRC & PBS via Kaggle | Province-level accident data 2006–2023 |
| Road Accident in Pakistan 2012–2021 | Monthly national accident records |
| Rescue 1122 Punjab | District-level emergency data — 37 Punjab districts |
| GADM Shapefiles | Pakistan province & district boundary shapefiles |
| Open-Meteo API | Weather data for major Pakistani cities |
| WHO Global Road Safety Report 2023 | International benchmarking data |

---

## 📁 Project Structure

```
roadguard_pakistan/
├── app.py
├── pages/
│   ├── 01_Overview.py
│   ├── 02_Map.py
│   ├── 03_Eda.py
│   ├── 04_Provinces.py
│   ├── 05_Predict.py
│   ├── 06_Policy.py
│   ├── 07_About.py
│   ├── 08_benchmarking.py
│   ├── 09_calculator.py
│   ├── 10_scorecard.py
│   └── 11_dangerous_roads.py
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── shapefiles/
├── models/
├── notebooks/
├── utils/
│   └── styles.py
├── .streamlit/config.toml
└── requirements.txt
```

---

## 🚀 Setup & Installation

```bash
git clone https://github.com/YOUR_USERNAME/road-accidents-pakistan.git
cd road-accidents-pakistan
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Version History

| Version | Release | Features |
|---------|---------|----------|
| v1.0 | May 2026 | Core dashboard — 15 charts, 3 maps, 2 ML models, 7 policy recs |
| v2.0 | May 2026 | + Benchmarking, Risk calculator, Scorecard, Dangerous roads, CSV download |

---

## ⚠️ Limitations

- District-level data only available for Punjab
- Dataset based on reported accidents
- ML models trained on aggregate data
- International benchmarking uses WHO 2023 estimates

---

## 🔮 Future Work (V3.0)

- Real-time accident data integration
- District-level data for all provinces
- Weather correlation analysis
- Mobile-optimised layout
- Hospital & insurance system integration

---

*RoadGuard Pakistan · BS Data Science Project · 2026 · 🇵🇰*