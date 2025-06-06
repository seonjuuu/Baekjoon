#1 후위 표기식
# 연산자 -> 우선순위 (스택 안에 우선순위가 더 높거나 같은 연산자가 들어 있으면 먼저 꺼내 출력하고 그 다음에 스택에 넣는다. 아니라면 그냥 append)
S = input()
num = {"(":0, ")":0, "+":1, "-":1, "*":2, "/":2}
stack = []
ans = ''

for i in S:
    if i.isalpha():  #피연산자인 경우 (알파벳으로 가정)
        ans = ans+i
    elif i == "(":
        stack.append(i)
    elif i == ")":  # 닫는 괄호 처리
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.pop()  # 여는 괄호 제거
    else:  # 연산자인 경우
        while stack and num[i] <= num[stack[-1]]:  # 우선순위 비교
            ans += stack.pop()
        stack.append(i)  # 현재 연산자 스택에 추가
# 스택에 남은 연산자를 결과에 추가
while stack:
    ans += stack.pop()        
print(ans)


#2
#핵심 -> 아스키코드 이용(바로 계산) / 결과값을 다시 append

N = int(input())
S = input()
stack = []
num = []
for i in range(N):
    num.append(int(input()))

for i in S:
    if i.isalpha():
        stack.append(num[ord(i)-65]) # A = [0] # 알파벳 형태가 아닌 피연산자값의 형태
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        # 계산한 값을 다시 스택에 넣어줌 !!
        if i == "+": 
            stack.append(str1+str2)
        elif i == "-":
            stack.append(str1-str2)
        elif i == "*":
            stack.append(str1*str2)
        elif i == "/":
            stack.append(str1/str2)

print('%.2f' % stack[-1])  # 소수점 둘째 자리까지 # 결과값은 스택에 남아있음 !!

#3
S = input()
result = [0] * 26
for i in S:
    result[ord(i)-97] += 1  # 소문자 a = 97

print(*result)  # 리스트를 공백으로 구분하여 출력

#4
# 다른 방법 : C = 'abcdefghijklmnopqrstuvwxyz'
S = input()
result = [-1]*26   
for i in range(len(S)):
    if result[ord(S[i])-97] == -1: # 처음 등장하는 위치이므로 조건문 추가
        result[ord(S[i])-97] =  i
print(*result)

#5
#문제 -> n이 주어지지 x -> 무한루프
#무한루프를 멈춰줄 코드 필요 -> if not text
import sys
while True:
    text = sys.stdin.readline().rstrip('\n') # rstrip('\n') = 줄바꿈 문자 제거

    if not text:  # 아무것도 입력되지 않았을 때는 text이 아무것도 아니기에 if not 구문에서 걸러진다.
        break

    # 소문자, 대문자, 숫자, 공백
    l, u, d, s = 0, 0, 0, 0
    for i in text:
        if i.islower():  # 소문자 확인함수
            l += 1
        elif i.isupper():  # 대문자 확인함수
            u += 1
        elif i.isdigit():  # 숫자 확인함수
            d += 1
        elif i.isspace():  # 공벡 확인함수
            s += 1

    print(l, u, d, s)

# 코드2 -> 아스키코드 이용
import sys 
while True :
    text = sys.stdin.readline().rstrip("\n")

    if not text:
        break

    lower, upper, num, blank = 0,0,0,0
    for i in text :
        if i == " " :
            blank += 1
        elif 65 <= ord(i) <= 90 :
            upper += 1
        elif 97 <= ord(i) <= 122 :
            lower += 1
        else :
            num += 1
    print(lower,upper,num,blank)       

#6
S = input()
print(len(S))

#7
text = input()
ans = ''
for i in text:
    if i.isupper():  # 대문자
        ans += chr((ord(i) - 65 + 13) % 26 + 65)
    elif i.islower():  # 소문자
        ans += chr((ord(i) - 97 + 13) % 26 + 97)
    else:  # 알파벳이 아닌 문자
        ans += i
print(ans)

#8
a, b, c, d = input().split()  #바로 변수에 대입
a = a+b  # 문자열의 합
c = c+d
print(int(a)+int(c))  #int형으로 바꿔 덧셈

#9
s = input()
answer = []

for i in range(len(s)):
    answer.append(s[i:])  #s[0:] -> 0번째부터 끝까지, s[1:] -> 1번째부터 끝까지, . . 

answer.sort()

for i in answer:
    print(i)
    
