import unittest
from validators.email import validate_email

class EmailTests(unittest.TestCase):
    def test_accepted(self):
        for value in ["student@gmail.com", "abc@yahoo.in", "ronav.js+fla@example.org",
                      "a_b-9@sub.domain.co", "first.last@college.edu"]:
            with self.subTest(value=value):
                self.assertTrue(validate_email(value)[0])

    def test_rejected(self):
        for value in ["@gmail.com", "abc@gmail", "abc@@gmail.com",
                      "a..b@gmail.com", "abc@-gmail.com"]:
            with self.subTest(value=value):
                self.assertFalse(validate_email(value)[0])

if __name__ == "__main__":
    unittest.main()
