# Problem Link: https://www.geeksforgeeks.org/infytq-2019-find-the-position-from-where-the-parenthesis-is-not-balanced/

st = []
open = ['(', '{', '[']
close = [')', '}', ']']


def check(s):
    # Agar first character hi closing bracket hai toh return index + 1 which is 1
    if(s[0] in close):
        return 1

    for i in range(len(s)):
        # Agar opening bracket hai toh append kardo
        if s[i] in open:
            st.append(s[i])
        # Closing bracket hai toh wo closing bracket close mein kis index par aa rha tha wo ek variable mein store kara diya
        elif s[i] in close:
            last = close.index(s[i])

            # Jo closing bracket aaya hai abhi agar uski ek position pehle uski ka opening bracket hua toh match ho gaya, toh pop kardo
            if(len(st) > 0) and (open[last] == st[len(st) - 1]):
                st.pop()
            else:
                # Agar uski matching ka opening bracket nahi toh wahin par mismatch ho gya toh index + 1 return kardo
                return i + 1

    # Poori string traverse karne ke baad
    # agar st ki length 0 aa rahi hai matlab balanced hai string toh return 0
    if len(st) == 0:
        return 0
    else:
        # Agar length 0 nahi hai toh ussi position par hi closing bracket hai jo ki mismatch hai, toh string ki length + 1
        return len(s) + 1


# Taking input
s = input()
print(check(s))
