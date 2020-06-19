print("융합콘텐츠학과 김루희 1745031")
print("문제 : 광주광역시에서 고령화 인구가 가장 많은 곳은 어디일까요?\n") #찾고 싶은 정보

import numpy as np #numpy 라이브러리 불러오기
#데이터 읽어오기
import csv
f=open('age_v2.csv', encoding='cp949') #맥북은 encoding을 해주지 않으면 오류 발생
data=csv.reader(f)
next(data) #헤더 부분 제거
name = input('찾고자 하는 지역의 이름을 입력해주세요! : ') #사용자에게 찾고자 하는 지역 입력받기
for row in data: #데이터를 한 줄씩 읽어오기
    if name in row[0]: #행정구역에 '광주광역시'가 있는지 확인
        result=np.array(row[3:], dtype=int) #0세부터 끝까지 모든 연령을 출력, 문자열을 정수로 변환
print(result) #결과 출력

#age_v2데이터에서 광주광역시 데이터 긁어오기
import pandas as pd #pandas 라이브러리 불러오기
df=pd.read_csv('age_v2.csv', encoding='cp949', header=0, index_col=0)
gwangju=df.iloc[987:1087,67:] #전국 인구 데이터에서 광주광역시 인구만 추출하기
#print(gwangju) 데이터가 슬라이싱 되었는지 확인
gwangju.to_csv('광주광역시 인구.csv') #광주광역시 데이터 csv파일로 저장

#광주광역시 인구csv 데이터에서 긁어오기
df2=pd.read_csv('광주광역시 인구.csv', index_col=0)
#구 통합 인구 삭제하기
df2=df2.drop(['광주광역시 동구 (2911000000)','광주광역시 서구 (2914000000)','광주광역시 남구 (2915500000)','광주광역시 북구 (2917000000)','광주광역시 광산구 (2920000000)'])
#print(df2)
df2['고령화 인구 총합']=df2.sum(axis=1) #열방향으로 총합 계산
print(df2) #결과 출력
totalgwangju=df2.iloc[:,36:] #고령화 인구 총합 column 열만 보기 위해 슬라이싱 해주기
print(totalgwangju) #데이터가 슬라이싱 되었는지 확인
totalgwangju.T #행과 열 바꿔주기
print(totalgwangju.T) #확인

#광주광역시 고령화 인구가 가장 많은 지역 찾기
x=np.array(totalgwangju) #데이터를 넘파이 어레이를 통해 배열로 변경 / x는 numpy array 이름
xmax=np.max(x) #최대값 찾기 / xmax는 찾으려는 최대값
print(name+'의 고령화 인구가 가장 많은 지역의 인구 수는 {}명이다.' .format(xmax)) #결과 출력
xmax_index=np.where(xmax==x)#xmax에 해당하는 xmax_index값 찾기
print('최댓값 {}의 index는 {}이다. ' .format(xmax, xmax_index[0])) #결과 출력
print(totalgwangju.iloc[44]) #결과 출력을 통해 행 번호가 44에 대응하는 값을 찾기 위해 결과 출력
print('광주광역시에서 고령화 인구가 가장 많은 지역은 남구 효덕동이고, 해당 지역의 고령화 인구의 총합은 {}이다.' .format(xmax)) #최종 결과 출력

#광주광역시 고령화 인구 현황 그래프로 표시하기
import matplotlib.pyplot as plt #matplotlib 라이브러리 불러오기
plt.rc('font', family='AppleGothic') #폰트 설정
plt.rcParams['axes.unicode_minus'] = False #한글 깨짐 해결하기
plt.style.use('ggplot') #격자 무늬 표시
totalgwangju.plot(color='green') #꺾은선 그래프로 시각화하기
plt.title(name + '에서 고령화 인구가 가장 많은 지역') #그래프 제목 첨부
plt.xticks(rotation=15, fontsize=5) #길어서 겹치는 x축 label 텍스트를 45도로 회전하고 사이즈를 줄임
plt.show() #그래프 그리기
