from typing import List, Dict


class Shop:
    def __init__(self, name: str, location: tuple, products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_purchase_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                product_cost = round(self.products[product] * quantity, 2)
                total_cost += product_cost

        return round(total_cost, 2)

    def is_product_available(self, product_cart: Dict[str, int]) -> bool:
        for product, quantity in product_cart.items():
            if product not in self.products or self.products[product] < quantity:
                return False
        return True