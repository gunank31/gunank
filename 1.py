# 1. Print Reverse Number Pyramid
#    Input: 5
#    Output:
#    54321
#    5432
#    543
#    54
#    5

rows =  int(input("Enter number of rows => "))

for i in range(rows):
    for i in range(rows,i,-1):
        print(i, end='' )
    print()  
