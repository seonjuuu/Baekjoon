#1
print("         ,r\'\"7")
print("r`-_   ,\'  ,/")
print(" \\. \". L_r\'")
print("   `~\\/")
print("      |")
print("      |")


#2 -> 리스트간의 뺄셈은 지원X
chess = [1,1,2,2,2,8]
A = list(map(int,input().split()))
for i in range(len(A)):
    print(chess[i]-A[i], end=" ")
    
    
#3 -> 뒤 공백은 생각X !! 
# 별이 증가하는 부분과 줄어드는 부분 나눠서
# range(, ,-1) : 역순으로 출력
# 별은 2N-1개가 찍힘 (N=줄)

# N입력받기
N = int(input())

# 별의 개수가 증가하는 부분
for i in range(1,N+1):
    print(" " * (N-i) + "*" * (2*i-1))
    
# 별의 개수가 감소하는 부분
for i in range(N-1,-0,-1):
    print(" " * (N-i) + "*" * (2*i-1))