#20191286 김나현 중간시험

print('*** 문제1 ***')  #문제 1번
equation = input("사칙연산을 입력(x 연산자 y)\n") #문자열 입력 

if (len(equation.split()) != 3): #연산자와 피연산자의 개수가 3개보다 적거나 많은 경우
    print("잘못 입력!!!") #잘못 입력이라고 출력 
else: #연산자와 피연산자의 개수가 3개인 경우 
    x, operator, y = equation.split() #띄어쓰기 간격으로 연산자, 피연산자 구분
    if (x.isnumeric()==False or y.isnumeric()==False): #피연산자가 정수가 숫자가 아니면 잘못 입력이라고 출력
        print("잘못 입력!!!") #잘못 입력이라고 출력
    elif (float(x)%1!=0 or float(y)%1!=0): #피연산자가 정수가 아니면 잘못 입력이라고 출력
        print("잘못 입력!!!") #잘못 입력이라고 출력
    else: #피연산자가 정수일 경우 
        x=int(x) #정수형으로 변환
        y=int(y) #정수형으로 변환 
        if (operator == '+'): #+이면
            print("{}{}{}={}".format(x, operator,y, x+y)) #더해서 출력
        elif (operator == '-'): #-이면
            print("{}{}{}={}".format(x, operator,y, x-y)) #빼서 출력
        elif (operator == '*'): #*이면
            print("{}{}{}={}".format(x, operator,y, x*y)) #곱해서 출력
        elif (operator == '/'): #/이면
            print("{}{}{}={:.3f}".format(x, operator,y, x/y)) #나눠서 출력
        else: #사칙연산이 아닐 경우
            print("잘못 입력!!!") #잘못 입력이라고 출력


print('*** 문제2 ***')  #문제 2번
변수 = {202201:['최양업', '010-1234-4500']}, {202202:['정약용','010-2230-6540']},{202203:['김대건','010-3232-7788']} #튜플 생성
dic1=변수[0] #변수 0번 index의 사전
dic2=변수[1] #변수 1번 index의 사전
dic3=변수[2] #변수 2번 index의 사전

std_id, name, phone, score=input().split() #문자열 입력
dic={} #빈 사전 생성
dic[int(std_id)]=name,phone,score #사전에 추가
print(dic) #사전 출력 



