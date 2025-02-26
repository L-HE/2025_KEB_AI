# 나이에 따른 생존율 계산

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split    #훈련, 검증세트 분할 함수
from sklearn.neighbors import KNeighborsRegressor       #적용모델 : K 최근점 이웃 회귀모델

titanic = sns.load_dataset('titanic')

median_age = titanic['age']