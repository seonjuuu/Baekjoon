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
    
    
#4 
A = input()
if A == A[::-1]:
    print("1")
else:
    print("0")
    
    
#5
A = input()
A = A.upper()
B = []
C = []
for i in range(len(A)):
    if A[i] not in B:
        B.append(A[i])
for i in range(len(B)):
    k = A.count(B[i])
    C.append(k)
max = max(C)    #C에서 max의 갯수가 2개 이상이면 ->?
if C.count(max) >= 2 :
    print("?")
else:
    print(B[C.index(max)])
    
##
#5-1 -> set( ) 이용
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])
  
  
#6->replace함수 사용
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))