#!/usr/bin/env python3

import os
import unittest
from database import get_links

class collectAllLinksTestCase(unittest.TestCase):
    """
    Unit test for the Collect All Links

    Verify that the first link record is the same that was passed as argument.
    """
    def test_runCollectAllLinks(self):
        """[SUCCESS] RUN APPLICATION."""
        os.system('python3 src/collect_all_links.py https://blog.acolyer.org/')
        links = get_links()
        self.assertEqual(links[0], 'https://blog.acolyer.org/')


if __name__ == "__main__":
    unittest.main()
