
# 학번: 2021073518 이름 : 김리나
# 주민등록번호를 입력할 때 생년월일과 성별을 출력하는 코드를 만들어보세요.

a = list(map(str,input('주민등록번호를 -를 포함하여 입력하시오 : ').split('-')))
birth_day = list(a[0])
gender = list(a[1])


year1 = int(birth_day.pop(0))
year2 = int(birth_day.pop(0))
month1 = int(birth_day.pop(0))
month2 = int(birth_day.pop(0))
day1 = int(birth_day.pop(0))
day2 = int(birth_day.pop(0))
gender_p = int(gender.pop(0))

if gender_p == 1 :
    print('나는', 1900+year1*10+year2,'년',month1*10+month2,'월',day1*10+day2,'일에 태어난 남자입니다.')

elif gender_p == 3 :
    print('나는', 2000 + year1 * 10 + year2, '년', month1 * 10 + month2, '월', day1 * 10 + day2, '일에 태어난 남자입니다.')

elif gender_p ==2 :
    print('나는', 1900 + year1 * 10 + year2, '년', month1 * 10 + month2, '월', day1 * 10 + day2, '일에 태어난 여자입니다.')
elif gender_p ==4 :
    print('나는', 2000 + year1 * 10 + year2, '년', month1 * 10 + month2, '월', day1 * 10 + day2, '일에 태어난 여자입니다.')