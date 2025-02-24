# Assignment
# v0.6) v0.5의 최근접이웃모델과 같이 동작하는 커스텀 클래스를 설계하시오.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helearn import KNeighborsRegressor

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")

X = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values
X_new = [[37_655.2]]


ls.plot(kind='scatter', grid= True, x = "GDP per capita (USD)", y = "Life satisfaction")
plt.axis([23500, 62500, 4, 9])
plt.show()


model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y, X_new)

print(model.predict())