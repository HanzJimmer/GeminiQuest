from constants import *
from enum import Enum
import random

class Role(Enum):
    CAPTAIN = 1
    MEDIC = 2
    ENGINEER = 3
    STANDARD = 4

    #each crew will need name, role, health , hunger
        #add currency to buy initial supplies later; for now, just initialize with spare parts

class Person():
    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.health = MAX_CREW_HEALTH
        self.hunger = MAX_HUNGER

    def lose_health(self, amount: int):
        self.health -= amount
        if (self.health <= 0): {
            self.kill() #kill character
        }

    def heal(self, amount: int):
        self.health = min(self.health + amount, MAX_CREW_HEALTH)

    def passive_hunger(self):
        self.hunger = max(self.hunger - 1, 0)
        if (self.hunger <= 0): {
            self.lose_health(1)
        }
    
    def eat(self):
        self.hunger = min(self.hunger + 1, MAX_HUNGER)
        return
    
def new_crew():
    crew_list = {}
    for role in range(1, 5):
        crew_list.add(Person(f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}", Role(role)))
    return crew_list
