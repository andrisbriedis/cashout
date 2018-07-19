from pricing_rules import PricingRules

class MissingItem(Exception):
    pass
class CheckOut(object):
    def __init__(self, pricing_rules: PricingRules):
        self.pricing_rules = pricing_rules
        self.items = []
        self.prices = {
            "A": {
                "regular_price": 50,
                "special_offer": {
                    "count": 3,
                    "price": 130
                }
            }
        }


    def scan(self, sku: str) -> None:
        if sku not in self.prices:
            raise MissingItem()
        self.items.append(sku)

    def total(self) -> float:
        item_count = len(self.items)
        total = 0
        if not self.items:
            return 0
        special_offers_count = int(item_count / self.prices['A']['special_offer']['count'])
        total = special_offers_count * self.prices['A']['special_offer']['price']
        total += (item_count % self.prices['A']['special_offer']['count']) * self.prices['A']['regular_price']

        return total
