# 2025/05/25
# get repeatable random number
import random 

for i in range(2):
    # Generated random number will be between 1 to 1000 but different in every run.
    print(random.randint(1, 1000))  

for i in range(2):
    # Any number can be used in place of '0'.
    random.seed(42)
    # Generated random number will be between 1 to 1000 but same in every run.
    print(random.randint(1, 1000))