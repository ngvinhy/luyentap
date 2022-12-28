def hinh_vuong_rong(h):
    i = 2
    print("*" * h)
    while i <= (h-1):
        print("*"+" "*(h-2)+"*")
        i += 1
    else:
        print("*" * h)


hinh_vuong_rong(5)
