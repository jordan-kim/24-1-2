# 2020063027_이승재
a = input('주민 번호를 입력하세요: ')
b=''
if int(a[7]) is 1:
    y,s = 1900, '남자'
elif int(a[7]) is 2:
    y,s = 1900, '여자'
elif int(a[7]) is 3:
    y,s = 2000, '남자'
elif int(a[7]) is 4:
    y,s = 2000, '여자'
print ('나는 {}년 {}월 {}일에 태어난 {}입니다.'.format(y+int(a[0:2]),a[2:4],a[4:6],s))