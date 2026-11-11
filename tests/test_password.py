import unittest
from validators.password import validate_password

class PasswordTests(unittest.TestCase):
    def test_accepted(self):
        for value in ["Hello@123", "Welcome@1", "Abcd#789", "Pass_word9!", "Qwerty$12"]:
            with self.subTest(value=value):
                self.assertTrue(validate_password(value)[0])

    def test_rejected(self):
        for value in ["hello123", "HELLO@123", "HelloWorld@", "Hi@12", "Hello 123@"]:
            with self.subTest(value=value):
                self.assertFalse(validate_password(value)[0])

if __name__ == "__main__":
    unittest.main()
