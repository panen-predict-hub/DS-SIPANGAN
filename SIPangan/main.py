import streamlit as st
import pandas as pd
import plotly.express as px
import os


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="SIPangan Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
.block-container {
    max-width: 1220px;
    padding-top: 1.3rem;
    padding-bottom: 1.5rem;
}

h1 {
    font-size: 1.85rem !important;
    font-weight: 700 !important;
    color: #1f2937;
    margin-bottom: 0.15rem !important;
}

h2, h3 {
    color: #1f2937;
    font-weight: 650 !important;
}

p, label, span {
    color: #374151;
}

[data-testid="stMetric"] {
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    padding: 0.85rem 1rem;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    color: #6b7280 !important;
}

[data-testid="stMetricValue"] {
    font-size: 1.18rem !important;
    font-weight: 700 !important;
    color: #111827 !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
    border-bottom: 1px solid #e5e7eb;
}

.stTabs [data-baseweb="tab"] {
    height: 40px;
    padding-left: 0.9rem;
    padding-right: 0.9rem;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    color: #2563eb !important;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.65rem;
}

.small-caption {
    font-size: 0.92rem;
    color: #6b7280;
    margin-bottom: 0.7rem;
}

.insight-box {
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    border-left: 4px solid #2563eb;
    padding: 0.85rem 1rem;
    border-radius: 12px;
    font-size: 0.92rem;
    color: #1f2937;
    line-height: 1.55;
}

hr {
    margin-top: 0.3rem;
    margin-bottom: 0.7rem;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(__file__)
    DATA_PATH = os.path.join(BASE_DIR, "data", "data_final.csv")

    data = pd.read_csv(DATA_PATH)

    data["periode_update"] = pd.to_datetime(data["periode_update"])
    data["tahun"] = data["periode_update"].dt.year
    data["bulan"] = data["periode_update"].dt.month
    data["tahun_bulan"] = data["periode_update"].dt.to_period("M").astype(str)

    if "series_id" not in data.columns:
        data["series_id"] = (
            data["nama_kabupaten_kota"].astype(str)
            + " | "
            + data["kategori"].astype(str)
        )

    return data


data = load_data()
