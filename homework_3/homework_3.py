#下列為根據最低年齡制定電影分級的函式，假設電影分級的規則如下：

# 限制級：18歲或以上皆可欣賞。
#輔導級：13(含) ~ 17歲以上皆可欣賞。
#普遍級：12(含)歲以下皆可欣賞。
#如果沒有輸入年齡預設為普遍級。

age = input("請輸入年齡")
level = ""
if age >= 18:
    level = "限制級"
elif 13 <= age <= 17:
    level = "輔導級"
elif age <=12:
    level = "普遍級"
elif age == "":
    level = "普遍級"
elif age  <= 0:
    level = "普遍級"
print(level)