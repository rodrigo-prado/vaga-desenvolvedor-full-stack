#!/usr/bin/env python3

import argparse

import requests
from bs4 import BeautifulSoup
from validator_collection import checkers

def get_list_of_all_links(web_link, history_links):
    if (checkers.is_url(web_link) and web_link not in history_links):
        # Add the link to the history
        history_links.append(web_link)

        page = requests.get(web_link)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Get all links
        href_links = [href.get('href') for href in soup.find_all('a')]

        # Print all links found
        for link in href_links:
            print(link)

        # Get links from referenced links
        for link in href_links:
            get_list_of_all_links(link, history_links)


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Collect all links from a initial web link.')
    parser.add_argument('web_link',
                        action='store',
                        type=str,
                        help='initial web link to collect other links')
    arg = parser.parse_args()
    print('Initial web link:', arg.web_link)

    history_links = []
    get_list_of_all_links(arg.web_link, history_links)
