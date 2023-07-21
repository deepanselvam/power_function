def pow(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a
    return pow(a, b // 2, c)

a = int(input())
b = int(input())
c = int(input())
print(pow(a, b, c))
