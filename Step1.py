#1 : Hello world! 출력하기'
print("Hello World!")

#2 -> 입력받기 : input() /  / split() : 띄어쓰기를 기준으로 구분 
# -> A,B = int(input().split()) -> 불가능 -> 이유 : int 함수는 리스트를 정수형으로 바꿔줄수없음 -> map함수 사용
# map -> map(각요소에 적용할 함수, 함수를 적용할 데이터집합) -> 정수로 변환 : map(int,input(),split())

#split() 예시
A,B = input("입력:").split()  #입력받은것은 정수가 아니므로 사칙연산 불가능 (A+B X) -> int로 변경해줘여함
print("A:",A)
print("B:",B)
print()

#2번문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
A,B = map(int,input("두 정수 입력:").split())
print("정수합:",A+B)

#3
A,B = map(int,input().split())
print(A-B)

#4
A,B = map(int,input().split())
print(A*B)

#5
A,B = map(int,input().split())
print(A/B)

#6 -> 사칙연산 : A+B, A-B, A*B, A/B(몫), A%B(나머지)
A,B = map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)

#7 
A = input()      #input은 원래 문자형
print(A+"??!")

#8 -> 서기연도 = 불기연도 - 543
A = int(input())
print(A-543)

#9
A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#10 -> 문자열 입력 함수 input()으로 A와 B에 저장할 정수값을 (문자열로) 입력받아 
#      A만 정수형으로 변환해주었고 B는 문자열 형태(=리스트형태로) 남겨두었습니다 -> 리스트에서 한자리씩[]떼기 -> 곱셈할때 정수형으로 비꾸기
A=int(input())
B=input()
print(A*int(B[2]))         # 리스트 -> list = [list[0],list[1]. . . .]
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))

#11
A,B,C = map(int,input().split())
print(A+B+C)

#12
#역슬래시(\) 출력 : \\(연속)  / ' or " 출력 : \' or \"  ("'" -> ' 출력)
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

#13
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")