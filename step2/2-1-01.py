

# 은재가 조사한 일주일간 유동 인구 데이터 (월요일~일요일)

"""
은재가 조사한 일주일간 유동 인구 데이터 (월요일~일요일)
"""

'''
은재가 조사한 일주일간 유동 인구 데이터 (월요일~일요일)
'''

a = [242, 256, 237, 223, 263, 81, 46]   # 리스트에 유동 인구 데이터 초기화
print('A=', a);                         # 출력하기


"""
# 인덱스 변수: i, 범위: [begin, end], 반복 패턴: operation

# 파이썬의 반복문으로 표현하기
# 파이썬의 리스트는 인덱스가 0부터 시작하므로 수열의 첫째항의 인덱스가 (begin-1)부터 시작함

for i in range(begin-1, end);
	operation
"""

# 데이터의 합과 평균 구하기
n=len(a)                                # 수열 a항 개수 구하기: 7개
my_sum=0                                # 합을 저장할 변수를 0으로 초기화
my_avg=0                                # 평균을 저장할 변수를 0으로 초기화
i=0                                     # 수열 항의 인덱스, 파이썬은 첫 번째 수열항의 인덱스는 0부터 시작함

for i in range(0, n):                   # 인덱스 값은 0부터 시작하여 (n-1)까지 반복하기
	my_sum = my_sum+a[i]                # 총합 구하기

my_avg=my_sum/n                         # 평균 구하기
print('Total SUm : ', my_sum);          # 총합 출력하기
print('Total Average : ', my_avg);      # 평균 출력하기