"""logging test module"""

import unittest
import os.path
from zync import bugger, logger

FILE = os.path.abspath("./.zync.log")


class LoggingTest(unittest.TestCase):
    """logging test class"""

    def test_logging(self):
        """logging test method"""

        # Call the logging functions
        bugger("This is a bugger log.")
        logger("This is a logger log.")

        # Assert that the log file was created
        self.assertTrue(os.path.isfile(FILE))

        # Assert that the log file contains the expected logs
        with open(".zync.log", "r", encoding="utf-8") as file:
            log_contents = file.read()
            self.assertIn("This is a bugger log.", log_contents)
            self.assertIn("This is a logger log.", log_contents)

    def tearDown(self):
        # Clean up the log file after the test
        if os.path.isfile(FILE):
            os.remove(FILE)


if __name__ == "__main__":
    unittest.main()
