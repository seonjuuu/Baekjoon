#1
A, B, C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#2
# 최대공약수 
# 1. 각 약수 구하기 2. 공통 약수 찾기 3. 최대