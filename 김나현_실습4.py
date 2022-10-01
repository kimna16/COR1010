print('20191286 김나현 실습4') #학번, 이름, 실습명 출력
print()                        #줄바꿈

#문제 1
print("***** 문제1 *****")              #문제 번호 출력
num=input("경과 일을 입력하세요: ")     #경과 일 입력
num=int(num)                            #변수 num을 정수형으로 형변환 

if (num%7==0):                                  #변수가 7로 나누어질 때, 
    print("{}일 후는 {}요일".format(num,'화'))  #화요일이라고 출력 
elif (num%7==1):                                #변수를 7로 나누었을 때, 나머지가 1이면 
    print("{}일 후는 {}요일".format(num,'수'))  #수요일이라고 출력 
elif (num%7==2):                                #변수를 7로 나누었을 때, 나머지가 2이면
    print("{}일 후는 {}요일".format(num,'목'))  #목요일이라고 출력
elif (num%7==3):                                #변수를 7로 나누었을 때, 나머지가 3이면
    print("{}일 후는 {}요일".format(num,'금'))  #금요일이라고 출력
elif (num%7==4):                                #변수를 7로 나누었을 때, 나머지가 4이면
    print("{}일 후는 {}요일".format(num,'토'))  #토요일이라고 출력
elif (num%7==5):                                #변수를 7로 나누었을 때, 나머지가 5이면
    print("{}일 후는 {}요일".format(num,'일'))  #일요일이라고 출력
elif (num%7==6):                                #변수를 7로 나누었을 때, 나머지가 6이면
    print("{}일 후는 {}요일".format(num,'월'))  #월요일이라고 출력
print()                                         #줄바꿈

    
#문제 2
print("***** 문제2 *****")             #문제 번호 출력
num=input("경과 일을 입력하세요: ")    #경과 일 입력
num=int(num)                           #변수 num을 정수형으로 형변환 
weekList='화수목금토일월'              #요일 판별 값을 리스트로 구성

print("{}일 후는 {}요일".format(num,weekList[num%7]))  #요일 판별 값, 문자열 포맷팅을 사용하여 출력
print()                                                #줄바꿈


#문제 3
print("***** 문제3 *****")                                                                      #문제 번호 출력         
medals=[['Austria',0,2,1],['Canada',4,8,5],['China',5,0,1],['France',0,4,5],['Germany',1,1,2],  #나라별 메달 개수 리스트 선언
        ['Japan',1,1,0],['Korea',5,3,1],['Norway',4,4,7],['Russia',4,6,4],['Vietnam',1,1,5]]

medals[0].append(medals[0][1]+medals[0][2]+medals[0][3])   #medals라는 리스트의 첫 번째 원소에 오스트리아 메달 합계 추가
medals[1].append(medals[1][1]+medals[1][2]+medals[1][3])   #medals라는 리스트의 두 번째 원소에 캐나다 메달 합계 추가
medals[2].append(medals[2][1]+medals[2][2]+medals[2][3])   #medals라는 리스트의 세 번째 원소에 중국 메달 합계 추가
medals[3].append(medals[3][1]+medals[3][2]+medals[3][3])   #medals라는 리스트의 네 번째 원소에 프랑스 메달 합계 추가
medals[4].append(medals[4][1]+medals[4][2]+medals[4][3])   #medals라는 리스트의 다섯 번째 원소에 독일 메달 합계 추가 
medals[5].append(medals[5][1]+medals[5][2]+medals[5][3])   #medals라는 리스트의 여섯 번째 원소에 일본 메달 합계 추가
medals[6].append(medals[6][1]+medals[6][2]+medals[6][3])   #medals라는 리스트의 일곱 번째 원소에 대한민국 메달 합계 추가
medals[7].append(medals[7][1]+medals[7][2]+medals[7][3])   #medals라는 리스트의 여덟 번째 원소에 노르웨이 메달 합계 추가
medals[8].append(medals[8][1]+medals[8][2]+medals[8][3])   #medals라는 리스트의 아홉 번째 원소에 러시아 메달 합계 추가
medals[9].append(medals[9][1]+medals[9][2]+medals[9][3])   #medals라는 리스트의 열 번째 원소에 베트남 메달 합계 추가

print(medals[0]) #medals라는 리스트의 첫 번째 원소 출력
print(medals[1]) #medals라는 리스트의 두 번째 원소 출력
print(medals[2]) #medals라는 리스트의 세 번째 원소 출력
print(medals[3]) #medals라는 리스트의 네 번째 원소 출력
print(medals[4]) #medals라는 리스트의 다섯 번째 원소 출력
print(medals[5]) #medals라는 리스트의 여섯 번째 원소 출력
print(medals[6]) #medals라는 리스트의 일곱 번째 원소 출력
print(medals[7]) #medals라는 리스트의 여덟 번째 원소 출력
print(medals[8]) #medals라는 리스트의 아홉 번째 원소 출력
print(medals[9]) #medals라는 리스트의 열 번째 원소 출력
print()          #줄바꿈
print(medals)    #medals라는 리스트 전체 출력
   
