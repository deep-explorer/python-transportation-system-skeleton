from enum import Enum

VehicleStatus = Enum(
    'VehicleStatus', ['free', 'busy', 'loading', 'not_working'])


class Vehicle():
    csv_path = 'database/vehicle.csv'

    def __init__(self, max_capacity, capacity_left_per_kg, capacity_left_per_item, current_position, current_status: VehicleStatus) -> None:
        self.max_capacity = max_capacity
        self.capacity_left_per_kg = capacity_left_per_kg
        self.capacity_left_per_item = capacity_left_per_item
        self.current_position = current_position
        self.current_status = current_status
