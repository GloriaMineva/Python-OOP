from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter

valid_types_waiters = {'FullTimeWaiter': FullTimeWaiter, 'HalfTimeWaiter': HalfTimeWaiter}
valid_types_clients = {'RegularClient': RegularClient, 'VIPClient': VIPClient}


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in valid_types_waiters:
            return f"{waiter_type} is not a recognized waiter type."
        try:
            existing_waiter = next(w for w in self.waiters if w.name == waiter_name)
            return f"{waiter_name} is already on the staff."
        except StopIteration:
            new_waiter = valid_types_waiters[waiter_type](waiter_name, hours_worked)
            self.waiters.append(new_waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in valid_types_clients:
            return f"{client_type} is not a recognized client type."
        try:
            existing_client = next(c for c in self.clients if c.name == client_name)
            return f"{client_name} is already a client."
        except StopIteration:
            new_client = valid_types_clients[client_type](client_name)
            self.clients.append(new_client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            matching_waiter = next(w for w in self.waiters if w.name == waiter_name)
            return matching_waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            matching_client = next(c for c in self.clients if c.name == client_name)
            points_earned = matching_client.earning_points(order_amount)
            return f"{client_name} earned {points_earned} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        try:
            existing_client = next(c for c in self.clients if c.name == client_name)
            discount_percentage, remaining_points = existing_client.apply_discount()
            return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        self.waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)
        total_earnings = 0
        for waiter in self.waiters:
            total_earnings += waiter.calculate_earnings()
        total_client_points = 0
        for client in self.clients:
            total_client_points += client.points
        result = ["$$ Monthly Report $$"]
        result.append(f'Total Earnings: ${total_earnings:.2f}')
        result.append(f'Total Clients Unused Points: {total_client_points}')
        result.append(f'Total Clients Count: {len(self.clients)}')
        result.append('** Waiter Details **')
        for waiter in self.waiters:
            result.append(str(waiter))
        return '\n'.join(result)
