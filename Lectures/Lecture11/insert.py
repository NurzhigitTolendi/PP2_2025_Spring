import psycopg2 
from config import load_config

def insert_vendor(vendor_name):
    # insert a new vendor into the vendors table 
    sql = """
          INSERT INTO vendors(vendor_name)
          VALUES (%s) RETURNING vendor_id;
          """
    
    vendor_id = None
    config = load_config() 

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute insert into table statement
                cur.execute(sql, (vendor_name,))

                rows = cur.fetchone()
                if rows:
                    # print(rows) 
                    vendor_id = rows[0] 

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 

    finally:
        return vendor_id 
    

def insert_many_vendors(vendor_list):
    # insert multiple vendors into the vendors table 
    sql = "INSERT INTO vendors (vendor_name) VALUES (%s);"
    config = load_config()

    rows = [] 

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, vendor_list)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        return rows
    
if __name__ == '__main__':
    insert_vendor("3M Co.")

    insert_many_vendors(
        [
            ('AKM Semiconductor Inc.', ), 
            ('Asahi Glass Co.', ), 
            ('Daikin Industries Inc.', ), 
            ('Samruk Kazyna Co.', ), 
            ('Astana Motors Inc.', ), 
            ('Chevron Inc.', ), 
            ('Dynacast International Inc.', )
        ]
    )


