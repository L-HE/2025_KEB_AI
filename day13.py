# Assignment
# 데이터 로딩 -> 데이터 전처리 -> 타겟 및 독립변수 설정 -> 트레이닝 / 테스트 셋 설정
# -> 모델 선택 및 학습 -> 예측 수행 -> 성능 평가(mse등) -> 시각화

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

mpg = sns.load_dataset('mpg')

train_set = train_test_split(mpg, test_size=0.2, random_state=42)

# mpg.hist(bins=50, figsize=(12, 8))
# plt.show()

