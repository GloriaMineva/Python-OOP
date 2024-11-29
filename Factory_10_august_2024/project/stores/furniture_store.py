from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 50)
        self.dict_products = {}

    @property
    def store_type(self):
        return 'FurnitureStore'

    # def store_stats(self):
    #     result = ''
    #     self.products = sorted(self.products, key=lambda p: p.model)
    #     result += f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
    #     estimated_profit = self.get_estimated_profit().split(' ')[-1]
    #     result += f'Estimated future profit for {len(self.products)} products is {estimated_profit}\n'
    #     result += '**Furniture for sale:\n'
    #
    #     for product in self.products:
    #         if product.model not in self.dict_products:
    #             self.dict_products[product.model] = []
    #         self.dict_products[product.model].append(product.price)
    #     for k, v in self.dict_products.items():
    #         result += f'{k}: {len(v)}pcs, average price: {(sum(v)/ len(v)):.2f}'
    #     return result

    def store_stats(self):
        result = []
        self.products = sorted(self.products, key=lambda p: p.model)
        result.append(f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}")
        estimated_profit = self.get_estimated_profit().split(' ')[-1]
        result.append(f'Estimated future profit for {len(self.products)} products is {estimated_profit}')
        result.append('**Furniture for sale:')

        for product in self.products:
            if product.model not in self.dict_products:
                self.dict_products[product.model] = []
            self.dict_products[product.model].append(product.price)
        for k, v in self.dict_products.items():
            result.append(f'{k}: {len(v)}pcs, average price: {(sum(v)/ len(v)):.2f}')
        return '\n'.join(result)