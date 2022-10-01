print("20191286 김나현 실습5")                                            #학번 이름 실습명
print()                                                                   #줄바꿈


print("***** 문제1 *****")                                                #문제1
medals = [ ['Austria',0,2,1], ['Canada',4,8,5], ['China',5,0,1],          #medals이라는 리스트 생성
['France',0,4,5], [ 'Germany',1,1,2], ['Japan',1,1,0],
['Korea',5,3,1], ['Norway',4,4,7], ['Russia',4,6,4],
['Viet Nam',1,1,5] ]

for i in medals:                                                          #medals에 있는 모든 나라마다 한 번씩 반복하여 아래 명령문을 실행함
    i.append(i[1]+i[2]+i[3])                                              #각 나라의 금, 은, 동 메달을 합한 개수를 내부 리스트의 맨 끝에 추가함
    
for i in medals:                                                          #medals에 있는 모든 나라마다 한 번씩 반복하여 아래 명령문을 실행함
    print(i)                                                              #각 나라에 관한 정보를 출력함
    
print()                                                                   #줄바꿈
print(medals)                                                             #변수 medals를 출력함
print()                                                                   #줄바꿈


print("**** 문제2 *****")                                                 #문제2
list1 = input("입력하세요\n")                                             #문자열을 입력 받음

print("** 특수문자를 공백으로 바꾼 새 문자열")                            #안내문 출력
list2 = ""                                                                #새 문자열을 저장할 빈 문자열 생성
for a in list1:                                                           #입력 받은 문자열의 모든 문자를 한 번씩 반복하여 아래 명령문들을 실행함
    if (a in "~!@#$%^&*-_+=(){}[]:;?.,<>"):                               #특수문자일 경우 
        a=' '                                                             #특수문자를 공백으로 바꿈
    print(a,end='')                                                       #문자 출력
    list2+=a                                                              #빈 문자열에 문자를 추가함
print()                                                                   #줄바꿈

print("** 단어별 빈도수")                                                 #안내문 출력
list3 = list2.split()                                                     #새 문자열을 공백을 기준으로 분리하여 새로운 리스트 생성
dictionary={}                                                             #빈 사전 객체 생성
for a in list3:                                                           #list3에 있는 모든 원소를 하나씩 반복하여 아래 명령문들을 실행함
    if (a in dictionary):                                                 #이전에 list3에 해당 원소와 같은 원소가 있었다면 
        dictionary[a]+=1                                                  #value를 1 증가함
    else:                                                                 #이전에 list3에 해당 원소와 같은 원소가 없었다면
        dictionary[a]=1                                                   #해당 원소를 key로 하고, value를 1로 하는 새로운 원소 쌍을 추가함
        
for a in dictionary:                                                      #사전에 있는 모든 원소 쌍을 한 번씩 반복하여 아래 명령문을 실행함
    print("{:10s}{:2d}".format(a, dictionary[a]))                         #단어는 10자리, 빈도수는 2자리로 출력


