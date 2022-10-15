# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1), type(str2), type(str3), type(str4))
# 문자열 길이
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

"""

# I'm Boy
print("I'm Boy")
print('I\m Boy')
print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String :  역 슬러시 자체를 신경을 안 씀
raw_s = r'D:\Python\test'
print(raw_s)
print()

# 멀티라인 출력
# 역슬래시 사용
multi_str1 = \
'''
Strin
Multi line
Test
'''
print(multi_str1)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print(str(complex(12)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha ...)
print("Capitalize: ", str_o1.capitalize())  # 첫글자를 대문자로 변환
print("endswith?: ", str_o2.endswith("s"))  # 끝 글자가 s로 끝나는가?
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('thon', ' Good'))    # A, B -> A를 찾아서 B로 바꿔줘
print("split: ", str_o4.split(' '))  # Type 확인
print("sorted: ", sorted(str_o1))  # reverse=True, 문자열을 입력받아서 어던 기준에 맞게 정렬에서 리스트 형태로 반환한다.
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))
print("split: ", str_o4.split(' '))     # 'a' -> a 를 기준으로 분리

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 

# 출력
for i in im_str:
    print(i)


# 슬라이싱
str_sl = 'Nice Python'

# 슬라이싱 연습
print(str_sl[0:3])  # 0 1 2
print(str_sl[5:])   # [5:11]
print(str_sl[:len(str_sl)])     # str_sl[:11]
print(str_sl[:len(str_sl) - 1]) # str_sl[:10]
print(str_sl[:])
print(str_sl[1:9:2])    # 1부터 9까지 가져오는데 2개 단위로 가져와라
print(str_sl[-4:-2])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])     # 음수는 오른쪽에서 왼쪽으로 -> 거꾸로 출력됨


# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))   # 문자를 마스키코드로
print(chr(122)) # 아스키코드를 문자로