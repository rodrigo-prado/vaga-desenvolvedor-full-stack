#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Collect all links from a initial web link.')
    parser.add_argument('web_link',
                        action='store',
                        type=str,
                        help='initial web link to collect other links')
    arg = parser.parse_args()
    print('Initial web link:', arg.web_link)
