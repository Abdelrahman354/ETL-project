# ETL Pipeline Project

## Overview
This project demonstrates the implementation of an ETL (Extract, Transform, Load) pipeline using PostgreSQL, Python, Docker, and Power BI. The primary goal is to extract data from multiple CSV sources, transform it for consistency and quality, and load it into a PostgreSQL data warehouse. The data is then visualized in Power BI for insightful analysis.

## Project Architecture

### 1. Data Extraction
- *Source*: Multiple CSV files containing raw data.
- *Script*: extraction.py
  - Handles the extraction of data from CSV files.

### 2. Data Transformation
- *Script*: transform.py
  - Processes the extracted data, ensuring it's clean and ready for loading. This includes data cleaning, normalization, and enrichment.

### 3. Data Loading
- *Script*: load.py
  - Loads the transformed data into the PostgreSQL database.

### 4. Database Schema
- *Schema Script*: schema.py
  - Defines the schema for the data warehouse, including tables like CustomerDim, ProductDim, FactTable, and DateTimeDim.
- *Star Schema Design*: The schema follows a star schema model, which organizes data into fact and dimension tables. This design optimizes complex queries and improves performance.

### 5. Main Jupyter Notebook
- *Integration*: main.ipynb
  - Orchestrates the entire ETL process by calling the extraction, transformation, and loading scripts.

### 6. Data Storage
- *Database*: The processed data is stored in a PostgreSQL database.

### 7. Infrastructure
- *Containerization*: Docker is used to containerize the application, ensuring consistency across different environments. Docker Compose manages two services: PostgreSQL and Jupyter.

### 8. Data Visualization
- *Visualization Tool*: Power BI
  - The data is visualized using Power BI, connected directly to the PostgreSQL server running in a Docker container on a VM. This setup allows for real-time data updates and seamless interaction with the dataset.
