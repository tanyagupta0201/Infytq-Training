# Problem Link: https://codewindow.in/odd-even-alternating-problem-infytq-2019-solve/

def solve(s):
    odd = []
    even = []
    special_char = 0

    for ch in s:
        if ch.isalnum() == False:
            special_char += 1
        elif ch.isdigit() == True:
            if int(ch) % 2 == 0:
                even.append(ch)
            else:
                odd.append(ch)

    # Check if number of special characters are even or odd.
    # Odd hain toh swap kardi lists kyuki phir pehle odd number se start hoga print hona
    # Agar swap nahi karte toh for loop mein else laga kar 2 baar code likhna padega pehle even ke liye aur phir odd ke liye
    if special_char % 2 != 0:
        odd, even = even, odd

    od = len(odd)
    ev = len(even)
    m = max(od, ev)

    # Abhi zero even aur odd numbers print hue hain
    e = 0
    o = 0

    for i in range(m):
        # Yeh jab tak check hoga tab tak saare even or odd numbers print na ho jaayein
        if e != ev:
            print(even[e], end='')
            e += 1
        if o != od:
            print(odd[o], end='')
            o += 1
    # Next line mein jaane ke liye jab 1 test case khatam ho jaye poora
    print()


# Number of test cases
t = int(input())

while (t):
    s = input()
    solve(s)
    t = t - 1
