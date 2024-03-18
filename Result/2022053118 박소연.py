# 2022053118 박소연

'''공학프로그래밍2 과제
주민등록번호를 입력할 때 생년월일과 성별을 출력하는 코드를 만들어보세요.
예 : 981216-1234123 입력 -> 나는 1998년 12월 16일에 태어난 남자입니다.

조건
주민등록번호 입력 시 '-' 반드시 포함
1900년대 출생, 2000년대 출생 모두 출력이 되어야 함

주민등록번호 뒷자리 첫번째 숫자 의미

1 : 1900년대생 남자
2 : 1900년대생 여자
3 : 2000년대생 남자
4 : 2000년대생 여자
'''

def b():
    while True:
        a = input("주민등록번호를 입력하세요 (-포함): ")
        if a[6] != '-' or len(a) != 14:
            print("다시 입력하세요")
            continue
        year, month, day, gender = c(a)
        print(f"나는 {year}년 {month}월 {day}일에 태어난 {gender}입니다.")
        break

def c(a):
    date = a[:6]
    gender_ = int(a[7])
    if gender_ == 1 or gender_ == 3:
        gender = '남자'
        year_ = '19' if gender_ == 1 else '20'
    else:
        gender = '여자'
        year_ = '19' if gender_ == 2 else '20'

    year = year_ + date[:2]
    month = date[2:4]
    day = date[4:6]

    return year, month, day, gender

if __name__ == "__main__":
    b()