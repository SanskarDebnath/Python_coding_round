import time
from itertools import cycle
lights = [
        ('green',2),
        ('Yellow',0.1),
        ('Red', 3)
          ]
colors = cycle(lights)
while True:
    col,sec = next(colors)
    print(col)
    time.sleep(sec)