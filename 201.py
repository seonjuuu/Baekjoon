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
            ans = ans + " "  # 마지막에 공백 살려주기

if stack: # 마지막 문자열을 위에서 append만 해줌. 루프 종료 후 스택에 남아 있는 문자를 처리, 즉 입력 문자열의 마지막이 공백이나 태그로 끝나지 않는 경우 / ex> one1 two2 three3 4fourr 5five 6six
    for _ in range(len(stack)):
        ans += stack.pop()

print(ans)

#2 -> 레이더 기준
#레이더가 영향을 주는 막대기의 개수 = 스택에 들어있는 여는괄호의 개수
# 1) 레이더인 경우 :  스택에 남아있는 열린 괄호의 개수
# 2) 막대의 끝인 경우 : 이때는 레이저에 의해 짤리고 남은 막대기의 끝이 되므로 막대기는 한 개만 추가
# 총 = (각 레이더가 영향을 주는 막대 개수의 합) + (막대의 끝인 경우 +1) (=막대 개수)
S = input()
stack = []
cnt = 0
for i in range(len(S)):
    if S[i] == "(":
        stack.append("(")
    else:
        if S[i-1] == "(":  #레이더인 경우
            stack.pop()
            cnt = cnt+len(stack)  # 각 레이더가 영향을 주는 막대 개수
        else:
            if S[i-1] == "(":  #레이더인 경우
                stack.pop()
                cnt = cnt+len(stack) # 각 레이더가 영향을 주는 막대 개수
            else:     # 막대의 끝인 경우
                stack.pop()
                cnt = cnt+1  # 막대의 끝인 경우 +1
print(cnt)


#3 -> 스택
# stack[1,2] -> [1]보다 [2]의 값이 작다는 것 -> 이때, for문을 통해 [2]와 [3]의 값을 비교하는데, [3]의 값이 [2]보다 작으면, [3]과 [1]은 비교하지 않고 3이 스택에 append되는데, 상황은 [1]보다 [2]이 더 작고, [2]보다 [3]이 더 작은것이므로 [1]과 비교할 필요가 없다 !!
# 오큰수는 가장 왼쪽값이므로 큰값을 찾으면, 그값이 바로 오큰수!
# 다음 값이 오큰수가 아닌데, 나중에 오큰수가 나올 경우 -> 일단, 스택에서 해당 인덱스를 pop하지 않고, for문에서 자리를 하나씩 옮겨, 그 자리의 값이 오큰수가 되는지 확인. 
# for문 -> 오큰수는 오른쪽의 값이므로(인덱스1부터 시작) / 입력받은 리스트의 값을 기준으로 아직 오큰수를 찾지 못한, 스택에 들어있는 인덱스자리의 값을 비교하여 오큰수면 
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
NGE= [-1]*N  # 오큰수가 없을 경우 -1로 표시해야하니 [-1] * N 사이즈의 리스트
stack = [0]  # 0번 인덱스