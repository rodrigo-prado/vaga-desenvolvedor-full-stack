#!/usr/bin/env python3

import sys
import argparse
# import psycopg2
import requests
from bs4 import BeautifulSoup
from validator_collection import checkers
from database import verify_connection, delete_records, insert_link, get_next_not_tracked_link, \
    mark_link_as_tracked, get_number_of_stored_links

def get_next_web_url():
    """
    This function is responsible for get the next link and mark the link as tracked in the database
    """
    web_link = get_next_not_tracked_link()
    if web_link is not None:
        mark_link_as_tracked(web_link)

    return web_link


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Collect all links from a initial web link.')
    parser.add_argument('web_link',
                        action='store',
                        type=str,
                        help='initial web link to collect other links')
    parser.add_argument('--limit',
                        action='store',
                        type=int,
                        default=100,
                        help='a limit to avoid endless search for links (default to 100)')
    arg = parser.parse_args()

    # Check if the initial web link is valid; if not, terminate
    if not checkers.is_url(arg.web_link):
        print('Initial web link is not valid!')
        sys.exit(1)

    # Check if the database connection is OKay; if not, terminate
    if not verify_connection():
        print('Database connection problem!')
        sys.exit(1)

    # Initializing link table
    print('Deleting old records.')
    delete_records()
    print('Inserting initial web link:', arg.web_link)
    insert_link(arg.web_link)

    web_link = get_next_web_url()
    print(web_link)
    # history_links = []
    while web_link is not None:
        page = requests.get(web_link)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Get all links
        href_links = [href.get('href') for href in soup.find_all('a')]

        for link in href_links:
            if checkers.is_url(link):
                link_id = insert_link(link)
                if link_id is not None:
                    print('Web link:', link, 'inserted')

        # Get next link to collect new links
        web_link = get_next_web_url()

        # Check if the number of stored link is bigger then limit; if yes break the loop
        if get_number_of_stored_links() > arg.limit:
            break
