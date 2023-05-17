import numpy as np
import pandas as pd

# print(pd.__version__)

# Series Object : 단일한 형태의 객체

# Series Object
# s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
# print(s)  # 리스트를 시리즈형으로 바꿈. 인덱스와 같이 출력됨
# print(s.values)  # 값만 출력
# print(s.index)  # RangeIndex(start=0, stop=5, step=1) 인덱스를 range형태로
# print(s[1])  # 0.25 인덱싱 기능
# print(s[1:4])  # 슬라이싱

# # 인덱스 지정
# s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
#               index=['a', 'b', 'c', 'd', 'e'])
# print(s)
# print(s['a'])  # 0.0
# print(s[['c', 'd', 'e']])  # 특정 인덱스만 불러오기
# print('b' in s)  # true s에 'b'가 index로 있으므로

# s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
#               index=[2, 4, 6, 8, 10])
# print(s)
# print(s[2:])  # 2번째 요소부터 출력
# print(s.unique())  # 유니크한 값만 출력
# print(s.value_counts())  # 값들의 개수
# print(s.isin([0.25, 0.75]))  # 값이 어디에 있는지 boolean형으로 반환해줌

# 딕셔너리
pop_dictionary = {'서울특별시': 9720846,
             '부산광역시': 3404423,
             '인천광역시': 2947217,
             '대전광역시': 1471040,
             '대구광역시': 2427954,
             '광주광역시': 1455048}
# 딕셔너리를 Series로. 키가 인덱스가 됨
population = pd.Series(pop_dictionary)
print(population)
print(population['서울특별시'])  # 9720846
print(population['서울특별시':'인천광역시'])  # 슬라이싱
