a = [242, 256, 237, 223, 263, 81, 46]   # 리스트에 유동 인구 데이터 초기화
print('A=', a);                         # 출력하기

#그래프를 그리기 위한 외부 모듈 선언
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name=font_manager.FontProperties(fname='c:/Windows/Fonts/H2MKPB.TTF').get_name()
rc('font', family=font_name)                         # 그래프 제목에 한글 표시하기

x_data=['MON','TUE','WED','THR','FRI','SAT','SUN']         # x축에 표시할 제목 리스트에 저장
# 주중 데이터만으로 합과 평균 구하기
weekday_size=5                                              # 주중이므로 5
weekday_sum=0                                               # 합이 저장될 변수 초기화
weekday_avg=0                                               # 평균이 저장될 변수 초기화

for i in range(0, weekday_size):                            # 인덱스 i는 0부터 시작하여 weekday_size번 반복하기
	weekday_sum=weekday_sum+a[i]                            # 주중 유동 인구수의 총합 구하기

weekday_avg = weekday_sum/weekday_size                      # 주중 인구수 평균 구하기

# 계산한 총합과 평균 출력하기
print('weekday Data = ', a[0:5])                            # 주중 데이터 출력하기
print('weekday Sum = ', weekday_sum)                        # 합 출력하기
print('weekday Average = ', weekday_avg)                    # 평균 출력하기
# 그래프의 제목 붙이기
plt.title('주중 유동 인구수 데이터', fontsize=16)         # 그래프 제목
plt.xlabel('요일',fontsize=12)                        # x축 제목
plt.ylabel('유동 인구수',fontsize=12)                  # y축 제목
# 꺽은선 그래프 그리기
plt.plot(x_data, a)
plt.scatter(x_data[0:weekday_size], a[0:weekday_size], c='red', edgecolors='none',s=50)
plt.show()