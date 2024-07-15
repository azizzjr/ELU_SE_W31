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
        try:
            total = CalculateTotal(self.invalid_cart)
        except TypeError as e:
            total = None
        # Since the original function doesn't handle invalid types, we expect it to raise a TypeError
        self.assertIsNone(total, "CalculateTotal should raise a TypeError for invalid price types")

    def test_display_total(self):
        total = 25.47
        display_message = display_total(total)
        self.assertEqual(display_message, "Total price: " + str(total))

if __name__ == '__main__':
    unittest.main()