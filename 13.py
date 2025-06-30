# 13. Number is a Harshad Number
#     Input: 18 1+8 = 9, 18 0/0 9 O Yes


num = int(input("Enter a number =>"))

digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if digit_sum != 0 and num % digit_sum == 0:
    print("Yes (Harshad Number)")
else:
    print("No (Not a Harshad Number)")
