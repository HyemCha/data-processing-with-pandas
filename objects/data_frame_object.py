import numpy as np
import pandas as pd

# DataFrame: 여러 컬럼이 들어간 2차원 특성을 가짐

# df = pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A':4, 'B':5, 'C':7}])
# print(df)  # 미씽된 부분은 NaN으로 대체됨 -> 누락값에 대한 대처

# # 랜덤값으로 구성
# df = pd.DataFrame(np.random.rand(5, 5),
#                   columns=['A', 'B', 'C', 'D', 'E'],
#                   index=[1, 2, 3, 4, 5])
# print(df)

# 딕셔너리는 DataFrame 객체로 변환 안 됨

pop_dictionary = {'서울특별시': 9720846,
             '부산광역시': 3404423,
             '인천광역시': 2947217,
             '대전광역시': 1471040,
             '대구광역시': 2427954,
             '광주광역시': 1455048}
population = pd.Series(pop_dictionary)

male_dictionary = {'서울특별시': 4732275,
                   '부산광역시': 1668618,
                   '인천광역시': 1476813,
                   '대전광역시': 734441,
                   '대구광역시': 1198815,
                   '광주광역시': 720060}
male = pd.Series(male_dictionary)
# print(male)

female_dictionary = {'서울특별시': 4988571,
                     '부산광역시': 1735805,
                     '인천광역시': 1470404,
                     '대전광역시': 736599,
                     '대구광역시': 1229139,
                     '광주광역시': 734988}
female = pd.Series(female_dictionary)
# print(female)

korea_df = pd.DataFrame({'인구수':population,
                         '남자인구수':male,
                         '여자인구수':female})
print(korea_df)
print(korea_df.index)  # 지역
print(korea_df.columns)  # 컬럼
print(korea_df['여자인구수'])  # 여자인구수만 보여줌
print(korea_df['서울특별시':'인천광역시'])