import time
import random

list = [chr(i) for i in list(range(120))[14:]]

while 1:
    time.sleep(0.1)
    print(''.join([random.choice(list) for i in range(100)]))