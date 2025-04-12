# SQL

# CRUD 
# Create - Insert
# Read - Select 
# Update - Update
# Delete - Delete

import psycopg2 

conn = psycopg2.connect(
    host = 'localhost', 
    dbname = 'PP2', 
    user = 'postgres', 
    password = '1234'
)

cur = conn.cursor()

# Delete table 
cur.execute('Drop table orders')
conn.commit()

# Create new table 
cur.execute("""
    Create table students_data (
            name VARCHAR(255), 
            id varchar(50) PRIMARY KEY, 
            study_year INT, 
            phone_number varchar(20)
            )

""")
# Don't forget to commit your changes when you do CREATE or UPDATE or DELETE something in databases
conn.commit()

# Insert some data into the table 
cur.execute("""
    INSERT into students_data(name, id, study_year, phone_number) 
    VALUES ('Talgat', '24BD202224', 1, '+77071234556'), 
           ('Aisha', '24BD145978', 1, '+77055839056');
""")
conn.commit()

# Get students
# cur.execute('Select * from students_data') 
cur.execute('Select name, phone_number, study_year from students_data')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())


# Update students_data
cur.execute("""
    UPDATE students_data
    Set study_year = 2
    where id = '24BD145978';
""")
conn.commit()


# Delete students
cur.execute("""
    Delete from students_data
    where id = '24BD202224'
""")
conn.commit()

# Close connection
cur.close()
conn.close() 

