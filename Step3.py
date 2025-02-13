#1 
N = int(input())
for i in range(1,10):
    print(N,"*",i,"=",N*i)


#2
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(A+B)


#3
n = int(input())
sum = 0                 #sum 변수 선언
for i in range(1,n+1):
    sum += i
print(sum)


#4
X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a,b = map(int,input().split())
    sum += (a*b)
if(X==sum):
    print("Yes")    
else:
    print("No")
    

#5 -> 몫을 정수형 : // -> N//4만큼 앞에 long이 붙음
N = int(input())
bite = ''
for i in range(N//4):
    bite += "long "     
bite = bite + 'int'
print(bite)


#6
import sys
T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)
    

#7
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print("Case #"+str(i+1)+':',(A+B))
    
    
#8
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')
    
    
#9
#파이썬의 경우 문자열을 더하고 곱할 수 있다는 강점이 있고, 직관성이 있는 언어입니다.
#그렇기에 문자열 출력하는 print를 반복하는 것이 아니라 단순 문자열에 수를 곱하여 문자열을 반복 출력할 수 있습니다.
N = int(input())
for i in range(1,N+1):
    print("*"*i)  
    

#10 (5칸을 공백과 별로 채워준다고 생각)
N = int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*(i)) 
    
    
#11
while(1):
    A,B = map(int,input().split())
    if(A==0 and B==0):
        break
    print(A+B)
    
    
#12 -> while - try - excpet 문
while True:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break