"""Exploratory and statistical analysis helpers."""

def merge_data(temp, co2, sea):
    df = temp.merge(co2, on='Year', how='inner')
    df = df.merge(sea, on='Year', how='inner')

    df = df.sort_values('Year')
    df = df.dropna()

    return df