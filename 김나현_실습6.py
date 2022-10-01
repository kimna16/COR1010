#4반 1조 20191286 김나현 실습6

print("***** 문제1 *****")                                                  #문제 번호 출력 
menu={"그린티라떼":3000,"모카라떼":3500,"아메리카노":2000,"카페라떼":2500}  #메뉴별 가격을 사전 객체로 구성 
print("*메뉴 가격 찾기입니다")                                              #문자열 출력 
while(1):                                                                   #while 반복문 실행 
        beverage=input("메뉴?")                                             #키보드로 메뉴 입력 받음 
        if (beverage==''):                                                  #빈 문자열을 입력했다면 
            break                                                           #반복을 종료함  
        if (beverage in menu):                                              #키보드로 입력 받은 음료수가 있는 메뉴면 
            print("{:s} {:d}원".format(beverage,menu[beverage]))            #메뉴와 메뉴의 가격을 출력함 
        else:                                                               #키보드로 입력 받은 음료수가 없는 메뉴면 
            print("없는 메뉴!")                                             #없는 메뉴라고 출력함 
print()                                                                     #줄바꿈



print("***** 문제2 *****")                                #문제 번호 출력 
fr=open("data.txt",'r')                                   #파일을 읽기 전용으로 엶
list1=fr.read()                                           #파일 전체를 하나의 문자열로 읽음  
fr.close()                                                #파일을 닫음
print("** 읽은 문자열")                                   #문자열 출력 
print(list1)                                              #list1 출력 
list2=""                                                  #빈 문자열 생성 
for a in list1:                                           #for 반복문을 돌면서 list1에 있는 모든 원소에 대해 아래 명령문을 실행함
    if a in """~!@#$%^&*-_+=(){}[]:;?.,<”>’""":           #list1에 있는 원소가 특수문자 중 하나면
        list2+=' '                                        #list2에 공백 문자를 연결하고 
    else:                                                 #list1에 있는 원소가 특수문자가 아니면 
        list2+=a                                          #list2에 해당 원소를 연결함 
print("** 새 문자열")                                     #문자열 출력 
print(list2)                                              #list2 출력 
list3=list2.split()                                       #list2를 공백을 기준으로 분리하여 list3를 만듦
dictionary={}                                             #빈 사전 생성 
for a in list3:                                           #for 반복문을 돌면서 list3에 있는 모든 원소에 대해 아래 명령문을 실행함 
    if (a in dictionary):                                 #list3에 있는 원소가 사전에 있으면 
        dictionary[a]+=1                                  #value를 하나 증가하고 
    else:                                                 #list3에 있는 원소가 사전에 없으면 
        dictionary[a]=1                                   #해당 원소가 key, value를 1로 하는 원소 쌍을 추가함 
print("** 단어별 빈도수")                                 #문자열 출력 
for a in dictionary:                                      #for 반복문을 돌면서 사전에 있는 모든 원소에 대해 아래 명령문을 실행함 
    print("{:10s}{:3d}".format(a,dictionary[a]))          #단어 10자리, 빈도수 3자리로 출력함 
