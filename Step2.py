#1
A,B = map(int,input().split())
if(A>B):
    print(">")
elif(A<B):
    print("<")
else:                    #elif(A==B) -> 같다(==)
    print("==")
    

#2
score = int(input())
if(90 <= score <=100) :
    print("A")
elif(80 <= score <= 89) :
    print("B")
elif(70 <= score <= 79) :
    print("C")
elif(60 <= score <= 69) :
    print("D")
else:
    print("F")
    

#3
year = int(input())
if(year%4 == 0):
    if(year%100 != 0 or year%400 == 0):
        print("1")
    else:
        print("0")
else:
    print("0")



#4 
x = int(input())
y = int(input())
if(x>0) :
    if(y>0) :
        print("1")
    else :
        print("4")
else:
    if(y>0) :
        print("2")
    else:
        print("3")



#5 
H,M = map(int,input().split())
if(M<45):
    if(H==0):    #분이 45보다 작을때만 0시에 영향을 미침
        H = 23
    else:
        H = H-1
    M = M+60
print(H, M-45)



#6
A,B = map(int,input().split())
C = int(input())
if(B+C >= 60):
    A = int(A+(B+C)/60)
    if(A>23):
        A = A-24
    B = (B+C)%60  
else:
    B = B+C
    
print(A,B)



#7
A,B,C = map(int,input().split())
if(A==B and B==C):
    print(10000+(A)*1000)
elif(A!=B and A!=C and B!=C):
    m = max(A,B,C)
    print(m*100)
else:                      #같은 눈이 2개
    if(A==B or A==C):
        print(1000+A*100)
    else:                   #B와C가같은경우    
        print(1000+B*100)
        

#7-1     
a, b, c = map(int, input().split())
if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))
    
        