import psycopg2 

conn = psycopg2.connect(
    host = 'localhost', 
    dbname = 'PP2', 
    user = 'postgres', 
    password = '1234'
)

cur = conn.cursor()

# Create table 
cur.execute("""
Create table orders (
    id serial primary key, 
    name varchar(100), 
    price numeric        
            )
            """)

conn.commit()

print('Table created successfully!')

# Closing connection 
cur.close()
conn.close() 