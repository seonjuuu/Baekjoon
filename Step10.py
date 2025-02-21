#1
A = int(input())
B = int(input())
print(A*B)

#2
x, y, w, h = map(int,input().split())
dis = [x,y,w-x,h-y]
print(min(dis))