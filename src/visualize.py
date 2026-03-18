"""Visualization helpers for climate data."""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Year'], df['Temperature'], label='Temperature')
    plt.plot(df['Year'], df['CO2'], label='CO2')
    plt.plot(df['Year'], df['SeaLevel'], label='Sea Level')
    plt.legend()
    plt.title("Climate Trends")
    plt.show()


def plot_heatmap(df):
    sns.heatmap(df[['Temperature','CO2','SeaLevel']].corr(), annot=True)
    plt.title("Correlation Heatmap")
    plt.show()