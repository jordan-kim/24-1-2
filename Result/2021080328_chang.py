#2021080328_chang
while True:
    a = input("주민등록번호를 입력하세요: ")
    if "-" in a:
        b, c = a.split("-")
        if len(b) == 6 and len(c) == 7:
            break

year = b[0:2]
month = b[2:4]
day = b[4:6]
gender = int(c[0])

if gender >= 3:
    year = "20" + year
else:
    year = "19" + year

answer = f"나는 {year}년 {month}월 {day}일에 태어난 "

if gender % 2 == 1:
    answer += "남자입니다."
else:
    answer += "여자입니다."

print(answer)