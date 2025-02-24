import numpy as np

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