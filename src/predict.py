"""Prediction model utilities."""

import numpy as np

def train_temperature_model(df):
    years = df['Year']
    temps = df['Temperature']

    coeffs = np.polyfit(years, temps, 1)
    return np.poly1d(coeffs)


def predict_future(model, start, end):
    years = np.arange(start, end)
    predictions = model(years)
    return years, predictions