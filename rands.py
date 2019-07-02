import random
import sys

x = int(random.random() * 100)

if x > 50:
    print('x =', x)
    print('gr8')
else:
    print('x =', x)
    sys.exit(2)
