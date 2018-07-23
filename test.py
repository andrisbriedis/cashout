import unittest

from checkout import CheckOut
from pricing_rules import PricingRules, MissingItem


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
        self.checkout.scan("NON_EXISTING")
        self.assertRaises(MissingItem, self.checkout.total)

    def test_double_item(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.assertEqual(100, self.checkout.total())

    def test_different_skus(self):
        self.checkout.scan("A")
        self.checkout.scan("B")
        self.assertEqual(120, self.checkout.total())

    def test_items_without_special_offers(self):
        self.checkout.scan("B")
        self.assertEqual(70, self.checkout.total())

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

    def test_special_offer_and_mixed_items(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("B")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("B")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.assertEqual(450, self.checkout.total())