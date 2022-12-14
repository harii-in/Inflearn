# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

시퀀스: 반복을 처리할 수 있고 어떤 순서가 있음.
'''

# 데이터 타입
str1 = "Python"
bool = True
str2 = "Anaconda"
float_v = 10.0    # 10 != 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0      # Key : Value
}
tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+ 
- 
* 
/ 
// : 몫 
% : 나머지
abs(x) : 절대값
pow(x, y) : x ** y : 제곱 -> 2 ** 3 == pow(2, 3) = 8
int(x) 
float(x) 
complex(x)
....
"""

# 정수 선언
i = 77
i2 = -14
big_int = 999999999999999999999999999999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939

# +
print(">>>>> + ")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 

# -
print(">>>>> -")
print("i1 - i2: ", i1 - i2) 
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)

# *
print(">>>>> *")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)

# /
print(">>>>> /")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)

# //
print(">>>>> //")
print("i2 // i1: ", i2 // i1) 
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)

# %
print(">>>>> %")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)

# **
print(">>>>> **")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)


# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))  # 정수 -> 실수
print(int(c))  # 실수 -> 정수
print(int(d))  # 실수 -> 정수
print(int(True))  # Bool -> 정수
    # True : 1, False : 0
print(float(True))  # Bool -> 정수
print(int(False))  # Bool -> 정수
print(float(False))  # Bool -> 정수
print(complex(3))  # 정수 -> 복소수
print(complex('3'))  # 문자 -> 숫자형(복소수)
print(complex(False))  # Bool -> 복소수

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)   # 몫, 나머지
print(x, y)
print(pow(5, 3))

#외부 모듈
import math

#ceil
print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수
#pi
print(math.pi)