#1 -> count
N = int(input())
A = list(map(int,input().split()))
V = int(input())

print(A.count(V))


#2
N, X = map(int,input().split())
A = list(map(int,input().split()))
for i in A:
    if(i<X):
        print(i, end=' ')  #end=" " 일렬출력을 옆으로 출력
        
        
#3
N = int(input())
A = list(map(int,input().split()))
print(min(A),max(A))


#4
A = []
for i in range(9):
    a = int(input())
    A.append(a)
print(max(A))
print(A.index(max(A))+1)


#5
N,M = map(int, input().split())
A= [0]*N
for X in range(M):
    i,j,k = map(int,input().split())
    for x in range(i-1,j):
        A[x] = k
for i in range(len(A)):
    print(A[i], end=" ")
    
    
#6
N, M=map(int, input().split())
A = []
for i in range(N):
    A.append(i+1)
for x in range(M):
    i,j = map(int, input().split())
    tamp = A[i-1]
    A[i-1] = A[j-1]
    A[j-1] = tamp
for i in range(N):
    print(A[i], end=' ')