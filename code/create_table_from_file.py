import pandas as pd
from sqlalchemy import create_engine

# Data Frame
df = pd.read_csv("/home/satriafdt/py/project3/source/users_w_postal_code.csv")

# Connecting to DB using SQLAlchemy
engine = create_engine("postgresql://postgres:Password1234@localhost:5432/dgsproject3")

# Create table 
df.to_sql("users_w_postal_code", engine)
