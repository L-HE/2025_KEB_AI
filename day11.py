import  numpy as np

a = np.array([1, 3, -9, 2])
# print(a, a.ndim)
b = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
# print(b, b.ndim, b.shape)
c = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]])
print(c, c.ndim, c.shape, c.dtype, c.strides)
# ndim: 배열의 차원 수를 나타내는 속성
# shape: 배열의 차원과 크기를 나타내는 tuple 형태의 속성
# dtype: 배열 요소들의 데이터 타입을 나타내는 속성(요소들은 해당 데이터 타입으로 일괄적 처리)