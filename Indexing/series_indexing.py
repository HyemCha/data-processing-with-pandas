import numpy as np
import pandas as pd

# Indexing - Series Indexing
# s = pd.Series([0, 0.25, 0.5, 0.75, 1.0],
#               index=['a', 'b', 'c', 'd', 'e'])
# print(s)
# print('b' in s)
# print(s.keys())
# print(list(s.items()))  # items()는 zip을 반환하므로 리스트로 감싸기
# s['f'] = 1.25
# print(s)  # 딕셔너리처럼 키와 값으로 구성됨
# print(s['a':'d'])
# print(s[0:4])  # 위와 동일한 결과
# print(s[(s > 0.4) & (s < 0.8)])  # 조건에 해당하는 것 뽑아내기
# print(s[['a', 'b', 'c']])

# s = pd.Series(['a', 'b', 'c', 'd', 'e'],
#               index=[1, 3, 5, 7, 9])
# print(s)
# print(s[1])
# print(s[1:3])
# print(s.iloc[1])  # 'b' 1번째 값
# print(s.iloc[1:3])
# print(s.reindex(range(10)))  # 인덱스를 다시 구성. 10이라고 쓰면 0~9까지의 값을 인덱스로 바꿔줌. 없는 값들은 NaN으로
# print(s.reindex(range(10), method='bfill'))  # 없는 값을 그 전 값으로 채우기 bfill:back fill
