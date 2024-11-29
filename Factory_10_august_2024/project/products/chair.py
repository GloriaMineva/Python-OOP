from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    MATERIAL = 'Wood'
    SUB = 'Furniture'

    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.MATERIAL, self.SUB)

    def discount(self):
        self.price *= 0.9