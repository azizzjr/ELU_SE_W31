import unittest
from unittest.mock import patch
from shopping_cart import CalculateTotal, display_total

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        self.invalid_cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 'invalid'}
        ]

    def test_calculate_total_valid_cart(self):
        total = CalculateTotal(self.cart)
        self.assertEqual(total, 25.47)

    def test_calculate_total_invalid_cart(self):
        with self.assertRaises(TypeError):
            CalculateTotal(self.invalid_cart)

    def test_display_total(self):
        total = 25.47
        with patch('builtins.print') as mocked_print:
            display_total(total)
            mocked_print.assert_called_with("Total price: 25.47")

if __name__ == '__main__':
    unittest.main()