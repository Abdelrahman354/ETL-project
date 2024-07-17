from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
def load_data(df, db_url):
    try:
        engine = create_engine(db_url)
        df.to_sql('online_retail', engine, if_exists='replace', index=False)
        print("Data successfully loaded into PostgreSQL.")
    except SQLAlchemyError as e:
        error_msg = str(e.__dict__.get('orig') or e)
        print(f"Error occurred while loading data: {error_msg}")