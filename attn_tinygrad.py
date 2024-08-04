#!/usr/bin/env python3
import numpy as np
from tinygrad import Tensor, dtypes
from attention import scaled_dot_product
import random

np.random.seed(42)
vectors = np.random.rand(4, 5)
d_model = 6

w_query = np.random.rand(vectors.shape[1], d_model)
w_key = np.random.rand(vectors.shape[1], d_model)
w_value = np.random.rand(vectors.shape[1], d_model)

q = vectors @ w_query
k = vectors @ w_key
v = vectors @ w_value


values, attn = scaled_dot_product(q, k, v)

vectors = Tensor(vectors)

w_query, w_key, w_value = Tensor(q), Tensor(k), Tensor(v)

# print(Tensor.scaled_dot_product_attention(w_query,w_key,w_value).numpy())


def make_dataset():
    ds = []
    for i in range(100):
        for j in range(100):
            s = i + j
            ds.append(
                [i // 10, i % 10, j // 10, j % 10, s // 100, (s // 10) % 10, s % 10]
            )
    random.shuffle(ds)
    ds = np.array(ds).astype(np.float32)
    ds_X = ds[:, 0:6]
    ds_Y = np.copy(ds[:, 1:])
    ds_X_train, ds_X_test = ds_X[0:8000], ds_X[8000:]
    ds_Y_train, ds_Y_test = ds_Y[0:8000], ds_Y[8000:]
    return ds_X_train, ds_Y_train, ds_X_test, ds_Y_test


X_train, y_train, X_test, y_test = make_dataset()

print(X_train.shape)
print()
print(y_train.shape)
