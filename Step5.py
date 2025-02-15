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