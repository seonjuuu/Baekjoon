# import sys
# input = sys.stdin.readline 을 적어줘야 빠름

#1
list = []
N = int(input())
for i in range(N):
    a = int(input())
    list.append(a)
    
list.sort()
for i in range(N):
    print(list[i])    

#2
list = []
for i in range(5):
    a = int(input())
    list.append(a)

list.sort()
print(sum(list)//5)
print(list[2])

#3
N, k = map(int,input().split())
x = list(map(int,input().split()))
x.sort(reverse=True)   # 내림차순
print(x[k-1])
#4
#시간초과 
#import sys
#input = sys.stdin.readline()
import sys
input = sys.stdin.readline