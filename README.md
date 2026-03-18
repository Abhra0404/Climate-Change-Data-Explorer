# 🌍 Climate Change Data Explorer

## 🚀 Problem Statement

Climate change is one of the most pressing global challenges today. Rising temperatures, increasing CO₂ emissions, and shifting climate patterns demand deeper understanding through data.

This project aims to:

* Analyze historical climate data
* Identify trends and correlations
* Generate meaningful insights
* Predict future temperature changes

The goal is to transform raw data into **actionable insights and visual storytelling**.

---

## 📊 Dataset Information

This project uses publicly available datasets:

### 1. Global Temperature Data

* Contains historical temperature records over time
* Key fields: `Year`, `AverageTemperature`, `Country`

### 2. CO₂ Emissions Data

* Country-wise CO₂ emissions over time
* Key fields: `Year`, `Country`, `CO2 Emissions`

### 🧹 Data Processing Steps:

* Removed missing/null values
* Converted date columns into year format
* Aggregated yearly averages
* Merged datasets based on `Year` and `Country`

---

## 🔍 Key Insights

* 📈 Global temperatures show a **clear upward trend** over the past century
* 🌍 Strong positive correlation between **CO₂ emissions and temperature rise**
* 🔥 Post-2000 period shows **accelerated warming compared to previous decades**
* 🌡️ Certain regions experience **higher temperature volatility**
* ⚠️ Recent years consistently exceed historical averages → indicating **climate anomalies**

---

## 📸 Screenshots of Visualizations

### 📈 Global Temperature Trend

* Line plot showing temperature rise over years

### 🌍 CO₂ vs Temperature Correlation

* Scatter plot with regression line

### 🔥 Correlation Heatmap

* Relationship between climate variables

### 🌎 Country-wise Comparison

* Multi-line plot comparing temperature trends across countries

*(Add screenshots here once generated)*

---

## 🔮 Future Predictions

Using linear regression (NumPy-based), the project predicts future temperature trends.

### 📌 Key Observations:

* Temperature is expected to **continue rising steadily**
* If current trends persist, future decades may see **significant warming increases**
* CO₂ emissions remain a **critical driving factor**

This highlights the urgency of **sustainable environmental policies**.

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/climate-explorer.git
cd climate-explorer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Jupyter Notebooks

```bash
cd notebooks
jupyter notebook
```

Run notebooks in order:

1. Data Cleaning
2. Analysis
3. Visualization
4. Prediction

---

### (Optional) Run Streamlit App

```bash
cd app
streamlit run app.py
```

---

## 🛠 Tech Stack

* **NumPy** → numerical computations & predictions
* **Pandas** → data cleaning & manipulation
* **Matplotlib** → trend visualization
* **Seaborn** → statistical plots & heatmaps

---

## 🌟 Future Improvements

* Add real-time climate data integration
* Build interactive dashboards
* Implement advanced ML models for prediction
* Deploy as a full-stack web application

---

## 🤝 Contributing

Feel free to fork this repo and enhance it with new features or datasets!

---

## ⭐ If you like this project

Give it a star ⭐ — it motivates further development!

---
