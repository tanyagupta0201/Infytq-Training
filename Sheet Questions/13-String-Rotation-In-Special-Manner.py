# Problem Link: https://codeofgeeks.com/string-rotation-in-special-manner/

def rotate(s3, n):
    n = list(str(n))
    s = 0  # to store sum

    for i in n:
        s += int(i) ** 2

    if s % 2 == 0:
        return s3[-1:] + s3[:-1]  # Right Rotation
    else:
        return s3[2:] + s3[:2]    # Left Rotation


s = input().split(",")  # take input

num = []  # to store number part
s1 = []   # to store string part

for i in s:
    s2, n = i.split(':')
    s1.append(s2)    # s1 = ['abcde', 'pqr']
    num.append(n)    # num = ['123', '45']

for i in range(len(num)):
    print(rotate(s1[i], num[i]))
