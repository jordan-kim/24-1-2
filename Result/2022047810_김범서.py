id = input("주민등록번호를 입력하세요: ")
id1, id2 = id.split("-")

year = id1[0:2]
month = id1[2:4]
day = id1[4:6]
gender = int(id2[0])

if gender >= 3:
    answer = f"나는 20{year}년 "
else:
    answer = f"나는 19{year}년 "

answer += f"{month}월 {day}일에 태어난 "

if gender % 2 == 1:
    answer += "남자입니다."
else:
    answer += "여자입니다."

print(answer)
