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