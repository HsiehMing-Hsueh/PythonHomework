# 判斷星座
birthValue =input("--------->")
birth_mo_day = int(birthValue[5:7]), int(birthValue[8:])
star_sign =""
if birth_mo_day[0] == 3 and birth_mo_day[1] <= 20:
    star_sign = "雙魚座（Pisces）02/20~3/20"
if birth_mo_day[0] == 2 and birth_mo_day[1] >= 20:
    star_sign = "雙魚座（Pisces）02/20~3/20"
if birth_mo_day[0] == 4 and birth_mo_day[1] <= 20:
    star_sign = "牡羊座（Aries）03/21 ~ 04/20"
if birth_mo_day[0] == 3 and birth_mo_day[1] >= 21:
    star_sign = "牡羊座（Aries）03/21 ~ 04/20"
if birth_mo_day[0] == 5 and birth_mo_day[1] <= 21:
    star_sign = "金牛座（Taurus）04/21 ~ 05/21"
if birth_mo_day[0] == 4 and birth_mo_day[1] >= 21:
    star_sign = "金牛座（Taurus）04/21 ~ 05/21"
if birth_mo_day[0] == 6 and birth_mo_day[1] <= 21:
    star_sign = "雙子座（Gemini）05/22 ~ 06/21"
if birth_mo_day[0] == 5 and birth_mo_day[1] >= 22:
    star_sign = "雙子座（Gemini）05/22 ~ 06/21"
if birth_mo_day[0] == 7 and birth_mo_day[1] <= 22:
    star_sign = "巨蟹座（Cancer）06/22 ~ 07/22"
if birth_mo_day[0] == 6 and birth_mo_day[1] >= 22:
    star_sign = "巨蟹座（Cancer）06/22 ~ 07/22"
if birth_mo_day[0] == 8 and birth_mo_day[1] <= 23:
    star_sign = "獅子座（Leo）07/23 ~ 08/23"
if birth_mo_day[0] == 7 and birth_mo_day[1] <= 23:
    star_sign = "獅子座（Leo）07/23 ~ 08/23"
if birth_mo_day[0] == 9 and birth_mo_day[1] <= 23:
    star_sign = "處女座（Virgo）8/24~09/23"
if birth_mo_day[0] == 8 and birth_mo_day[1] >= 24:
    star_sign = "處女座（Virgo）8/24~09/23"
if birth_mo_day[0] == 10 and birth_mo_day[1] <= 23:
    star_sign = "天秤座（Libra）09/24~10/23"
if birth_mo_day[0] == 9 and birth_mo_day[1] >= 24:
    star_sign = "天秤座（Libra）09/24~10/23"
if birth_mo_day[0] == 11 and birth_mo_day[1] <= 22:
    star_sign = "天蠍座（Scorpio）10/24~11/22"
if birth_mo_day[0] == 10 and birth_mo_day[1] >= 24:
    star_sign = "天蠍座（Scorpio）10/24~11/22"
if birth_mo_day[0] == 12 and birth_mo_day[1] <= 21:
    star_sign = "射手座（Sagittarius）11/23~12/21"
if birth_mo_day[0] == 11 and birth_mo_day[1] >= 23:
    star_sign = "射手座（Sagittarius）11/23~12/21"
if birth_mo_day[0] == 1 and birth_mo_day[1] <= 20:
    star_sign = "摩羯座（Capricorn）12/22~01/20"
if birth_mo_day[0] == 12 and birth_mo_day[1] >= 22:
    star_sign = "摩羯座（Capricorn）12/22~01/20"
if birth_mo_day[0] == 2 and birth_mo_day[1] <= 19:
    star_sign = "水瓶座（Aquarius）01/21~2/19"
if birth_mo_day[0] == 1 and birth_mo_day[1] >= 21:
    star_sign = "水瓶座（Aquarius）01/21~2/19"

print(star_sign)
