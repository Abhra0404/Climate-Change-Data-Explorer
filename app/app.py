import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Climate Explorer", layout="wide")

# -------------------- LOAD DATA --------------------
df = pd.read_csv("../data/cleaned/final_climate_data.csv")

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.metric-card {
    background-color: #111;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
.big-font {
    font-size: 28px;
    font-weight: bold;
}
.small-font {
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
st.sidebar.title("⚙️ Controls")

metric = st.sidebar.selectbox(
    "Select Metric",
    ["Temperature", "CO2", "SeaLevel"]
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df['Year'].min()),
    int(df['Year'].max()),
    (1960, 2020)
)

normalize = st.sidebar.checkbox("Normalize Data")

# Filter data
df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Normalize if selected
if normalize:
    df_plot = (df - df.min()) / (df.max() - df.min())
else:
    df_plot = df

# -------------------- HEADER --------------------
st.title("🌍 Climate Change Explorer")
st.markdown("A data-driven dashboard analyzing global climate trends and predictions.")

# -------------------- KPI CARDS --------------------
col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="metric-card">
    <div class="small-font">Latest Temperature</div>
    <div class="big-font">{df['Temperature'].iloc[-1]:.2f}°C</div>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="metric-card">
    <div class="small-font">Latest CO₂</div>
    <div class="big-font">{df['CO2'].iloc[-1]:.2f}</div>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="metric-card">
    <div class="small-font">Sea Level</div>
    <div class="big-font">{df['SeaLevel'].iloc[-1]:.2f}</div>
</div>
""", unsafe_allow_html=True)

# -------------------- CHARTS --------------------
col1, col2 = st.columns(2)

# Trend Chart
with col1:
    st.subheader(f"{metric} Trend")
    fig, ax = plt.subplots()
    ax.plot(df['Year'], df_plot[metric], linewidth=2)
    ax.set_title(f"{metric} Over Time")
    st.pyplot(fig)

# Heatmap
with col2:
    st.subheader("Correlation")
    fig, ax = plt.subplots()
    sns.heatmap(df[['Temperature','CO2','SeaLevel']].corr(),
                annot=True,
                cmap='coolwarm',
                ax=ax)
    st.pyplot(fig)

# -------------------- SCATTER RELATION --------------------
st.subheader("Relationships")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.regplot(x='CO2', y='Temperature', data=df, ax=ax)
    ax.set_title("CO₂ vs Temperature")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.regplot(x='Temperature', y='SeaLevel', data=df, ax=ax)
    ax.set_title("Temperature vs Sea Level")
    st.pyplot(fig)

# -------------------- PREDICTION --------------------
st.subheader("🔮 Future Prediction")

years = df['Year']
temps = df['Temperature']

coeffs = np.polyfit(years, temps, 1)
trend = np.poly1d(coeffs)

future_years = np.arange(df['Year'].max()+1, df['Year'].max()+20)
future_preds = trend(future_years)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(years, temps, label="Actual")
ax.plot(future_years, future_preds, linestyle='--', label="Predicted")
ax.legend()
ax.set_title("Temperature Forecast")

left_pad, pred_col, right_pad = st.columns([1, 2, 1])
with pred_col:
    st.pyplot(fig, use_container_width=False)

# -------------------- INSIGHTS --------------------
st.subheader("🧠 Key Insights")

corr = df[['Temperature','CO2','SeaLevel']].corr()

if corr.loc['CO2','Temperature'] > 0.7:
    st.success("Strong correlation between CO₂ and temperature")

if corr.loc['Temperature','SeaLevel'] > 0.7:
    st.info("Temperature rise contributes to sea level rise")

if df['Temperature'].iloc[-1] > df['Temperature'].mean():
    st.warning("Recent years show abnormal warming trends")