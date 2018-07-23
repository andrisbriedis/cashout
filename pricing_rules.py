
class MissingItem(Exception):
    pass

class PricingRules(object):
    def __init__(self):
        self.prices = {
            "A": {
                "regular_price": 50,
                "special_offer": {
                    "count": 3,
                    "price": 130
                }
            },
            "B": {
                "regular_price": 70,
            }
        }

    def get(self, sku: str, quantity: int):
        if sku not in self.prices:
            raise MissingItem()
        prices = self.prices[sku]

        total = 0
        if 'special_offer' in prices:
            special_offer = prices['special_offer']
            special_offers_count = int(quantity / special_offer['count'])
            total = special_offers_count * special_offer['price']
            quantity = (quantity % special_offer['count'])
        total += quantity * prices['regular_price']
        return total
