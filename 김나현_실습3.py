print('20191286 김나현 실습3') #학번, 이름, 실습명 출력

#문제1
print()                        #줄바꿈
print('***** 문제1 *****')     #문제 번호 출력
a=input('근무시간? ')          #근무시간 입력
b=input('시간당 급여? ')       #시간당 급여 입력
c=input('원천징수세율? ')      #원천징수세율 입력
d=input('주민세율? ')          #주민세율 입력 

a=int(a)                       #정수 형변환
b=int(b)                       #정수 형변환
c=float(c)                     #실수 형변환
d=float(d)                     #실수 형변환

print('='*20)                                                   #출력1
print('*총 급여: {:d}원'.format(a*b))                           #출력2
print('*공제:\n 원천징수세 ({:.2f}): {:.1f}원'.format(c,a*b*c)) #출력3
print(' 주민세 ({:.2f}): {:.1f}원'.format(d,a*b*d))             #출력4
print(' 총 공제: {:.1f}원'.format(a*b*c+a*b*d))                 #출력5
print('*공제 후 급여: {:.0f}원'.format(a*b-(a*b*c+a*b*d)))      #출력6


#문제2
print()                               #줄바꿈
print('***** 문제2 *****')            #문제 번호 출력
num=input('경과 일을 입력하세요: ')   #경과 일 입력

num=int(num)                          #정수 형변환

print('{}일 후는 월요일인가? {}'.format(num,num%7==0)) #월요일인지 판별
print('{}일 후는 화요일인가? {}'.format(num,num%7==1)) #화요일인지 판별
print('{}일 후는 수요일인가? {}'.format(num,num%7==2)) #수요일인지 판별
print('{}일 후는 목요일인가? {}'.format(num,num%7==3)) #목요일인지 판별
print('{}일 후는 금요일인가? {}'.format(num,num%7==4)) #금요일인지 판별
print('{}일 후는 토요일인가? {}'.format(num,num%7==5)) #토요일인지 판별
print('{}일 후는 일요일인가? {}'.format(num,num%7==6)) #일요일인지 판별


#문제3
print()                                                  #줄바꿈
print('***** 문제3 *****')                               #문제 번호 출력
firstName, lastName=input('영문이름?(이름 성)').split()  #이름, 성 입력
year, month, date=input('생일?(yyyy/mm/dd)').split('/')  #생년월일 입력

identify=lastName[len(lastName)-1]+firstName[1:]         #아이디 생성
password='mm'+year[len(year)-1]+month+date               #비밀번호 생성

print('아이디',identify)                                 #아이디 출력
print('패스워드',password)                               #비밀번호 출력



