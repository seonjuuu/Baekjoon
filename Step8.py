#1
S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
N = N[::-1]
B = int(B)
result = 0

for i in range(len(N)):
    result += S.index(N[i])*(B**i)
    
print(result)


#2 -> 몫이 0일때까지 -> 나머지들만 진법변환
S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int,input().split())
result = ''
while N:                   #N이 0일 될때까지
    result = S[N%B] + result
    N=N//B                 #몫
    
print(result)    


#3
T = int(input())

for _ in range(T):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i
