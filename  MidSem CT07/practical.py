health=100
import time
import random
print("Tim has "+ str(health) +" health")

while health != 0:
    health = health - random. randint(1, 15)
    print(health)
    time. sleep(1)
