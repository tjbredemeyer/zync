"""sluggging test module"""

import unittest
from zync import Slugger, slugger


class SlugifyTest(unittest.TestCase):
    """slugging test class"""

    def test_slugify(self):
        """slugging test method"""
        string = "This is a TEST!"
        slug1 = Slugger(string)
        slug2 = slugger(string)

        assert slug1 == "This-is-a-TEST"
        assert slug2 == "this-is-a-test"


if __name__ == "__main__":
    unittest.main()
