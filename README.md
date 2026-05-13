# 🛡️ RoadGuard Pakistan
### Road Traffic Accident Analysis Dashboard

> *Data-driven road safety intelligence for Pakistan*

---

## Overview

RoadGuard Pakistan is an interactive web dashboard built with Streamlit that analyses road traffic accident data across Pakistan. It provides geospatial hotspot maps, exploratory data analysis, and machine learning predictions for accident severity and fatality risk.

## Features

- 📊 KPI summary cards (total accidents, fatalities, top cause)
- 🗺️ Interactive Folium heatmap with province & highway filters
- 📈 15+ EDA charts (trends, causes, severity, weather correlations)
- 🏙️ Province-level comparison with choropleth maps
- 🤖 ML predictions: severity classifier + fatality risk regressor
- 📋 Data-backed policy recommendations

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Dashboard | Streamlit 1.28+ |
| Data | Pandas, NumPy |
| Visualisation | Plotly, Seaborn, Matplotlib |
| Mapping | Folium, GeoPandas |
| ML | scikit-learn, XGBoost, joblib |

## Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/road-accidents-pakistan.git
cd road-accidents-pakistan

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the dashboard
streamlit run app.py
```

## Project Structure

```
roadguard_pakistan/
├── app.py                    # Streamlit entry point
├── pages/                    # Multi-page app
│   ├── 01_overview.py
│   ├── 02_map.py
│   ├── 03_eda.py
│   ├── 04_provinces.py
│   ├── 05_predict.py
│   └── 06_policy.py
├── data/
│   ├── raw/                  # Original source files (gitignored)
│   ├── cleaned/              # Processed CSV + data dictionary
│   └── shapefiles/           # GADM Pakistan shapefiles
├── models/                   # Trained .joblib model files
├── notebooks/                # Jupyter EDA notebooks
├── utils/                    # Helper modules
│   ├── preprocessing.py
│   ├── model_utils.py
│   └── map_utils.py
├── assets/                   # Logo, CSS overrides
├── .streamlit/config.toml    # Theme configuration
└── requirements.txt
```

## Data Sources

- [Kaggle Pakistan Road Accidents Dataset](https://www.kaggle.com)
- [NHMP — National Highway & Motorway Police](https://nhmp.gov.pk)
- [Open-Meteo Weather API](https://open-meteo.com)
- [GADM Pakistan Shapefiles](https://gadm.org)
- [PBS — Pakistan Bureau of Statistics](https://pbs.gov.pk)

## ML Models

| Model | Algorithm | Target | Goal |
|-------|-----------|--------|------|
| Severity Classifier | Random Forest | Minor / Serious / Fatal | >80% accuracy |
| Fatality Regressor | Gradient Boosting | Fatality count | R² > 0.70 |

## Live Demo

🔗 [View on Streamlit Cloud](#) *(link after deployment)*

---

*BS Data Science Project · April 2026*
