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