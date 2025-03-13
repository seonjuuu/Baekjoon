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