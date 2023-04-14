print("請輸入2個數,求2數之公因數")
n = int(input("請輸入第1個數:"))
m = int(input("請輸入第2個數:"))
if n > m:
    x = n
else:
    x = m
for y in range(2,x):
    if n % y == 0 and m % y == 0:
        print(y)

