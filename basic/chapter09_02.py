# Chapter09-2
# CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Header Skip
    
    # 객체 확인
    print(reader)
    
    # 타입 확인
    print(type(reader))
    
    # 속성 확인
    print(dir(reader))  # __iter__이 있으므로 for문 에서도 사용 가능
    print()

    for c in reader:
        # print(c)      # 내용 확인
        
        # 타입 확인 - 리스트
        print(type(c))
        
        # list to str
        print(' '.join(c))

# 예제2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 선택
    # 잘못된 구분자 이용시 하나로 가져옴. 구분x

    for c in reader:
        print(c)

# # 예제3 (Dict 변환)
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인  for문 및 반복문에서 사용 가능
    print()

    for c in reader:
        for k, v in c.items():      # items는 key와 value를 반환
            print(k, v)
        print('-------------')

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))
    # 타입 확인
    print(type(wt))

    for v in w:
        wt.writerow(v)

# 예제5
with open('./resource/write2.csv', 'w', newline='') as f:
    
    # 필드명
    fields = ['One', 'Two', 'Three']
    
    # Dict Writer 선언
    wt = csv.DictWriter(f, fieldnames=fields)
    
    # Herder Write
    wt.writeheader()

    for v in w:
        wt.writerow({'one': v[0], 'two': v[1], 'three': v[2]})