health=100
import time
import random
print("Tim has "+ str(health) +" health")

while health > 0:
    health = health - random. randint(1, 15)
    print("Tim has " + str(health) + " left after exploring a dungeon")
    time. sleep(1)
print("Tim died :(")


list=[]
food= input("What would you like to order?")
while food != "end":
    print(food)
    list.append(food)
    