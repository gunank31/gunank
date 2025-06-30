# 10. Count the Number of Factors (excluding arrays)
#     Input: 12
#     Output: 6 (1, 2, 3, 4, 6, 12)


num = int(input("Enter a number =>"))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print("Number of factors =>", count)
