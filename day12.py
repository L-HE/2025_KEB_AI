# Assignment
# v0.9) v0.8의 사이킷런 라이브러리를 주석처리하고 결측치를 산술평균으로 채워 넣으시오.

import numpy as np
import pandas as pd
# from sklearn.impute import SimpleImputer

df = pd.DataFrame(
    {
        'A':[1, 2, np.nan, 4],
        'B':[np.nan, 2, 3, 4],
        'C':[1, 2, 3, 4]
    }
)

print(df)


mean = df.mean()
df.fillna(value=mean, inplace=True)
print(df)
