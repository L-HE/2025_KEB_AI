# Assignment
# v0.7 결측치 있는 dataframe

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame(
    {
        'A':[1, 2, np.nan, 4],
        'B':[np.nan, 2, 3, 4],
        'C':[1, 2, 3, 4]
    }
)

print(df)