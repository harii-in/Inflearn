# Chapter02-1
# 파이썬 완전 기초
# Print 사용법


# 기본 출력
print('Python STart!')
print("Python STart!")
print()

print('''Python STart!''')
print("""Python STart!""")
print()

# seperator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '1234', '5678', sep = '-')
print('python', 'google.com', sep = '@')
print()

# end 옵션
print('Welcome to', end = ' ')
print('IT news', end = ' ')
#print문은 자동으로 줄바꿈은 해주지만, end가 들어가면 end 옵션에 들어간 문자로 다음 print문에 이어짐.
print('Web Site')

# file 옵션
import sys
print('Learn Python', file = sys.stdout)
print()

# format 사용(d:3, s:'Python', f=3.14)
print('%s %s' %('one', 'two'))
print('{0} {1}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' %('nice'))
print('{:>10}'.format('nice'))

print('%-10s' %('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' %('nice'))
print('%.5s' %('python study'))
print('{:10.5}'.format('python study'))

print()

# %d
print('%d %d' %(1, 2))
print('{} {}'.format(1, 2))

print('%4d' %(41))
print('{:4d}'.format(42))

print()

# %f
print('%f' %(3.14334343434))
print('{:f}'.format(3.14334343434))

print('%06.2f' %(3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))