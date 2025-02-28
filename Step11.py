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