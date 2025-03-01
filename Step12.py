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