# hình đồng hồ cát
n = 5
for i in range(1, n+1):
    for j in range(1, i):
        print("", end=" ")
    for j in range(1, n+2-i):
        print("*", end=" ")
    print()
for i in range(2, n+1):
    for j in range(1, n+1-i):
        print("", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
