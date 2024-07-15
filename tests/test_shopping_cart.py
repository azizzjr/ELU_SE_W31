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

    @patch('shopping_cart.CART', [
        {'name': 'Item A', 'price': 10.99},
        {'name': 'Item B', 'price': 5.99},
        {'name': 'Item C', 'price': 8.49}
    ])
    def test_calculate_total(self, mock_cart):
        total = CalculateTotal(mock_cart)
        self.assertEqual(total, 25.47)

    @patch('shopping_cart.CART', [
        {'name': 'Item A', 'price': 10.99},
        {'name': 'Item B', 'price': 5.99},
        {'name': 'Item C', 'price': 'invalid'}
    ])
    def test_calculate_total_with_invalid_price(self, mock_cart):
        with self.assertRaises(TypeError):
            CalculateTotal(mock_cart)

    def test_display_total(self):
        total = 25.47
        display_message = display_total(total)
        self.assertEqual(display_message, "Total price: " + str(total))

if __name__ == '__main__':
    unittest.main()