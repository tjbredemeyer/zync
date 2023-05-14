import unittest
from zync import Slugger, slugger


class SlugifyTest(unittest.TestCase):
    def test_slugify(self):
        string = "This is a TEST!"
        string_Slug = Slugger(string)
        string_slug = slugger(string)

        assert string_Slug == "This-is-a-TEST"
        assert string_slug == "this-is-a-test"


if __name__ == "__main__":
    unittest.main()
