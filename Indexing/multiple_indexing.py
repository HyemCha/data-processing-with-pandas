import numpy as np
import pandas as pd
from data.data import korea_df

# Multi Indexing -> 고차원 데이터 처리


### 다중 인덱스 Series
idx_tuples = [('서울특별시', 2010), ('서울특별시', 2020),
              ('부산광역시', 2010), ('부산광역시', 2020),
              ('인천광역시', 2010), ('인천광역시', 2020),
              ('대구광역시', 2010), ('대구광역시', 2020),
              ('대전광역시', 2010), ('대전광역시', 2020),
              ('광주광역시', 2010), ('광주광역시', 2020)]
# print(idx_tuples)
pop_tuples = [10312545, 9720846,
              2567910, 3404423,
              2758296, 2947217,
              2511676, 2427954,
              1503664, 1471040,
              1454636, 1455048]
population = pd.Series(pop_tuples, index=idx_tuples)
# print(population)

midx = pd.MultiIndex.from_tuples(idx_tuples)  # from_tuples 메서드로 다중인덱스 구성
# print(midx)

population = population.reindex(midx)
# print(population)
# print(population[:, 2010])  # 2010년도 데이터만
# print(population['대전광역시', :])  # 대전광역시 데이터만

korea_mdf = population.unstack()  # 다중인덱싱을 가진 series 구조를 dataframe으로 변환
# print(korea_mdf)

korea_mdf.stack()  # dataframe을 다중인덱싱을 가진 series로 변환

male_tuples = [5111259, 4732275,
              1773170, 1668618,
              1390356, 1476813,
              1155245, 1198815,
              7513648, 734441,
              721780, 720060]
# print(male_tuple)

female_tuples = [5201286, 4988571,
                 1794740, 1735805,
                 1367940, 1470404,
                 1256431, 1229139,
                 750016, 736599,
                 732856, 734988]

korea_mdf = pd.DataFrame({'총인구수':population,
                          '남자인구수': male_tuples,
                          '여자인구수': female_tuples})
# print(korea_mdf)

ratio = korea_mdf['남자인구수'] * 100 / korea_mdf['여자인구수']
# print(ratio)
# print(ratio.unstack())

korea_mdf = pd.DataFrame({'총인구수':population,
                          '남자인구수': male_tuples,
                          '여자인구수': female_tuples,
                          '남여비율': ratio})
# print(korea_mdf)


### 다중인덱스 생성
df = pd.DataFrame(np.random.rand(6, 3),
                  index=[['a', 'a', 'b', 'b', 'c', 'c'], [1, 2, 1, 2, 1, 2, ]],
                  columns=['c1', 'c2', 'c3'])
# print(df)

d = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b', 'c', 'c'], [1, 2, 1, 2, 1, 2, ]])
print(d)