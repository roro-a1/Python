# Randomisation
import random

"""
random_int = random.randint(1, 10)
print(random_int)
"""
"""
random_num = random.random()
print(random_num)
"""
"""
random_float = random.uniform(1, 10)
print(random_float)
"""

random_int = random.randint(0, 1)
if random_int == 0:
    print("Heads")
else:
    print("Tails")