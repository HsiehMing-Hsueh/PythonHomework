"""
撰寫一個大樂透電腦自動選號程式  程式執行會以亂數的方式顯示1-49之間七個不重複的大樂透號碼
請輸入本期大樂透電腦選號的組數:10
"""

import random

def LOTTLO(numbers):
    numbers = list()
    while(len(numbers) <= 6):
        LT = random.randint(1,50)
        numbers.append(LT)
    return numbers
    
serice = int(input("請輸入本期大樂透點腦選號組數:"))
serice_num = 0
for i in range(serice):
    if serice > 1:
        serice_num += 1
        number = LOTTLO(serice)       
        print(f"第{serice_num}組號碼為:")
        lots = list(number)
        SP =lots.pop()
        for targe in lots:
            print(targe,end="\n")
        print(f"特別號:{SP}")
    else:
        break
print("祝你中獎,程式結束")