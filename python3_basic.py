'''
파이썬 기본적인 자료형
1. 숫자형
2. 문자열
'''

'''
1. 숫자형
'''
num1 = 123
num1 = -123
num1 = 0
print(num1)

num2 = 1.2
num2 = 4.24e-2  # 4.24 * 10의 -2승
print(num2)

# 연산
num1 = 2
num2 = 4
print(num1 + num2)  # 더하기
print(num1 - num2)  # 빼기
print(num1 * num2)  # 곱하기
num3 = num2 / num1  # 나누기
print(num3 == 2)
print(num2 % num1)  # 나머지 반환
print(num2 // num1) # 몫 반환
print(num1 ** num2) # 제곱
print('\n');4


'''
2. 문자형
'''
txt1 = "Hello 'World'"
txt2 = 'Hello "World"'
txt3 = '\tHello \n"World"'
multiline1 = """
Hello 
World
"""
multiline2 = '''
Hello 
World
'''
print(txt1)
print(txt2)
print(txt3)
print(multiline1)
print(multiline2)
print('\n');

# 문자열 연산
print(txt1 + txt2)
print(txt1 * 3)
print('\n');

# 문자열 길이, 인덱싱, 슬라이싱
txt4 = "i am hybrid app developer parkdongjo"
print(len(txt4))    # 길이
print(txt4[3])      # 인덱싱
print(txt4[-2])
print(txt4[-0])
print(txt4[0])
print('\n');
print(txt4[0:4]) # 슬라이싱 0 <=  < 4
print(txt4[5:8])
print(txt4[5:])
print(txt4[:10])
print(txt4[10:-10])

# 문자열 포맷팅
# %s(문자열) / %c(문자 1개) / %d(정수) / %f(부동소수)
# 방법 1
txt5 = "hello %d world"
txt6 = "hello %s world"
txt7 = "hello %s world %d"
print(txt5 % 10)
print(txt6 % "charles")
print(txt7 % ("charles", 20))

# 방법 2
txt8 = "hello {0} come {1}"
print(txt8.format("world", "on"))
txt9 = "hello {txt} come {num}"
print(txt9.format(txt="world", num=5))

# 방법 3
dic1 = {'txt': "hello", 'num': 5}
print(f"hello {dic1['txt']} world come {dic1['num'] + 2}")
print('\n')


## 문자열 관련 함수들
print(txt4.count("a"))
print(txt4.find("a")) # 처음나온 문자 위치 반환, 없으면 -1
print(txt4.index("a")) # 처음나욘 문자 위치 반환, 없으면 error
print("/".join(txt4))  # 문자열 삽입
print(txt4.upper()) # 소문자를 대문자로 변환
print(txt4.lower()) # 대문자를 소문자로 변환
print(txt4.strip()) # 양쪽 공백 제거
print(txt4.replace("parkdongjo", "parkcharles")) # 지정한 문자열을 변경
print(txt4.split()) # 공백을 기준으로 배열에 문자열을 나누어 준다
print(",".join(txt4).split(",")) # 문자열의 각각의 문자 사이에 ','를 삽입한다.
