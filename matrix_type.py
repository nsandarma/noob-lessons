#!/usr/bin/env python3
from typing import Union, List, Tuple, Optional
import numpy as np
import unittest


class Matrix:

    def __init__(self, m: List[Union[List, Tuple]]):
        assert all(
            isinstance(x, (list, tuple, Matrix)) for x in m
        ), f"{m} is not matrix"

        row = len(m)
        cols = len(m[0])

        assert all(cols == len(x) for x in m), "{m} is not matrix"

        self.rows = row
        self.cols = cols
        self.m = m

    def __str__(self):
        s = f"{self.m}"
        s = s.replace("],", "]\n").replace(",", " ")
        return s

    def __matmul__(self, other):
        return self.matmul(other)

    def matmul(self, other):
        other = Matrix(other) if not isinstance(other, Matrix) else other

        assert self.cols == other.rows, f"{self.cols} != {other.rows}"

        v = [[other.m[c][r] for c in range(other.rows)] for r in range(other.cols)]
        result = [
            [sum([col[i] * row[i] for i in range(other.rows)]) for col in v]
            for row in self.m
        ]  # nice code ! :D
        return Matrix(result)

    def numpy(self):
        return np.array(self.m)

    @property
    def shape(self):
        return self.rows, self.cols


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.m1 = Matrix(
            [
                [1, 2, 4],
                [4, 3, 6],
            ]
        )

        self.m2 = Matrix([[1, 2, 3], [4, 5, 6], [4, 5, 6]])

        self.me = [[1, 2], [1]]

    def test_mul(self):
        m1 = self.m1 @ self.m2
        m2 = self.m1.numpy() @ self.m2.numpy()
        self.assertListEqual(m1.m, m2.tolist())


if __name__ == "__main__":
    unittest.main()
