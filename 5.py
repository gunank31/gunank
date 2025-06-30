# 5. Armstrong Number Checker (3-digit)
#    Input: 153 13 + 53 + 33 = 153
#    Output: Armstrong


number = int(input("Enter a 3-digit number =>"))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

armstrong_sum = (hundreds ** 3) + (tens ** 3) + (units ** 3)

if armstrong_sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")
