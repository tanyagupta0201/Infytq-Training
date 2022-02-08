
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


a = int(input("Enter base: "))
n = int(input("Enter power: "))

print(power(a, n))
