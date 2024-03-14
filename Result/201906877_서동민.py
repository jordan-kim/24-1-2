#2019068577_서동민
# 주민등록번호 > 생년월일
id_number= input("주민등록번호를 입력하세요(-포함) : ")

if(len(id_number) != 14) :
    print("잘못된 길이입니다.")
    exit()

year = id_number[0:2]
month = id_number[2:4]
day = id_number[4:6]

gender = int(id_number[7])

if(gender == 1 or gender == 2) :
    year = "19" + year
elif(gender == 3 or gender == 4) :
    year = "20" + year

if(gender == 1 or gender == 3) :
    gender = "남자"
elif(gender == 2 or gender == 4) :
    gender = "여자"


print("나는 {}년 {}월 {}일에 태어난 {}입니다.".format(year, month, day, gender))
