health=100
import time
import random
print("Tim has "+ str(health) +" health")

while health > -1:
    health = health - random. randint(1, 15)
    print("Tim has " + health + "left after exploring a dungeon")
    time. sleep(1)
print("Tim died :(")
