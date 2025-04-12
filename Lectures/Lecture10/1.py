# Databases

# RDB - Relational Datababases / РБД - Реляционные базы данных  
# RDBMS - Relationial Database Management Systems / СУБД - Системы управления базами данных
# SQL - Structured Query Language (Структурированный язык запросов)

# Except PostgreSQL there are several RDBMS like MySQL, SQLite, etc. 

# PostgreSQL (also known as Postgres) will be used as our RDBMS 

# To start, we need: 
# - Download and install PostgreSQL
# - https://www.w3schools.com/postgresql/postgresql_install.php
# - https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
#   - During installation you can leave everything on default 
#   - !!! Remember/Write down the password that you set during the installation
# - Install psycopg2 module
#   - pip install psycopg2 (or pip3)
#   - or 
#   - pip install psycopg2-binary (or pip3)


# CRUD - Create, Read (Select), Update, Delete 
# CRUD describes 4 main operations with the databases 

# PostgreSQL Syntax :
# https://www.w3schools.com/postgresql/postgresql_create_table.php

import psycopg2 

conn = psycopg2.connect(
    host = 'localhost', 
    dbname = 'PP2', 
    user = 'postgres', 
    password = '1234'
)

# Create a cursor to work with the database 
cur = conn.cursor()

# Querying the database 
cur.execute('Select * from students;')

db_ver = cur.fetchall() 

print(db_ver)