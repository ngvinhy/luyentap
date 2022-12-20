# hình tam giác vuông cân đáy dưới
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(' *', end='')
    print()

# hình tam giác vuông cân đáy trên
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(' *', end='')
    print()
