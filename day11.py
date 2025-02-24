import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
from helearn import LinearRegression

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
#print(type(ls))

X = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values
# print(X)

ls.plot(kind='scatter', grid= True, x = "GDP per capita (USD)", y = "Life satisfaction")
plt.axis([23500, 62500, 4, 9])
plt.show()


model = LinearRegression()

model.fit(X, y)

X_new = [[37_655.2]]
print(model.predict(X_new))