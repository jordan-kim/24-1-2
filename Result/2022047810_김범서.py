# 2022047810_김범서
while True:
    id = input("주민등록번호를 입력하세요: ")
    if "-" in id:
        id1, id2 = id.split("-")
        if len(id1) == 6 and len(id2) == 7:
            break

year = id1[0:2]
month = id1[2:4]
day = id1[4:6]
gender = int(id2[0])

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
