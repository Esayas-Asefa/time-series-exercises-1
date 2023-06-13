import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import prepare as prep
import env 

def prep_sales(df):
    df.sale_date = df.sale_date.str.replace('00:00:00 GMT', '')
    df.sale_date = df.sale_date.str.strip()
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y')
    df.set_index('sale_date', inplace=True)
    df.reset_index('sale_date', inplace=True)
    df['year'] = df.sale_date.dt.year
    df['month'] = df.sale_date.dt.month
    df['dayofweek'] = df.sale_date.dt.day_of_week
    df['sales_total'] = df.sale_amount * df.item_price
    seasons = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11]}
    def assign_season(month):
        for season, months in seasons.items():
            if month in months:
                return season
    df['Season'] = df.sale_date.dt.month.apply(assign_season)
    total_nulls = df.isnull().sum().sum()
    threshold = len(df) * len(df.columns) * 0.05
    if total_nulls <= threshold:
        df = df.dropna()
        print("Null values deleted successfully!")
    else:
        print("The total number of null values exceeds the threshold. No deletion performed.")     
    #print(df)
    # if null count per column is less than 5 percent of total, drop
    # if null count per column is greater than 5 percent replace with mean for that column
    
    return df

