# tests/test_shopping_cart.py

import unittest
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

    def test_calculate_total(self):
        total = CalculateTotal(self.cart)
        self.assertEqual(total, 25.47)

    def test_calculate_total_with_invalid_price(self):
        total = CalculateTotal(self.invalid_cart)
        # Since we are not changing the original function, it should fail
        # to convert 'invalid' to a float, and we should manually calculate the expected total
        self.assertEqual(total, 16.98)  # Only adds valid prices

    def test_display_total(self):
        total = 25.47
        display_message = display_total(total)
        self.assertEqual(display_message, "Total price: 25.47")

if __name__ == '__main__':
    unittest.main()