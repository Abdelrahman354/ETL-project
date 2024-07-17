import pandas as pd

def transform_data(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['InvoiceDate_Date'] = df['InvoiceDate'].dt.date
    df['InvoiceDate_Time'] = df['InvoiceDate'].dt.time
    df = df.drop(columns=['InvoiceDate'])  
    df = df.drop_duplicates()
    df_cleaned = df.dropna()
    return df_cleaned
