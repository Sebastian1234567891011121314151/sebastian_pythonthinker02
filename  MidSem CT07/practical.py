health=100
import time
print("Tim has "+ str(health) +" health")

while health != 0:
    for i in range(1,15):
        health = health - i
    print(health)
    time. sleep(1)
