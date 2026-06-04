from constants import *
from enum import Enum

class Role(Enum):
    CAPTAIN = 1
    MEDIC = 2
    ENGINEER = 3
    STANDARD = 4

    #each crew will need name, role, health (initialize to 10?), hunger (initialize to 10?)
        #add currency to buy initial supplies later; for now, just initialize with spare parts

class Person():
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.health = MAX_CREW_HEALTH
        self.hunger = MAX_HUNGER

    def lose_health(self, amount: int):
        pass

    def heal(self, amount: int):
        pass

    def passive_hunger(self):
        self.hunger -= 1
        return
    
    def eat(self):
        self.hunger += 1
        return