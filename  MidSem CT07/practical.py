# health=100
# import time
# import random
# print("Tim has "+ str(health) +" health")

# while health > 0:
#     health = health - random. randint(1, 15)
#     print("Tim has " + str(health) + " left after exploring a dungeon")
#     time. sleep(1)
# print("Tim died :(")


list=[]

question=input("Would you like to order?")
if question != "no":
    food=input("What would you like to order?")
    list.append(food)
else:
    print(list)
    