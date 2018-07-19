from pricing_rules import PricingRules
from checkout import CheckOut, MissingItem
from decimal import Decimal

import unittest


class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.pricing_rules = PricingRules()
        self.checkout = CheckOut(self.pricing_rules)

    def test_sanity(self):
        self.assertEqual(0, self.checkout.total())

    def test_single_item(self):
        self.checkout.scan("A")
        self.assertEqual(50, self.checkout.total())

    def test_non_existent_sku(self):
        self.assertRaises(MissingItem, self.checkout.scan, "NON_EXISTING")

    def test_double_item(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.assertEqual(100, self.checkout.total())

    def test_special_offer(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.assertEqual(130, self.checkout.total())

    def test_special_offer_and_additional_items(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.assertEqual(230, self.checkout.total())
