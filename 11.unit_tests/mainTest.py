import unittest
from cardValidator import *
from datetime import *

class CreditCardValidTest(unittest.TestCase):
    def setUp(self) -> None:
        print("Setup")

    def test_validate_card(self):
        result = validateCard(date(2025,2,2))
        self.assertEqual('Valid', result)

    def test_invalid_card(self):
        result = validateCard(date(1994,2,2))
        self.assertEqual('Not valid', result)

    def tearDown(self) -> None:
        print("Teardown")

if __name__== '__main__':
    unittest.main()