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
