from pricing_rules import PricingRules

class CheckOut(object):
    def __init__(self, pricing_rules: PricingRules):
        self.pricing_rules = pricing_rules
        self.items = {}

    def scan(self, sku: str) -> None:
        self.items[sku] = self.items.get(sku, 0) + 1

    def total(self) -> float:
        if not self.items:
            return 0

        total = 0
        for sku, count in self.items.items():
            total += self.pricing_rules.get(sku, count)
        return total
