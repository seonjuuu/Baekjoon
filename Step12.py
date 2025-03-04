#1 -> 완전 이진 탐색
#경우1 -> for 삼중문
N, M = map(int,input().split())
list = list(map(int,input().split()))
result = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (list[i]+list[j]+list[k] <= M):
                result.append(list[i]+list[j]+list[k])
            else:
                continue

print(max(result))


#2
#1) N보다 작은 수들 다 확인하는 과정 -> for문
#2) i의 각 자릿수를 더함
# (map(int,str(i))) -> 정수인 i를 문자열로 변환(str(i))=>변환하게 되면 문자열의 각 문자로 쪼개진다!! -> map함수를 이용하여 각 문자에 int함수를 적용하여 정수로 변환
## map(int, num_str)는 num_str의 각 문자에 int 함수를 적용하여 문자 '1', '9', '8'을 각각 정수 1, 9, 8로 변환합니다. 최종적으로 [1, 9, 8]이라는 리스트가 됩니다
#3) i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자 !!

N = int(input())

for i in range(1,N+1):    # n보다 작은 수들을 다 확인
    num = sum(map(int,str(i)))  # i의 각 자릿수의 합
    num_sum = i + num   # 분해합 = 생성자 + 각 자릿수의 합
    if num_sum == N:
        print(i)
        break
    if i == N :  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)
        
        
#3
a,b,c,d,e,f = map(int,input().split())
result = []
for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x + b*y == c ) and (d*x+e*y==f):
            print(x,y)
            break
        
        
#4
# (i+j)가 짝수인 자리인 경우, 맨 왼쪽 위칸의 색과 같아야한다. 즉, 해당 칸의 색이 흰색이면 맨 왼쪽 위칸의 색이 검정색인경우일때 수정해야하는 칸이다. 따라서 b_start를 1증가.
# 홀수인 경우에는, 해당 칸과 맨 왼쪽 위칸의 색이 달라야한다. 따라서 해당칸의 색이 흰색이면, 맨 왼쪽 위칸의 색이 흰색일 때 수정해하는것이므로, w_start +1
n, m = map(int,input().split())
bored = []
cnt = []

for i in range(n):
    bored.append(input())