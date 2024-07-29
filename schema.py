from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Numeric, ForeignKey, UniqueConstraint, BigInteger,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DateTimeDim(Base):
    __tablename__ = 'datetime_dim'
    datetime_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    __table_args__ = (UniqueConstraint('date', 'time', name='_datetime_uc'),)

class CustomerDim(Base):
    __tablename__ = 'customer_dim'
    customer_id = Column(BigInteger, primary_key=True)
    country = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('customer_id', 'country', name='_customer_uc'),)

class ProductDim(Base):
    __tablename__ = 'product_dim'
    stock_code = Column(String(255), primary_key=True)  
    description = Column(String(255), nullable=False)
    unit_price = Column(Numeric, nullable=False)
    __table_args__ = (UniqueConstraint('stock_code', 'description', 'unit_price', name='_stock_uc'),)

class FactTable(Base):
    __tablename__ = 'fact_table'
    fact_id = Column(Integer, primary_key=True)
    invoice_no = Column(String(255), nullable=False)
    stock_code = Column(String(255), ForeignKey('product_dim.stock_code'), nullable=False)
    quantity = Column(Integer, nullable=False)
    datetime_id = Column(Integer, ForeignKey('datetime_dim.datetime_id'), nullable=False)
    customer_id = Column(BigInteger, ForeignKey('customer_dim.customer_id'), nullable=False)

def create_schema(db_url):
    try:
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        print("Schema created successfully.")
    except Exception as e:
        print(f"Error occurred while creating schema: {e}")
