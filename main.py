from src.preprocess import clean_temperature, clean_co2, clean_sea
from src.analysis import merge_data
from src.visualize import plot_trends, plot_heatmap
from src.predict import train_temperature_model, predict_future

# Load & clean
temp = clean_temperature("data/raw/global_temp.csv")
co2 = clean_co2("data/raw/co2.csv")
sea = clean_sea("data/raw/sea_level.csv")

# Merge
df = merge_data(temp, co2, sea)

# Visualize
plot_trends(df)
plot_heatmap(df)

# Predict
model = train_temperature_model(df)
years, preds = predict_future(model, 2025, 2040)

print("\nFuture Temperature Predictions:\n")

for year, temp in zip(years, preds):
    print(f"{int(year)} → {temp:.2f}°C")