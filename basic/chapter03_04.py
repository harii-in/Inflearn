# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중목o, 수정x, 삭제x) # 불변

# 선언
a = ()
b = (1, )   # 튜플 원소가 하나일 때는 ,를 찍어줘야 함.
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Chptine')
e = (100, 1000, ('Ace', 'Base', 'Chptine'))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1]))

# 수정x
# d[0] = 1500

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언패킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')    # 네 개의 원소를 하나로 묶음.
print(t)
print(t[0])     # 인덱싱을 이룸.
print(t[-1])    # 하나씩 내부 원소를 확인 가능

# 언팩킹1
(x1, x2, x3, x4) = t    # 4개의 원소가 각각 변수로 할당됨.

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)