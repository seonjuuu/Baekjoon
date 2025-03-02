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