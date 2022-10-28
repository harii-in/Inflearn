# 모듈 사용 실습

import sys

print(sys.path)
print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('\\wsl.localhost')

# print(sys.path)

import chapter06_02

print(chapter06_02.add(10, 1000000))