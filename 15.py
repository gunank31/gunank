# 15. Find the N-th Digit from the Right
#     Input: 987654, n = 3 Output: 6


num = int(input("Enter a number =>"))
n = int(input("Enter position from right =>"))

for i in range(n - 1):
    num //= 10

nth_digit = num % 10
print("Output =>", nth_digit)
