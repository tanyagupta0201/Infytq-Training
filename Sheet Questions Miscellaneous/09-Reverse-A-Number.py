def rev(n, r):
    if n == 0:
        return r
    return rev(n // 10, r * 10 + n % 10)


n = int(input("Enter a number: "))
print(rev(n, 0))
