#1
while(1):
    A, B = map(int,input().split())
    if (A == B):
        break
    elif(B%A == 0):
        print("factor")
    elif(A%B == 0):
        print("multiple")
    else:
        print("neither")