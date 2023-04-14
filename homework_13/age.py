import datetime
s = input("------>")
birthday = datetime.date(int(s[0:4]),int(s[5:7]),int(s[8:]))
Now = datetime.datetime.today().date()
print(birthday)
print(Now)
age_day = Now - birthday
print(age_day)
print(type(age_day))
delta = datetime.date(1,1,1) + (age_day)
age = int(delta[0:4])


print(delta)
print(type(delta))
print(age)
print(type(age))