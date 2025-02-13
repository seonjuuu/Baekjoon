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