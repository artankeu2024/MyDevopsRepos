import random
import math

health = 50 

difficulty = 1

potion_health = int(random.randint(25,50)/difficulty)

health2 = health + potion_health


print(health2)