import psycopg2, csv

# Connecting to PostgreSQL
conn = psycopg2.connect("host=localhost dbname=dgsproject3 user=postgres password=Password1234")

# Using Cursor
cur = conn.cursor()

# Read csv File
with open("/home/satriafdt/py/project3/source/users_w_postal_code.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO users (email, name, phone, postalZip) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
            row
        )

# Commit
conn.commit()