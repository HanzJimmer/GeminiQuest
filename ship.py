from constants import *

class Ship():
    #also initialize the ship health, shields, and inventory
        #add ammunition later for more difficult version? or even weapon types?)
        #add ability to specify beginning supplies

    def __init__(self, crew:list):
        self.crew = crew
        self.ship_health = MAX_SHIP_HEALTH
        self.ship_shields = MAX_SHIP_SHIELDS_1
        self.ship_inventory = {"spare_parts" : 2, "fuel" : 100, "food" : 20}
        self.distance_remaining = DISTANCE_TO_GEMINI

    def __str__(self):
        return (f"Ship health: {self.ship_health}\nShields: {self.ship_shields}\nDistance to Gemini: {self.distance_remaining} "
                f"lightyears\nShip Inventory: {self.get_inventory()}")

    def get_inventory(self):
        inventory = ""
        for item in self.ship_inventory:
            inventory += f"\n\t-{item}: {self.ship_inventory[item]}"
        return inventory

    def add_inventory(self, item_name: str, amount: int):
        if item_name in self.ship_inventory:
            self.ship_inventory[item_name] += amount

    def subtract_inventory(self, item_name: str, amount: int):
        if item_name in self.ship_inventory:
            self.ship_inventory[item_name] -= amount

    def lose_hull(self, amount: int):
        self.ship_health -= amount
        if self.ship_health <= 0: {
            self.kill()
        }

    def lose_shield(self, amount: int):
        self.ship_shields = max(self.ship_shields - amount, 0)

    def repair_hull(self, amount: int):
        self.ship_health = min(self.ship_health + amount, MAX_SHIP_HEALTH)

    def repair_shield(self, amount: int):
        self.ship_shields = min(self.ship_shields + amount, MAX_SHIP_SHIELDS_1)

    def ship_to_json(self):
        