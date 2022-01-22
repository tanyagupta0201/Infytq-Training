# Problem Link: https://www.biochemithon.in/python-tutorials/infytq-practice-problem-1-four-digit-otp/

s = input("Enter the string: ")
otp = ""

for i in range(1, len(s), 2):
    sqr = (int)(s[i]) ** 2
    otp += str(sqr)

if len(otp) >= 4:
    print(otp[0: 5])
else:
    print("-1")
