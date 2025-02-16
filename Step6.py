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