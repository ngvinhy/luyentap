def binh_hanh(h):
    for i in range(1, h + 1):
        print('*' * i)
    for i in range(1, h):
        print(' ' * i + '*' * (h - i))


binh_hanh(5)


def binh_hanh_rong(h):
    print('*')
    for i in range(2, h):
        print('*' + ' ' * (i - 2) + '*')
    print('*' * (h * 2 - 1))
    for i in range(h, h * 2 - 2):
        print(' ' * i + '*' + ' ' * (h * 2 - i - 3) + '*')
    print(' ' * (h * 2 - 2) + '*')


binh_hanh_rong(5)
