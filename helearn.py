import numpy as np
import pandas as pd


class LinearRegression:
    def __init__(self):
        self.slope = None       #weight
        self.intercept = None   #bias


    def fit(self, X, y):
        """
        learning function
        :param X: independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :return:void
        """

        X_mean = np.mean(X)
        y_mean = np.mean(y)

        # MSE: mean squared error -> 제곱해서 부호를 지우므로써 오차값을 표시. 오차값을 줄이기 위함.
        #                            (관측치 - 타겟값)^2
        denominator = np.sum(pow(X-X_mean, 2))
        numerator = np.sum((X-X_mean) * (y-y_mean))

        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * X_mean)


    def predict(self, X) -> np.ndarray:
        """
        predict value for input
        :param X: new independent variable
        :return: predict value for input (2d array format)
        """
        return self.slope * np.array(X) + self.intercept


class KNeighborsRegressor:
    def __init__(self, n_neighbors = 5):
        self.sum = 0
        self.avg = 0
        self.nb = n_neighbors
        self.ylist = None


    def fit(self, X, y, X_new):
        """
        learning function
        :param X: independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :param X_new: new independent variable
        :return: void
        """
        ylist = [[]]
        X = np.append(X, X_new, axis=0)
        X_num = None
        switch_flag = True
        while switch_flag:
            i = len(X) - 1
            value = X[i][0]
            while i > 0 and X[i - 1][0] > value:
                X[i][0] = X[i - 1][0]
                i -= 1
                switch_flag = False
            X[i][0] = value
            X_num = i


        y = np.insert(y, X_num, None, axis= 0)
        num = 1
        for j in range(1, self.nb + 1, 2):
            while num <= int((j + 1) / 2):
                if (X[X_num][0] - X[X_num - num][0]) < (X[X_num + num][0] - X[X_num][0]):
                    ylist = np.append(ylist, y[X_num - num][0])
                    ylist = np.append(ylist, y[X_num + num][0])
                else:
                    ylist = np.append(ylist, y[X_num + num][0])
                    ylist = np.append(ylist, y[X_num - num][0])
                num += 1
        self.ylist = ylist


    def predict(self) -> float:
        """
        predict value for input
        :return: predict value for input
        """
        for i in range(self.nb):
            self.sum = self.sum + self.ylist[i]
        self.avg = self.sum / self.nb

        return self.avg
