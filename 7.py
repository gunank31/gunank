# 7. Create a Pattern Without Using Arrays
#    Input: 4
#    Output:
#    1
#    12
#    123
#    1234


n = int(input("Enter a number =>"))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
