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
  
  
#4
#한변에 점이 몇개 있는지 
# 입력
n = int(input())

# 점의 개수 계산
side = (1 + 2**n)  #한변을 기준으로 늘어나는 규칙
print(side**2)     #총점의 갯수는, 변의 점개수의 제곱


#5 
# -> cnt를 하나 증가할때, 수는 6이 증가
# 기본적으로 cnt = 1
# 2칸 -> 2~7 = (1+6*1) -> 즉, 최댓값이 7. 입력받은 수가 최댓값보다 작으면 그 2칸만 이동
# 해당 수가 어느 범위에 있는지
# 3칸 -> 8~19 = (7+6*2)
# 4칸 -> 20~37= (19+6*3)
#즉, 최댓값보다 크면 한칸 더 증가

N = int(input())
cnt = 1         #출력값, 이동칸수
nummax = 1      #최댓값

while(N > nummax):
    nummax = nummax+(6*cnt)  #다음칸수 최댓값
    cnt += 1                 #칸수 증가
    
print(cnt)
