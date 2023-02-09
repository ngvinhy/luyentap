from math import sqrt, pow
def tinh(m,n,a,b):
    s1 = s2 = 0
    for i in range(m,n+1):
        c = True if sqrt(i) % 1 == 0 else False
        if c:
            if a<=i<=b and i% 2 == 0:
                continue
            else:
                s1 +=i
        else:
            for j in range (1,i):
                if i%j==0 and j%2 == 0:
                    s2 +=j
    return s1,s2
print(tinh(1,2,3,4))