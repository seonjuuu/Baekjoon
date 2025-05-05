#1
#해결방법 : 스택 하나를 이용하여 한 문자열씩 처리
#경우들
# 문자열 : 공백을 만나거나(내부공백X) / "<"만나면 한 문자열 끝
# 1. "<" : 한 문자열 끝임, 스택에 들어있는 문자들을 역순으로 ans에 추가("<"를 스택에 추가하기 전에!!) -> "<" 와 태그 안의 문자들을 스택에 추가
# 2. ">" : 태그의 끝, ">"를 스택에 추가하여 스택의 문자를 차례대로 다 빼기(pop(0))
# 3. 공백 & 외부 : 한 문자열 끝, 스택에 들어있는 문자들을 역순으로 ans에 추가(공백은 나중에 ans추가 !!)
S = input() #split(X) -> 문자 사이의 공백이 필요
stack = []
ans = ""
check = "outer"   # 태그안의 여부를 체크
for i in S:
    if (i == "<"):
        check = "inter"
        for _ in range(len(stack)):  #스택에 들어있는 문자들을 역순(pop())으로 다 빼기
            ans = ans + stack.pop()
            
    stack.append(i) 

    if (i == ">"): # 태그 끝. "<"부터 들어있는 스택을 다 비우기. 차례대로(pop(0))
        check = "outer"  # 태그의 끝이므로 다시 외부
        for _ in range(len(stack)):
            ans = ans + (stack.pop(0))

    if i == " " and check == "outer":
        stack.pop() #방금 들어간 공백을 제거
        for _ in range(len(stack)):  # 문자열들만 뒤집어서 ans에 더함
            ans = ans + stack.pop()
            ans = ans + " "