from pricing_rules import PricingRules
from decimal import Decimal


class CheckOut(object):
    def __init__(self, pricing_rules: PricingRules):
        self.pricing_rules = pricing_rules

    def scan(self, sku: str) -> None:
        pass

    def total(self) -> Decimal:
        return Decimal(0)

