print("20191286 김나현 실습#2")
print() #빈 줄 출력

#문제 1
print("***** 문제1 *****")
average=(793+889+927)/3 #평균 계산
print(average)          #그대로 출력
print(round(average,1)) #소수점 이하 1자리 출력
print(int(average))     #버림으로 정수 출력
print(round(average))   #반올림으로 정수 출력
print()                 #빈 줄 출력

#문제 2
print("***** 문제2 *****")
distance = 40*(10**12)             #지구로부터의 거리
speedOfLight = 3*(10**5)           #빛의 속도
time = distance/speedOfLight       #빛의 속도로 별까지 가는 데에 걸리는 시간
print(time/(365*24*60*60), "광년") #초단위로 표현된 변수를 년단위로 바꾸어 출 
print()                            #빈 줄 출력

#문제 3
print("***** 문제3 *****")
a=15; b=143; #변수 할당
print(str(a)+"일 후는 화요일인가?", a%7==1) #15일 후가 화요일인지 판별
print(str(b)+"일 후는 화요일인가?", b%7==1) #143일 후가 화요일인지 판별
