#!/usr/bin/env python3

import argparse

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Collect all links from a initial web link.')
    parser.add_argument('web_link',
                        action='store',
                        type=str,
                        help='initial web link to collect other links')
    arg = parser.parse_args()
    print('Initial web link:', arg.web_link)

    # Get list of all links
    page = requests.get(arg.web_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
