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

def fac(n):
    if n == 0:
        return 1
    f = n*fac(n-1)
    return f

print(fac(N))


#8
N = int(input())
cnt = 0
def fac(n):
    if n == 0:
        return 1
    f = n*fac(n-1)
    return f

S = (str(fac(N)))[::-1]
for i in S:
    if i=="0":
        cnt +=1
    else:
        break

print(cnt)


# 골드바흐의 추측
# 소수 리스트를 먼저 만들어놓음
# 1000001 이 소수인지 확인하기 위해서는 1000001의 제곱근까지만 확인해보면 되는것이므로! 범위는 2~1000001**0.5 까지

import sys 
#소수리스트
num = [True] * 1000001
for i in range(2, int(len(num)**0.5)+1):
    if num[i] == True:  # i가 소수라면
        for j in range (2*i, 1000001, i):
            num[j] = False # i의 배수들은 소수가 아니므로 False

while(1):
    N = int(sys.stdin.readline())
    if N==0:
        break
    
    for i in range(3,N-2,2):
        if num[i]==True and num[N-i]==True :
            print(f'{N} = {i} + {N-i}')
            break
    else:  # for-else문 
        print("\"Goldbach\'s conjecture is wrong.\"")     
     

#C
#팩토리얼 X
#문제 : 끝자리에 0 -> 10의 거듭제곱 -> 10^1 : 끝자리 0이 1개, 10^2 : 끝자리 0이 2개 . . 10^n : 끝자리 0이 n개
# 10^n -> 2^n * 5^n -> 즉, nCm의 소인수분해에 2*5가 몇 개 포함되어 있는지 !!
# nCm에 포함된 2와 5의 개수를 각각 센 다음, 둘 중 더 작은 개수가 끝자리 0의 개수 (2*5의 형태가 만들어지기 위해선 짝이 맞아야하기 때문!!)
# 2의 개수 = n!이 포함하는 2의 개수 - m!이 포함하는 2의 개수 - (n-m)!아 포함하는 2의 개수
# n!이 포함하는 2의 개수? = "n이하의 범위에서 k^1,k^2,k^3 ... 의 배수를 모두 카운트하여 더하는것"

import sys
n, m = map(int,input().split())

def count_k(n,k): # n!에 포함된 k의 개수 구하기
    result = 0    
    temp = k
    
    while temp <= n:
        result += n // temp
        temp *= k   # k의 1승, 2승, 3승 . . 
    return result

two = count_k(n,2) - count_k(n-m,2) - count_k(m,2)
five = count_k(n,5) - count_k(n-m,5) - count_k(m,5)
print(min(two, five))  