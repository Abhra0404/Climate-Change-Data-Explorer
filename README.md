# 🌍 Climate Change Data Explorer

An interactive data science project that analyzes global climate trends, uncovers relationships between key environmental factors, and predicts future climate conditions.

---

## 🚀 Live Demo

👉 https://climate-change-data-explorer.streamlit.app/

---

## 📌 Problem Statement

Climate change is one of the most critical challenges of our time. Understanding how factors like CO₂ emissions, global temperature, and sea level are interconnected is essential for making informed decisions.

This project aims to:

* Analyze historical climate data
* Identify key trends and correlations
* Build predictive models for future climate changes
* Present insights through an interactive dashboard

---

## 📊 Datasets Used

The project integrates multiple real-world datasets:

* 🌡 **Global Land Temperature**
* 🏭 **CO₂ Emissions Data**
* 🌊 **Global Sea Level Rise**

### 🧹 Data Processing

* Cleaned missing values
* Standardized time format (Year)
* Aggregated yearly averages
* Merged multiple datasets into a unified structure

---

## 🧠 Key Features

### 📈 Interactive Dashboard

* Built using **Streamlit + Plotly**
* Dynamic metric selection
* Year range filtering
* Smooth interactive visualizations

### 📊 Data Visualizations

* Time-series trend analysis
* Multi-variable comparison charts
* Correlation heatmaps
* Scatter plots with regression

### 🌍 Geospatial Visualization

* Interactive world map using Plotly
* Animated data exploration

### 🔮 Predictive Modeling

* Linear regression using NumPy
* Future temperature forecasting
* Trend projection visualization

### 🧠 Insight Engine

* Automatically highlights:

  * CO₂ → Temperature correlation
  * Temperature → Sea level impact
  * Recent climate anomalies

---

## 🛠 Tech Stack

* **Python**
* **NumPy** → numerical computation
* **Pandas** → data processing
* **Matplotlib & Seaborn** → static visualization
* **Plotly** → interactive charts
* **Streamlit** → dashboard UI

---

## 📁 Project Structure

```
climate-explorer/
│
├── app/
│   └── app.py              # Streamlit dashboard
│
├── data/
│   ├── raw/               # Original datasets
│   └── cleaned/           # Processed datasets
│
├── src/
│   ├── preprocess.py      # Data cleaning logic
│   ├── analysis.py        # Data merging
│   ├── visualize.py       # Visualization functions
│   └── predict.py         # Prediction logic
│
├── notebooks/             # EDA & experimentation
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/climate-explorer.git
cd climate-explorer
```

### 2️⃣ Install dependencies

```
pip3 install -r requirements.txt
```

### 3️⃣ Run the dashboard

```
streamlit run app/app.py
```

---

## 🔮 Future Improvements

* Integrate real-time climate APIs
* Add advanced machine learning models
* Improve geospatial accuracy with country-level datasets
* Deploy full-stack version with backend APIs

---

## 🌟 Key Insights

* Global temperatures show a **consistent upward trend**
* Strong positive correlation between **CO₂ emissions and temperature**
* Rising temperatures contribute to **sea level increase**
* Recent years exhibit **accelerated warming patterns**

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and improve the project.

---

## ⭐ Show your support

If you found this project useful, consider giving it a star ⭐

---

## 👤 Author

**Abhra**
Aspiring Software Engineer & Data Enthusiast

---
