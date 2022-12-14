# Chapter04-01
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급


# Non Comprehending Lists
chars = '+_)(*&^%$#@!~)'    # str: 플랫형이면서 불변형
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))   # 유니코드

# Comprehending Lists - 지능형 리스트
# 속도 약간 우세
code_list2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
# filter(익명함수/함수, 리스트/자료구조형)

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
# 유티코드를 문자형으로
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()


# Generator 생성 
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)   # 값 들을 생성하지 않은 상태. 첫 번째 값을 반환할 준비가 됨.
# Array
array_g = array.array('I',  (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())     # array를 list로 반환

print()
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print(s)


print()
print()

# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'      # 모든 list의 첫 번째 index가 다 바뀜

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])      # id값이 모두 다른 list id, 주소값이 다름.
print([id(i) for i in marks2])      # 하나의 주소 값이 네 개로 복사가 됐음.