#20191286 김나현 기말시험 

print("*** 문제1 ***") #문제 번호 1
성적={'Hong':90, 'Kim':100, 'Lee':89, 'Choi':50} #학점 사전 객체
def gChk(score): #함수
    if score >= 90:  #90점 이상
        grade='A' #A 학점
    elif score >= 80: #80점 이상
        grade='B' #B 학점
    elif score >= 70: #70점 이상
        grade='C' #C 학점
    else: #70점 미만
        grade='D' #D 학점
    return grade #함수 실행 결과로 학점을 반환함 

학점={} #빈 사전 객체 

for a in 성적: #for 반복문으로 성적 사적 객체에 있는 모든 원소에 대해 
    학점[a]=gChk(성적[a]) #value를 이용해 함수에 넣고 반환된 학점을 value로 갖는 원소를 빈 사전 객체에 포함함
    
print(학점) #이렇게 해서 만든 객체를 출력함



print("*** 문제2 ***") #문제 번호 2
while True: #무한 루프를 만듦
    a=int(input()); #숫자를 입력받아 정수형으로 변환 
    if (a<0): #a가 음수이면 
        break  #바로 반복을 종료하고 무한 루프를 빠져나감
    if (a%2==1): #a가 홀수이면 
        continue #출력 작업을 스킵하고 계속 진행함 
    else: #a가 짝수이면 
        print(a) #출력을 함 
        


print("*** 문제3 ***") #문제 번호 3
f=open("daily.txt", 'r') #daily.txt 파일을 엶
s=f.readlines() #한 줄씩 s에 저장함
totalcapu=0 #totalcapu는 카푸치노의 총 판매량
for num in s: #for 반복문을 돎
    num=num.split() #띄어쓰기로 문자열을 구분함
    capu=int(num[2]) #카푸치노 판매량을 저장함
    totalcapu=totalcapu+capu #총 카푸치노 판매량에 더함
print(totalcapu) #총 카푸치노 판매량을 출력함



print("*** 문제4 ***") #문제 번호 4
import numpy as np #numpy를 import함
list=np.array(range(1,101)) #1차원 배열을 만듦
print(list) #출력


print("*** 문제5 ***") #문제 번호 5
import pandas as pd #panda를 import함
import matplotlib.pyplot as plt #matplotlib을 import함
df=pd.DataFrame(성적.values(),index=성적.keys(),columns=['score']) #dataframe 객체 생성
df['grade']=학점.values() #'grade'열 추가
print(df['score'].mean()) #score의 평균 구함
print(df[df['grade']=='A']) #A학점인 행들을 추출하여 출력함
df['score'].plot(kind='bar') #score열을 막대그래프로 그림
plt.show() #보여줌


print("*** 문제6 ***") #문제 번호 6
import pandas as pd #panda를 import함
titanic = pd.read_csv('titanic.csv') #타이타닉.csv 파일을 읽음
print(titanic[["Sex", "Pclass","Age"]].groupby(['Sex','Pclass']).mean().round(1)) #출력함



























