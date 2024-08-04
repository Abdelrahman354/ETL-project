import pandas as pd
def fix_negatives_zeros(data):
    if data < 0:
        return data * -1
    elif data == 0:
        return pd.NA
    else:
        return data
def transform_data(df):
    
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['InvoiceDate_Date'] = df['InvoiceDate'].dt.date
    df['InvoiceDate_Time'] = df['InvoiceDate'].dt.time
    df['Quantity'] = df['Quantity'].apply(fix_negatives_zeros)
    df['UnitPrice'] = df['UnitPrice'].apply(fix_negatives_zeros)
    df = df.drop(columns=['InvoiceDate'])  
    df=df.drop_duplicates()  
    df= df.dropna()
    df['CustomerID'] = df['CustomerID'].astype(int)

    datetime_dim_data = df[['InvoiceDate_Date', 'InvoiceDate_Time']].drop_duplicates().rename(columns={'InvoiceDate_Date': 'date', 'InvoiceDate_Time': 'time'})
    customer_dim_data = df[['CustomerID', 'Country']].drop_duplicates().rename(columns={'CustomerID': 'customer_id', 'Country': 'country'})
    product_dim_data = df[['StockCode', 'Description']].drop_duplicates().rename(columns={'StockCode': 'stock_code', 'Description': 'description'})
    
    fact_table_data = df[['InvoiceNo', 'StockCode', 'Quantity', 'InvoiceDate_Date', 'InvoiceDate_Time', 'CustomerID', 'UnitPrice']].rename(columns={'InvoiceNo': 'invoice_no', 'StockCode': 'stock_code', 'Quantity': 'quantity', 'CustomerID': 'customer_id', 'UnitPrice': 'unit_price'})
    
    return df,datetime_dim_data, customer_dim_data, product_dim_data, fact_table_data

