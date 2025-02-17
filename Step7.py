#1 행렬 -> 리스트안에 리스트 => A = [[0행],[1행],[2행]] / A[0] = 리스트 , A[0][1] = 원소
A, B = [], []  ## A=[] , B=[] (X)
N, M = map(int, input().split())

for i in range(N) :
    row = list(map(int, input().split()))
    A.append(row)


for i in range(N):
    row = list(map(int,input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print() #행을 나눔
    
    
    
#2
A = []

for i in range(9):
    row = list(map(int, input().split()))
    A.append(row)

max = A[0][0]
maxrow, maxcol = 0,0    #위치초기화
for row in range(9):
    for col in range(9):
        if A[row][col] > max :
            max = A[row][col]
            maxrow = row
            maxcol = col
print(max)
print(maxrow+1, maxcol+1)



#3
# 행의 길이 = 열 -> len(행) = 열의 갯수
# A = [input() for i in range(5)]
A = []
for i in range(5):
    row = list(input())  #split() 할 필요 X(띄어쓰기 안한다고함)
    A.append(row)
    
for col in range(15):
    for row in range(5):
        if col < len(A[row]):   ## 열의 인덱스가 행의 길이보다 짧으면 출력
            print(A[row][col],end='')
            
            
            
#4
N = int(input())
array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화 ([0]*100:원소 / for문 : 행갯수)
for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
    x, y = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x, x + 10):  # 가로를 돈다.
        for j in range(y, y + 10):  # 세로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += array[k].count(1)  # 1 개수만 세어준다

print(result)


##4(2)
N = int(input()) #색종이 개수
array = []
for _ in range(100):
    array.append([0]*100)

for _ in range(N):
    x, y = map(int, input().split())
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            array[i][j] = 1
            
sum = 0
for i in range(100):
    sum += array[i].count(1)
print(sum)