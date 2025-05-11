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