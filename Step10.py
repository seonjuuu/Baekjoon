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
    

#4
n = int(input())
print(n*4)


#5
N = int(input())
X = []
Y = []
for i in range(N):
    x,y= map(int,input().split())
    X.append(x)
    Y.append(y)
    
print((max(X)-min(X))*(max(Y)-min(Y)))


#6
a = int(input())
b = int(input())
c = int(input())
if a+b+c == 180:
    if a==b==c==60 :
        print("Equilateral")
    elif a==b or b==c or a==c :
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
    
#7
a, b, c = map(int, input().split())
if a == b == c == 0 :
    break
if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)) :
    print("Invalid")
elif a == b == c :
    print('Equilateral')
elif a == b or b == c or a == c :
    print("Isosceles")
else :
    print("Scalene")