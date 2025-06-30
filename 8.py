# 8. Find First Digit of a Number
#    Input: 9832
#    Output: 9


number = int(input("Enter a number =>"))

while number >= 10:
    number = number // 10

print("First digit =>", number)
