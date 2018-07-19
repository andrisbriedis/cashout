from pricing_rules import PricingRules
from checkout import CheckOut
from decimal import Decimal

import unittest


class CheckoutTest(unittest.TestCase):
    def test_sanity(self):
        rules = PricingRules()
        checkout = CheckOut(rules)
        self.assertEqual(Decimal(0), checkout.total())