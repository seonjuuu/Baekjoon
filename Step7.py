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