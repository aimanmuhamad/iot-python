import pandas as pd
import sqlalchemy
import pymysql

# Create database engine for data.db
engine = create_engine("sqlite:///data.db")

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date,tmax,tmin
  FROM weather;
"""

# Make a dataframe by passing query and engine to read_sql()
temperatures = pd.read_sql(query,engine)

# View the resulting dataframe
print(temperatures)