import psycopg2
from config import load_config

def create_proc():
    """ Create procedures in the PostgreSQL database"""
    commands = (
        """
        CREATE OR REPLACE PROCEDURE add_new_part(
            new_part_name varchar,
            new_vendor_name varchar
        ) 
        AS $$
        DECLARE
            v_part_id INT;
            v_vendor_id INT;
        BEGIN
            -- insert into the parts table
            INSERT INTO parts(part_name) 
            VALUES(new_part_name) 
            RETURNING part_id INTO v_part_id;
            
            -- insert a new vendor
            INSERT INTO vendors(vendor_name)
            VALUES(new_vendor_name)
            RETURNING vendor_id INTO v_vendor_id;
            
            -- insert into vendor_parts
            INSERT INTO vendor_parts(part_id, vendor_id)
            VALUES(v_part_id,v_vendor_id);
            
        END;
        $$
        LANGUAGE PLPGSQL;      
        """,
        )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_proc()