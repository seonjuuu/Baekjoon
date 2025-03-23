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

    
#7 -> sort 함수 기준 정하기
#이차원 리스트 -> [[x1,y1],[x2,y2] . . .] 
#list.sort() = x을 기준으로 정렬 -> y을 기준으로 정렬
N = int(input())
list = []

for i in range(N):
    x,y = map(int,input().split())
    list.append([x,y])

list.sort()  
for i in range(N):  
    print(list[i][0], list[i][1])
# for i in list: 
# print(i[0], i[1]) 

#8
#두번째 값을 기준 -> sort 함수의 기준을 바꿔야함
#list.sort(key = lambda x: (x[1], x[0]))
#경우1
N = int(input())
list = []
for i in range(N):
    x,y = map(int,input().split())
    list.append([y,x])    # y,x 순서바꿔서 append

list.sort() # 순서바꿨기에, y가 x보다 먼저 -> y기준으로 정렬 후 x로 정렬
for i in range(N):
    print(list[i][1],list[i][0])

#9
#기본 list.sort() -> 사전순으로 정렬(sort 정렬이 문자까지 정렬)
#정렬 우선순위의 역순
#정렬 순서를 주의해야 되는데, 상위 조건 A와 하위 조건 B가 있으면 먼저 B로 정렬을 한 후에 A로 정렬을 해야 원하는 결과를 얻을 수 있다. -> 최종적으로 원하는 출력의 정렬은, A의 조건이므로, A를 마지막에!
N = int(input())
list = []
for i in range(N):