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