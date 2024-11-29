from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passanger_car import PassengerCar

vehicle_types = {
    "PassengerCar": PassengerCar,
    "CargoVan": CargoVan,
}


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            matching_user = next(x for x in self.users if x.driving_license_number == driving_license_number)
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in vehicle_types:
            return f"Vehicle type {vehicle_type} is inaccessible."
        try:
            matching_plate_number: BaseVehicle = next(x for x in self.vehicles if x.license_plate_number == license_plate_number)
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            new_vehicle = vehicle_types[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        new_route_id = len(self.routes) + 1
        try:
            matching_route: Route = next(x for x in self.routes if x.start_point == start_point and x.end_point == end_point)
            if matching_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif matching_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif matching_route.length > length:
                matching_route.is_locked = True
                new_route = Route(start_point, end_point, length, new_route_id)
                self.routes.append(new_route)
                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."
        except StopIteration:
            new_route = Route(start_point, end_point, length, new_route_id)
            self.routes.append(new_route)
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        matching_user: User = next(x for x in self.users if x.driving_license_number == driving_license_number)
        if matching_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        matching_vehicle: BaseVehicle = next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles))
        if matching_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        matching_route: Route = next(x for x in self.routes if x.route_id == route_id)
        if matching_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        matching_vehicle.drive(matching_route.length)
        if is_accident_happened:
            matching_vehicle.is_damaged = True
            matching_user.decrease_rating()
        else:
            matching_user.increase_rating()
        return str(matching_vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles: List[BaseVehicle] = [el for el in self.vehicles if el.is_damaged]
        damaged_vehicles = sorted(damaged_vehicles, key=lambda el: (el.brand, el.model))
        if count < len(damaged_vehicles):
            damaged_vehicles = damaged_vehicles[:count]
        for car in damaged_vehicles:
            car.is_damaged = False
            car.recharge()
        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        self.users = sorted(self.users, key=lambda u: -u.rating)
        result = '"*** E-Drive-Rent ***\n'
        for user in self.users:
            result += str(user) + "\n"
        return result

