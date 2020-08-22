#!/usr/bin/python
import psycopg2
from config import config

def delete_records():
    """ Delete all records of links in the PostgreSQL database"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # delete link table data
        cur.execute("DELETE FROM link")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def verify_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    return_value = True
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return_value = False
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return return_value


if __name__ == '__main__':
    verify_connection()
