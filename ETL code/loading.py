from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import DateTimeDim, CustomerDim, ProductDim, FactTable

def load_data(db_url, datetime_dim_data, customer_dim_data, product_dim_data, fact_table_data):
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:

        datetime_dim_objects = [DateTimeDim(date=row['date'], time=row['time']) for index, row in datetime_dim_data.iterrows()]
        session.bulk_save_objects(datetime_dim_objects)
        session.commit()


        for index, row in customer_dim_data.iterrows():
            customer_dim_object = CustomerDim(customer_id=row['customer_id'], country=row['country'])
            session.merge(customer_dim_object)
        session.commit()


        for index, row in product_dim_data.iterrows():
            product_dim_object = ProductDim(stock_code=row['stock_code'], description=row['description'])
            session.merge(product_dim_object)
        session.commit()


        datetime_dim_map = session.query(DateTimeDim).all()
        datetime_dim_map_dict = {(item.date, item.time): item.datetime_id for item in datetime_dim_map}
        fact_table_data['datetime_id'] = fact_table_data.apply(lambda row: datetime_dim_map_dict[(row['InvoiceDate_Date'], row['InvoiceDate_Time'])], axis=1)


        fact_table_objects = [FactTable(invoice_no=row['invoice_no'], stock_code=row['stock_code'], quantity=row['quantity'], datetime_id=row['datetime_id'], customer_id=row['customer_id'], unit_price=row['unit_price']) for index, row in fact_table_data.iterrows()]
        session.bulk_save_objects(fact_table_objects)
        session.commit()
        
        print("Data successfully loaded into PostgreSQL.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()