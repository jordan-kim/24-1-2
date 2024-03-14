#2021073863_박승우

num=(input('주민번호를 입력하시오:'))

if '-' in num:
    cn=num.replace('-','')


mog=int(cn[6])

if mog<3:
    if mog==1:
        print('나는 19{}년 {}월 {}일에 태어난 남자입니다.'.format(cn[0:2], cn[2:4], cn[4:6]))
    if mog==2:
        print('나는 19{}년 {}월 {}일에 태어난 여자입니다.'.format(cn[0:2], cn[2:4], cn[4:6]))

else:
    if mog==3:
        print('나는 20{}년 {}월 {}일에 태어난 남자입니다.'.format(cn[0:2], cn[2:4], cn[4:6]))
    if mog==4:
        print('나는 20{}년 {}월 {}일에 태어난 여자입니다.'.format(cn[0:2], cn[2:4], cn[4:6]))