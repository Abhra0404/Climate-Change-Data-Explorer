"""Data preprocessing utilities."""

import pandas as pd

def clean_temperature(path):
    df = pd.read_csv(path)
    df['Year'] = pd.to_datetime(df['dt']).dt.year
    df = df.groupby('Year')['AverageTemperature'].mean().reset_index()
    df.rename(columns={'AverageTemperature': 'Temperature'}, inplace=True)
    return df


def clean_co2(path):
    df = pd.read_csv(path)
    year_col = 'year' if 'year' in df.columns else 'Year'
    value_col = 'value' if 'value' in df.columns else 'CO2'

    df = df.groupby(year_col)[value_col].mean().reset_index()
    df.rename(columns={year_col: 'Year', value_col: 'CO2'}, inplace=True)
    return df


def clean_sea(path):
    df = pd.read_csv(path)
    df.rename(columns={
        'year': 'Year',
        'mmfrom1993-2008average': 'SeaLevel',
        'obs8': 'SeaLevel'
    }, inplace=True)

    df = df.groupby('Year')['SeaLevel'].mean().reset_index()
    return df