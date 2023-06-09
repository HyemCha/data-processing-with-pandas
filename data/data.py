import pandas as pd

pop_dictionary = {'서울특별시': 9720846,
             '부산광역시': 3404423,
             '인천광역시': 2947217,
             '대구광역시': 2427954,
             '대전광역시': 1471040,
             '광주광역시': 1455048}
population = pd.Series(pop_dictionary)

male_dictionary = {'서울특별시': 4732275,
                   '부산광역시': 1668618,
                   '인천광역시': 1476813,
                   '대구광역시': 1198815,
                   '대전광역시': 734441,
                   '광주광역시': 720060}
male = pd.Series(male_dictionary)
# print(male)

female_dictionary = {'서울특별시': 4988571,
                     '부산광역시': 1735805,
                     '인천광역시': 1470404,
                     '대구광역시': 1229139,
                     '대전광역시': 736599,
                     '광주광역시': 734988}
female = pd.Series(female_dictionary)
# print(female)

korea_df = pd.DataFrame({'인구수':population,
                         '남자인구수':male,
                         '여자인구수':female})