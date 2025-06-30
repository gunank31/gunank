# 2. Sum of Digits Until Single Digit
#    Input: 9875 9+8+7+5 = 29 2+9 = 11 1+1 = 2
#    Output: 2


num = int(input("Enter number =>"))

for i in range(100):
    singledigit=0
    for digit in str(num):
        singledigit += int (digit)
    num = singledigit
    if num < 10:
        break
print("Output =>",num )
