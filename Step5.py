#1 -> input는 문자열
S = input()
i = int(input())
print(S[i-1])


#2
S = input()
print(len(S))


#3
T = int(input())
for i in range(T):
    S = input()
    print(S[0]+S[-1])
    
    
#4
# ord(문자) : 아스키 코드를 반환
# chr(숫자) : 숫자에 맞는 아스키 코드를 반환 (숫자->문자)
print(ord('A'))
print(ord('9'))  # 9를 숫자가 아닌 문자로 받아서, 그의 아스키 코드를 반환
S = input()
print(ord(S))


#5
N = int(input())
S = input()
sum = 0
for i in range(N):
    sum += int(S[i])
print(sum)


#6
S = input()
C = 'abcdefghijklmnopqrstuvwxyz'
for i in C:
    if i in S :          #만약 S안에 i가 들어있다면
        print(S.index(i), end=' ')
    else:
        print(-1,end=' ')
        
#6
##find함수 이용
# find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력한다.
#만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수이다.
S = input()
C = 'abcdefghijklmnopqrstuvwxyz'
for i in C:
    print(S.find(i), end=' ')
    
    
#7
T = int(input())
for i in range(T):
    R,S = input().split()
    R = int(R)
    for x in range(len(S)):
        print(S[x]*R, end='')
    print("")    # 줄넘김
    
    
#8 -> split 함수 이용
S = input().split() #공백을 기준으로 분리
print(S)            #['문자','문자', , , ] 형태
print(len(S))       #리스트의 갯수로, 문자가 몇개인지


#9 정수형은 인덱스로 사용 x -> 문자열형태에서 앞뒤를 바꿔주고, 정수형으로 바꿔서 비교
A,B= input().split()
res_A = A[::-1]        #[::-1] 역순 
res_B = B[::-1]
print(max(int(res_A),int(res_B)))


#10 문자열은 ==, != 로 비교X -> in or not in으로!
#방법 1
S = input()
time = 0

for i in S:
    if i in "ABC":   #i가 ABC중에 있다면
        time += 3
    elif i in "DEF":
        time += 4
    elif i in "GHI":
        time += 5
    elif i in "JKL":
        time += 6
    elif i in "MON":
        time += 7
    elif i in "PQRS":
        time += 8
    elif i in "TUV":
        time += 9
    elif i in "WXYZ":
        time += 10
    else:
        time += 11
print(time)

#방법2 
#리스트이용
list = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S = input()
time = 0

for i in range(len(S)):    #S문자열에서 문자하나씩
    for j in list:         #리스트에서 문자열하나씩
        if S[i] in j :     #S의 문자가 문자열에 들어간다면
            time += list.index(j)+3 #해당 문자열의 인덱스값(번호값)+3(기본3초추가)
print(time)