
def power(a, n):
    if n == 0:
        return 0

    if a == 0:
        return 0

    if n % 2 == 0:
        return power(a * a, n / 2)
    else:
        return a * power(a * a, n / 2)


a = int(input("Enter base: "))
n = int(input("Enter power: "))

print(power(a, n))
