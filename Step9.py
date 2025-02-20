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