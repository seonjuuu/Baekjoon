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