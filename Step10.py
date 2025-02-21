#1
A = int(input())
B = int(input())
print(A*B)

#2
x, y, w, h = map(int,input().split())
dis = [x,y,w-x,h-y]
print(min(dis))

#3 -> x좌표, y좌표 수가 2개씩
X = []
Y = []
for i in range(3):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
    
for x in X :
    if X.count(x) == 1:
        print(x, end=" ")
        break
    
for y in Y :
    if Y.count(y) == 1:
        print(y)
        break