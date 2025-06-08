#1
A, B, C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#2
# 최대공약수 
# 1. 각 약수 구하기 2. 공통 약수 찾기 3. 최대
# 최소공배수 = 두 수의 곱을 최대공약수로 나눈 값
a, b = map(int, input().split())

tmp = []
for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        tmp.append(i)
    
print(max(tmp))
print(max(tmp) * (a // max(tmp)) * (b // max(tmp)))

#유클리드 호제법(최대공약수)
#1. GCD(a,b)=GCD(b,a%b)  = . . . = (최대공약수, 0)
#나머지가 0이 될때까지 -> 최대공약수 = b
#a가 작을 경우도 문제 없음
# -> a%b = a -> GCD(a,b)=GCD(b,a)로 자리가 바뀌어 계산됨
a, b = map(int, input().split())

def gcd(a, b):      # 최대공약수
    while b != 0:   # a%b != 0 
        a, b = b, a % b  
    return a

max = gcd(a,b)
print(max)
print((a * b) // max)

#3
T = int(input())
for i in range(T):
    A, B = map(int,input().split())
    n, m = A,B
    while(m!=0):
        n,m = m, n%m   # n = 최대공약수
    print((A*B)//n)   

#4
N = int(input())
num = list(map(int,input().split()))
cnt = 0
for i in num :
    result = []
    for j in range(1,i):
        if i%j == 0 :
            result.append(j)
    if len(result) == 1:
        cnt += 1
print(cnt)


#4 - 제곱근 활용
N = int(input())
num = list(map(int,input().split()))
cnt = 0

for i in num :
    if i > 1 :        # 1은 소수가 아님
        flag = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:   # 소수가 아님
                flag = 0
                break
    
        if flag:
            cnt += 1
print(cnt)


#5 -> 시간초과, 에라토스테네스의 체
# 예를들어, 30 일때 -> 5x6 -> 30이 소수인지를 확인할때는 -> 5로 나눠지는 먼저 나눠지는지 확인. = 6으로 나눠지는 확인하는 것과 같음 
# 따라서, 5로 나눠지는지만 확인해도 된다
# 즉, 소수 아닌 수 -> 약수들로 나눠지는데
# 이때, 약수들로 나눠지는지 확인할때, 모든 약수를 확인하는 것이 아니라, 약수들은 쌍을 이루고 있기에, 제곱근을 사용해서 모든 수의 절반만 확인
M, N = map(int,input().split())

for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0 :
            break
    else:              # if-else(X) #for-else (O) -> for문에서 break하지 않았을때(소수일때)
        print(i)


#7 -> 팩토리얼
N = int(input())