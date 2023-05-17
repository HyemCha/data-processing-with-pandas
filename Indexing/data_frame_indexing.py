import numpy as np
import pandas as pd
from data.data import korea_df

# DataFrame Indexing

# print(korea_df['남자인구수'])
# print(korea_df.남자인구수)
korea_df['남여비율'] = (korea_df['남자인구수'] * 100 / korea_df.여자인구수)  # 유도성에 가까운 것...
# print(korea_df.남여비율)

# print(korea_df.values)  # 값들이 array 형태로 반환됨
# print(korea_df.T)  # 행과 열이 바뀌어 반환
# print(korea_df.values[0])  # 한 줄만 뽑아냄
# print(korea_df['인구수'])
# print(korea_df.loc[:'인천광역시', :'남자인구수'])  # 행은 '인천광역시'까지, 컬럼은 '남자인구수'까지
# print(korea_df.loc[(korea_df.여자인구수 > 1000000)])  # 여자인구수가 1000000이상인 곳만 보여줌
# print(korea_df.loc[korea_df.인구수 < 2000000])  # 인구수가 2000000이상인 곳만 반환
# print(korea_df.loc[korea_df.인구수 > 2500000])  # 인구수가 2500000이상인 곳만 반환
# print(korea_df.loc[korea_df.남여비율 > 100])  # 남여비율이 100이상인 곳만 반환
# print(korea_df.loc[(korea_df.인구수 > 2500000) & (korea_df.남여비율 > 100)])  # 인구수가 2500000 이상이고 남여비율이 100이상인 곳
# print(korea_df.iloc[:3, :2])  # 정수 색인으로 접근