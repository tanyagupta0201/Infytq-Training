# Problem Link: https://codewindow.in/add-and-concatenate-infytq-2019-solve/

list = input().split(',')
l = len(list)

sum1 = 0
sum2 = ''

idxFive = list.index('5')
idxEight = list.index('8')

for i in range(0, l):
    if i < idxFive or i > idxEight:
        sum1 += int(list[i])

for i in range(idxFive, idxEight + 1):
    sum2 += ''.join(list[i])

print(sum1 + int(sum2))
