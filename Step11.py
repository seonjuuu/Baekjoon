#1 -> 시간복잡도를 이해해야하는 문제
print(1)  # 수행횟수는 무조건 딱1번 / 0(1)
print(0)  # 상수항이므로 차수는 0

#2
n = int(input())
print(n)
print(1)

#3
n = int(input())
print(n**2)
print(2)

#4
n = int(input())
print((n*(n-1))//2)
print(2)

#5
n = int(input())
print(n**3)
print(3)

#6 -> 조합, 1부터 n까지의 정수를 중복되지 않게 조합
n = int(input())
print((n*(n-1)*(n-2))//6)
print(3)

#7 -> a0가 음수일 경우를 생각해여함
# a0가 음수일 때, 성립하기 위해서는 f의 n계수가 g의 n계수보다 작거나 같아야한ㄷ
# 즉, a1 <= c
# a0이 음수인 경우 : 처음엔 만족한 결과가 나오다가 n이 커질수록 결과를 만족하지 못함 => 예외처리
# a1이 음수인 경우 : 처음부터 결과를 만족하지 않다가 커질수록 결과를 만족  => 예외처리 해줄 필요X
a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

if (a1*n0+a0 <= c*n0 and a1 <= c):
    print(1)
else:
    print(0)