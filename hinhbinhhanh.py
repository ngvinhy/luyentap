def binh_hanh(h):
   for i in range(1, h + 1):
      print('* ' * i)
   for i in range(1, h):
      print('  ' * i + '* ' * (h - i))


binh_hanh(5)
