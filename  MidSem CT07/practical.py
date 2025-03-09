health=100
x = range(-14,0)
import time
import random
print("Tim has "+ str(health) +" health")

while health > -14:
    health = health - random. randint(1, 15)
    print("Tim has " + str(health) + " left after exploring a dungeon")
    time. sleep(1)
print("Tim died :(")
