#!/usr/bin/python
import psycopg2
from config import config

def get_links():
    """ Query all links in the link table """
    conn = None
    link_list = []
    try:
        # Read database configuration
        params = config()
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        cur = conn.cursor()
        # Select all links, and populate the list
        cur.execute("SELECT url FROM link ORDER BY id")
        row = cur.fetchone()
        while row is not None:
            link_list.append(row[0])
            row = cur.fetchone()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return link_list


def get_number_of_stored_links():
    """ Return the quantity of the link that was stored in the database """
    conn = None
    number_of_links = None
    try:
        # Read database configuration
        params = config()
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        cur = conn.cursor()
        # Select the next non-tracked link
        cur.execute("SELECT COUNT(*) FROM link")
        row = cur.fetchone()
        if row is not None:
            number_of_links = row[0]
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return number_of_links

def mark_link_as_tracked(link_url):
    """ Mark link as tracked """
    sql = """ UPDATE link
                SET tracked = 1
                WHERE url = %s"""
    conn = None
    updated_rows = 0
    try:
        # Read database configuration
        params = config()
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        cur = conn.cursor()
        # Execute the UPDATE  statement
        cur.execute(sql, (link_url,))
        # Get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def get_next_not_tracked_link():
    """ Return the next link that was not tracked yet """
    conn = None
    link_url = None
    try:
        # Read database configuration
        params = config()
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        cur = conn.cursor()
        # Select the next non-tracked link
        cur.execute("SELECT url FROM link WHERE tracked = 0 ORDER BY id")
        row = cur.fetchone()
        if row is not None:
            link_url = row[0]
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return link_url


def insert_link(link_url):
    """ insert a new link into the link table """
    sql = """INSERT INTO link(url, tracked)
             VALUES(%s, 0) RETURNING id;"""
    conn = None
    link_id = None
    try:
        # Read database configuration
        params = config()
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        cur = conn.cursor()
        # Verify existent link URL
        cur.execute("SELECT url FROM link WHERE url = %s ORDER BY id", (link_url,))
        row = cur.fetchone()
        if row is None:
            # Insert a new link URL
            cur.execute(sql, (link_url,))
            # get the generated id back
            link_id = cur.fetchone()[0]
            # Commit the changes to the database
            conn.commit()
        # Close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return link_id


def delete_records():
    """ Delete all records of links in the PostgreSQL database"""
    conn = None
    try:
        # Read the connection parameters
        params = config()
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Delete link table data
        cur.execute("DELETE FROM link")
        # Close communication with the PostgreSQL database server
        cur.close()
        # Commit the changes
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
        # Read connection parameters
        params = config()
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # Create a cursor
        cur = conn.cursor()
        # Execute a statement
        cur.execute('SELECT version()')
        # Close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return_value = False
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return return_value
