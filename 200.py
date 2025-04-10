#1 스택

import sys
input = sys.stdin.readline
N = int(input())
stack = []
for i in range(N):
    command = input().split() # command[0] command[1]
    
    if command[0] == "push":
        stack.append(command[1])
        
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])   #stack[len(stack)-1] = stack[-1] / print(stack.pop()) - 한줄로 가능, list.pop() 
            del(stack[len(stack)-1])
    
    elif command[0] == "size":
        print(len(stack))
    
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
        
#2 단어 뒤집기
N = int(input())

for i in range(N): 
    word = list(input().split())
    new = []
    for j in range(len(word)):
        new.append(word[j][::-1]) #reverse(x)  -> reverse와 [::-1] 차이점
    
    for k in new:
        print(k, end=" ")

#3
# 스택이용
# "(" -> 추가
# ")" -> (를 하나 삭제 
# 결과적으로 0이 되어야 yes
# ( 가 입력되면 append로 추가를 하고, ) 가 입력되면 stack에 있던 ( 를 pop하여 꺼내준다. 단, ) 가 들어왔을 때 stack에 꺼낼 ( 가 있어야 하는데 없다면 짝이 맞지 않는 것이므로 ) 를 추가한 뒤에 break를 하여 반복문을 멈춘다. 여기서 ) 를 추가하는 것이 아니라 사실 아무거나 추가해도 된다. 그 이유는 마지막에 결국 stack의 길이가 0이 아닐 때에 NO를 출력하므로 아무거나 넣어서 stack의 길이가 0이 아니게 만들면 된다. stack의 길이가 0이면 ( 와 ) 가 짝이 맞다는 것이므로 YES를 출력한다.
N = int(input())
for i in range(N):
    v = input()
    stack = []
    for j in range(len(v)):  
        if v[j] == "(":
            stack.append("(")
        else:
            if len(stack) == 0 :
                stack.append(")")
                break
            stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

#4 스택수열
n = int(input()) 
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:  # 입력한 수를 만날 때 까지 오름차순으로 push / 들어있는 수(이전 num보다 작은수들)는 while의 조건에 맞지 않으므로 pass -> if문으로 ex> num = 3일때
        stack.append(cur)
        answer.append("+")
        cur += 1      # 다음 num은 cur이 (이전num+1)의 값부터 num까지 수를 push
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:  # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()       # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                 # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")       # 왜냐하면 TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        flag = 1           # flag = 1을 적어 출력할 때, 이 경우의 answer은 출력하지 않는다.
        break
    
if flag == 0: