#1
S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
N = N[::-1]
B = int(B)
result = 0

for i in range(len(N)):
    result += S.index(N[i])*(B**i)
    
print(result)