#Army Game
import math

n, m = [int(c) for c in input().split()]
print(int(math.ceil(n/2) * int(math.ceil(m/2))))
