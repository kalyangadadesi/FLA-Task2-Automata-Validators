import unittest
from validators.atm_pin import validate_pin

class PinTests(unittest.TestCase):
    def test_accepted(self):
        for value in ["1234", "5678", "0000", "9081", "2468"]:
            with self.subTest(value=value):
                self.assertTrue(validate_pin(value)[0])

    def test_rejected(self):
        for value in ["123", "12345", "12a4", "12 4", ""]:
            with self.subTest(value=value):
                self.assertFalse(validate_pin(value)[0])

if __name__ == "__main__":
    unittest.main()
