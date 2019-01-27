"""

百分制成绩转等级制成绩
90分以上 	 	--> A
80分~89分 	--> B
70分~79分	--> C
60分~69分	--> D
60分以下		--> E

Version: 0.1
Author: 骆昊
Date: 2018-02-28

"""

score = float(input('请输入成绩: '))
if 100 >= score >= 90:
    grade = 'A'
elif 90 > score >= 80:
    grade = 'B'
elif 80 > score >= 70:
    grade = 'C'
elif 70 > score >= 60:
    grade = 'D'
elif 60 > score >= 0:
    grade = 'E'
else:
    grade = '请输入有效单位！'
print('对应的等级是:', grade)
