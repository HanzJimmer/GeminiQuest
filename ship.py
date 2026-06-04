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

    def add_inventory(self, item_name: str, amount: int):
        pass

    def subtract_inventory(self, item_name: str, amount: int):
        pass

    def lose_hull(self, amount: int):
        pass

    def lose_shield(self, amount: int):
        pass

    def repair_hull(self, amount: int):
        pass

    def repair_shield(self, amount: int):
        pass