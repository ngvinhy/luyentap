import math
n = 4
s = math.sqrt(n)
for i in range(n-1, 0, -1):
    s = math.sqrt(s + i)
print(s)
