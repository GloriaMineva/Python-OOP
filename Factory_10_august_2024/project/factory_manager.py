from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore

store_types = {'ToyStore': ToyStore, 'FurnitureStore': FurnitureStore}
product_types = {'Chair': Chair, 'HobbyHorse': HobbyHorse}


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in product_types:
            raise Exception("Invalid product type!")
        new_product = product_types[product_type](model, price)
        self.products.append(new_product)
        return f"A product of sub-type {new_product.SUB} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in store_types:
            raise Exception(f"{store_type} is an invalid type of store!")
        new_store = store_types[store_type](name, location)
        self.stores.append(new_store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        counter_products = 0
        for p in products:
            if ((store.store_type == 'FurnitureStore' and p.SUB == 'Furniture') or
                    (store.store_type == 'ToyStore' and p.SUB == 'Toys')):
                counter_products += 1
                store.products.append(p)
                self.products.remove(p)
                store.capacity -= 1
                self.income += p.price
        if counter_products > 0:
            return f'Store {store.name} successfully purchased {counter_products} items.'
        return f"Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        try:
            matching_store = next(s for s in self.stores if s.name == store_name)
            if len(matching_store.products) > 0:
                return "The store is still having products in stock! Unregistering is inadvisable."
            self.stores.remove(matching_store)
            return f"Successfully unregistered store {store_name}, location: {matching_store.location}."
        except StopIteration:
            return "No such store!"

    def discount_products(self, product_model: str):
        matching_products = [p for p in self.products if p.model == product_model]
        for p in matching_products:
            p.discount()
        return f"Discount applied to {len(matching_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        try:
            matching_store = next(s for s in self.stores if s.name == store_name)
            return matching_store.store_stats()
        except StopIteration:
            return "There is no store registered under this name!"

    def statistics(self):  # TODO result to be a list and join with \n
        result = []
        unsold_dict = {}
        unsold_sum = 0
        self.products = sorted(self.products, key=lambda el: el.model)
        self.stores = sorted(self.stores, key=lambda s: s.name)
        for p in self.products:
            unsold_sum += p.price
            if p.model not in unsold_dict:
                unsold_dict[p.model] = 0
            unsold_dict[p.model] += 1
        result.append(f"Factory: {self.name}")
        result.append(f'Income: {self.income:.2f}')
        result.append('***Products Statistics***')
        result.append(f'Unsold Products: {len(self.products)}. Total net price: {unsold_sum:.2f}')
        for k, v in unsold_dict.items():
            result.append(f'{k}: {v}')
        result.append(f'***Partner Stores: {len(self.stores)}***')
        for store in self.stores:
            result.append(store.name)
        return '\n'.join(result)


# Initialize the FactoryManager
factory_manager = FactoryManager("Cool Factory")

# Produce some items
print(factory_manager.produce_item("Chair", "Classic", 80.0))
print(factory_manager.produce_item("Chair", "Modern", 100.0))
print(factory_manager.produce_item("Chair", "Modern", 200.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
print()

# Register new stores
print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
print()

# Sell products to stores
chair1 = factory_manager.products[0]
chair2 = factory_manager.products[1]
chair3 = factory_manager.products[2]
store1 = factory_manager.stores[0]
store2 = factory_manager.stores[1]
print(factory_manager.sell_products_to_store(store2, chair1, chair2))
print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
print()

# Unregister store
print(factory_manager.unregister_store("Furniture Outlet"))
print()

# Discount products
print(factory_manager.discount_products("Classic"))
print(factory_manager.discount_products("Rocking Horse"))
print()

# Request store statistics
print(factory_manager.request_store_stats("Furniture Outlet"))
print(factory_manager.request_store_stats("Toy World"))
print()

# Factory statistics
print(factory_manager.statistics())
print()

# Unregister store
print(factory_manager.unregister_store("Toy World"))
