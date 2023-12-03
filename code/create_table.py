import psycopg2

# Connecting to PostgreSQL
conn = psycopg2.connect("host=localhost dbname=dgsproject3 user=postgres password=Password1234")

# Using Cursor
cur = conn.cursor()

# Create Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    email text,
    name text,
    phone text,
    postalZip text
    )
""")

# Commit
conn.commit()