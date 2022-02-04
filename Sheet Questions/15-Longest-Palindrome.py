# Problem Link: https://meganaukri.com/infytq-exam-questions/

# Input a string
s = input()

# Generate all possible substrings and store them into a list
list = [s[i: j + 1] for i in range(len(s)) for j in range(len(s))]

l = 0
out = ""  # to store the longest palindrome string

# Check for each substring present in list
for i in list:
    rev = i[:: -1]
    if i == rev and len(i) > l:
        l = len(i)
        out = i

print(out)
