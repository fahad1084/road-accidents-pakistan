# 🛡️ RoadGuard Pakistan
### Road Traffic Accident Analysis Dashboard

> *Data-driven road safety intelligence for Pakistan*

🔗 **Live Dashboard:** https://road-accidents-pakistan-mzv8xqsctzm4f9tpa9ntq4.streamlit.app

---

## Overview

RoadGuard Pakistan is an interactive web dashboard built with Streamlit that analyses road traffic accident data across Pakistan. It provides geospatial hotspot maps, exploratory data analysis, machine learning predictions for accident severity and fatality risk, and data-backed policy recommendations.

Pakistan records 30,000+ road fatalities annually yet no centralised, publicly accessible analytical platform existed. RoadGuard Pakistan addresses this gap.

---

## Features

| Page | Description |
|------|-------------|
| 📊 Overview | KPI summary cards — total accidents, fatalities, injuries, worst province |
| 🗺️ Accident Map | Interactive Folium heatmap + province & Punjab division choropleth maps |
| 📈 EDA & Trends | 15 exploratory charts — trends, causes, severity, province comparisons |
| 🏙️ Province Comparison | Side-by-side stats, radar chart, severity trends per province |
| 🤖 ML Predictions | Severity classifier form + fatality risk regressor with gauge chart |
| 📋 Policy Insights | 7 data-backed policy recommendations with supporting charts |
| 👤 About | Project background, data sources, tech stack, author info |

---

## ML Model Performance

| Model | Algorithm | Target | Score | Target Met |
|-------|-----------|--------|-------|------------|
| Severity Classifier | Random Forest | Low / Medium / High | 100% Accuracy | ✅ (>80%) |
| Fatality Regressor | Gradient Boosting | Killed count | R² = 0.9958 | ✅ (>0.70) |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Dashboard | Streamlit 1.28+ |
| Data | Pandas, NumPy |
| Visualisation | Plotly, Seaborn, Matplotlib |
| Mapping | Folium, GeoPandas, streamlit-folium |
| ML | scikit-learn, XGBoost, joblib |

---

## Data Sources

| Source | Description |
|--------|-------------|
| [NTRC / PBS via Kaggle](https://www.kaggle.com/datasets/ahsanneural/pakistan-traffic-accidents-ntrc-and-pbs) | Province-level accident data 2006–2023 |
| [Road Accident in Pakistan 2012–2021](https://www.kaggle.com/datasets/mohsinali123/road-accident-in-pakistan-2012-2021) | Monthly national accident records |
| [Rescue 1122 Punjab](https://www.kaggle.com) | District-level emergency call data for 37 Punjab districts |
| [GADM Shapefiles](https://gadm.org) | Pakistan province & district boundary shapefiles |
| [Open-Meteo API](https://open-meteo.com) | Weather data for major Pakistani cities |

---

## Project Structure

```
roadguard_pakistan/
├── app.py                        # Streamlit entry point
├── pages/
│   ├── 01_overview.py            # KPI dashboard
│   ├── 02_map.py                 # Interactive maps
│   ├── 03_eda.py                 # 15 EDA charts
│   ├── 04_provinces.py           # Province comparison
│   ├── 05_predict.py             # ML predictions
│   ├── 06_policy.py              # Policy recommendations
│   └── 07_about.py               # About page
├── data/
│   ├── raw/                      # Original source files (gitignored)
│   ├── cleaned/                  # Processed CSVs + maps + dictionary
│   └── shapefiles/               # GADM Pakistan shapefiles (gitignored)
├── models/                       # Trained .joblib model files
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_part1.ipynb
│   ├── 03_eda_part2_geo.ipynb
│   ├── 04_ml_training.ipynb
│   └── 05_geospatial.ipynb
├── utils/
│   ├── styles.py                 # Shared sidebar & CSS
│   ├── preprocessing.py
│   ├── model_utils.py
│   └── map_utils.py
├── assets/                       # Logo, images
├── .streamlit/config.toml        # Theme configuration
└── requirements.txt
```

---

## Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/road-accidents-pakistan.git
cd road-accidents-pakistan

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the dashboard
streamlit run app.py
```

---

## Limitations

- District-level data is only available for Punjab (Rescue 1122). Other provinces have province-year level data only.
- Dataset is based on reported accidents — actual figures may be higher due to underreporting.
- ML models trained on aggregate data; individual accident-level prediction requires more granular data.

---

## Future Improvements

- Real-time accident data integration via API
- District-level data for Sindh, KPK, and Balochistan
- Year range filter across all dashboard pages
- Dark mode support
- Downloadable filtered data as CSV
- Mobile-optimised layout

---

*BS Data Science Project · May 2026 · Pakistan*