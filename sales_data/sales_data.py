import os
from urllib.request import urlretrieve

import pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
if not os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(excel, 'SalesOrders')


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df['Year'] = df['OrderDate'].dt.year
    result = df.groupby(['Year', 'Region'])['Total'].sum()
    return result


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    max_total = df.groupby('Rep')['Total'].sum().max()
    rep_name = df.groupby('Rep')['Total'].sum().idxmax()
    return rep_name, max_total


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    most_sold = df.groupby('Item')['Units'].sum().idxmax()
    num_units = df.groupby('Item')['Units'].sum().max()
    return most_sold, num_units
