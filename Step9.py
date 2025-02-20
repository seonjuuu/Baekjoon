#1
while(1):
    A, B = map(int,input().split())
    if (A == B):
        break
    elif(B%A == 0):
        print("factor")
    elif(A%B == 0):
        print("multiple")
    else:
        print("neither")
        
        
#2
N, k = map(int,input().split())
A = []
for i in range(1,N+1):
    if (N%i == 0):
        A.append(i)

if (len(A) >= k):
    print(A[k-1])
else:
    print("0")
  
    
    
#3 -> join / 리스트 합을 sum함수로 구할수있음 / sep="" : 출력
while(1):
    n = int(input())
    if (n==-1):
        break
    A = []
    for i in range(1,n):
        if(n%i==0):
            A.append(i)

    if sum(A) == n :
        print(n,' = '," + ".join(str(i) for i in A), sep="")
    else:
        print(n,"is NOT perfect.")
        
        
        
#4
N = int(input())
N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in A :
    B = []
    for k in range(1,i):
        if i%k == 0:
            B.append(k)
    if len(B) == 1 :
        cnt += 1
print(cnt)



#5
M = int(input())
N = int(input())

num = []
result = []
for i in range(M,N+1):
    num.append(i)

for i in num :
    A = []
    for k in range(1,i):
        if i%k == 0:
            A.append(k)
    if len(A) == 1:
        result.append(i)

if len(result) > 0 :
    print(sum(result))
    print(min(result))

else:
    print("-1")
    
    
#6
#소수리스트 따로 구할 필요 X
#어짜히 앞에서부터 나누기 때문에 소수 아닌 수들로 나눠질 수가 없음
N = int(input())
A = []
for i in range(2,N+1):
    if N==1:
        break
    while(N%i == 0):  # 같은 수로 계속 나누기
        print(i)
        N = N//i