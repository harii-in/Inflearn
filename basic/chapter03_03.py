# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])     # Base
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
# 같은 id 값
temp = c
print(temp, c)
print(c == temp)
print(id(temp))
print(c)

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']] -> 슬라이싱 범위 지정 시 원소로 들어감. 
print('c - ', c)
c[1] = ['a', 'b', 'c']  # 자리 지정 후 리스트를 넣으면 리스트로 들어감. 중첩.
print('c - ', c)
c[1:3] = []     # 비움
print('c - ', c)
del c[2]        # 삭제
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)     # 끝에 데이터 수정. 마지막 끝부분에 데이터 삽입.
print('a - ', a)
a.sort()        # 오름차순으로 정렬
print('a - ', a)
a.reverse()     # 내림차순으로 정렬
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)  # 두 번쨰 위치에 7을 넣을거야. 그 뒤는 밀림.
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[9543]
a.remove(10)
print('a - ', a)
print('a - ', a.pop())  # 기존에 있던 list에서 마지막에 있던 원소를 가져오고 기존의 리스트에서 그 원소를 제거.
print('a - ', a)
print('a - ', a.pop())  # LIFO (Last-In-First-Out)
print('a - ', a)
print('a - ', a.count(4))   # 4의 개수
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)