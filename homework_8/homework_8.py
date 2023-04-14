'''
同學的姓名為key,value必需為{'國文': 56, '英文': 85, '數學': 68, '自然': 76, '社會': 62}
建立2維的dictionary
'''

import random
students ={name:{scorces:random.randint(50,100) for scorces in ["國文","英文","數學","自然","社會"]} for name in ["賴依凡","張雯嬌","張濬昇","謝明學","劉俊孝","彭千祐","賴弈旭","劉冠亨","黃基展","楊凱丞","張文嘉","鄭丞芸","翟品皓","邱秀慧","陳瑞涓","陳彥廷","鄭興耀","溫國焜","高家成","鄒騰沅","徐瑋良","余友中","李唯","林可中"]}

st_name = input("請輸入同學的姓名:")
students[st_name]
print(st_name)
print(students[st_name])
