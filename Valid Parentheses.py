def isValid(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return False if len(s) != 0 else True


chuoi = str(input())
print(isValid(chuoi))
