#!/usr/bin/env python3

import argparse
import psycopg2
import requests
from bs4 import BeautifulSoup
from validator_collection import checkers
from database import verify_connection

def get_list_of_all_links(web_link, history_links, max_links):
    """
    This function is responsible for get the list of the links, store, and search for more links.
    """
    if (checkers.is_url(web_link) and web_link not in history_links):
        print(web_link)

        # Add the link to the history
        history_links.append(web_link)

        if (len(history_links) >= max_links):
            return

        page = requests.get(web_link)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Get all links
        href_links = [href.get('href') for href in soup.find_all('a')]

        # Print all links found
        # for link in href_links:
        #     print(link)

        # Get links from referenced links
        for link in href_links:
            get_list_of_all_links(link, history_links, max_links)


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Collect all links from a initial web link.')
    parser.add_argument('web_link',
                        action='store',
                        type=str,
                        help='initial web link to collect other links')
    parser.add_argument('--max-links',
                        action='store',
                        type=int,
                        default=100,
                        help='max number of links (default to 100)')
    arg = parser.parse_args()
    print('Initial web link:', arg.web_link)

    if (verify_connection()):
        print('Database connection is OKay!')
        history_links = []
        get_list_of_all_links(arg.web_link, history_links, arg.max_links)
    else:
        print('Database connection problem!')
