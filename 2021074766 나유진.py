#2021074766 나유진

def extract_info(resident_id):
    # 주민번호 추출 함수를 extract_info라고 정의한 코드

    birth_date = resident_id[:6]
    # 생년월일을 추출하기 위해 주민번호 앞 6자리 숫자 추출

    gender_code = int(resident_id[7])//2
    birth_century = "19" if gender_code == 0 else "20"
    # 주민번호 뒷자리 첫번쩨 숫자로 성별과 출생연대 구분

    birth_year = birth_century + birth_date[:2]
    birth_month = birth_date[2:4]
    birth_day= birth_date[4:6]
    # 출생 연도, 월, 일 추출

    gender = "남자" if gender_code % 2 == 1 else "여자"
    # 성별 구분. 남자는 1 또는 3, 여자는 2 또는 4. 따라서 2로 나누었을 때 나머지 1이면 남자

    return birth_year, birth_month, birth_day, gender

def main():
    resident_id = input("주민번호를 입력하세요 (예:981216-1234123):")
    # 주민 번호 입력받기
    if '-' not in resident_id:
        print("주민등록번호 형식이 잘못되었습니다.")
        return
    # '-'없을 시 에러 문구

    try:
        # 생년 월일, 성별 추출
        birth_year, birth_month, birth_day, gender = extract_info(resident_id)
        print(f"나는 {birth_year}년 {birth_month}월 {birth_day}일에 태어난 {gender}입니다.")
    except IndexError:
        print("주민등록번호 형식이 잘못되었습니다.")

if __name__ == "__main__":
    main()