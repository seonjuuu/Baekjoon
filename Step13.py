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

N = int(input())
list = []
for i in range(N):
    k = int(input())
    list.append(k)
list.sort()
for i in list:
    print(i)
    
    
#6
N = list(map(int,str(input)))
N.sort(reverse=True)    # sort=정렬 / [::-1] = 자리옮기기(정렬x)
for i in range(len(N)):
    print(N[i],end="")