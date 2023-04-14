#讓使用者輸入成績, 若成績在90分以上就顯示「優等」, 80-89分顯示「甲等」，70-79分顯示「乙等」，60-69分顯示「丙等」，60分以下顯示「丁等」。
scores = int(input("請輸入成績:"))


print(f"請輸入成績(0-100):{scores}")
if (scores >= 90 ):
    print("優等")
else:
    if(scores >= 80):
        print("甲等")
    else:
        if(scores >= 70):
            print("乙等")
        else:
            if(scores >=60):
                print("丙等")
            else:
                print("丁等")    