#<18.5為太輕18.5-23為正常24-26過重27-29輕度肥胖30-34中度肥胖>=35重度肥胖

height = int(input("請輸入身高,單位為(公分):"))
weight = int(input("請輸入體重,單位為(公斤):"))
BMI = weight / (height/100) **2
Level =" "

if BMI < 18.5:
    Level = "太輕"
elif  18.5 <= BMI < 24:
    Level = "正常"
elif 24 <= BMI <27:
    Level = "過重"
elif 27 <= BMI <30:
    Level = "輕度肥胖"
elif 30 <= BMI <34:
    Level ="中度肥胖"
elif BMI >= 35 :
    Level = "重度肥胖"
print(f"BMI為{BMI:.2f}")
print(Level)