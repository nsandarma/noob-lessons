#!/usr/bin/env python3
import numpy as np
from attention import scaled_dot_product


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)


def multihead_attention(m_w_query, m_w_key, m_w_value):
    num_head = m_w_query.shape[0]
    m_query = vectors @ m_w_query
    m_key = vectors @ m_w_key
    m_value = vectors @ m_w_value

    heads = []
    attns = []

    for i in range(num_head):
        query = m_query[i]
        key = m_key[i]
        value = m_value[i]

        out, attn = scaled_dot_product(query, key, value, mask)
        heads.append(out)
        attns.append(attn)

    heads, attns = np.array(heads), np.array(attns)

    concat_heads = np.concatenate(heads, axis=-1)
    concat_attns = np.concatenate(attns, axis=-1)

    w_output = np.random.rand(num_head * d_v, d)

    outputs = concat_heads @ w_output
    return outputs, attns


if __name__ == "__main__":
    np.random.seed(42)
    vectors = np.random.randn(4, 5)
    seq_length, d = vectors.shape
    d_q = 4
    d_k = 4
    d_v = 5

    num_head = 3
    m_w_query = np.random.rand(num_head, d, d_q)
    m_w_key = np.random.rand(num_head, d, d_k)
    m_w_value = np.random.rand(num_head, d, d_v)
    mask = np.triu(np.ones((seq_length, seq_length)) * -np.inf, 1)

    outputs, attns = multihead_attention(m_w_query, m_w_key, m_w_value)
    print(outputs)
    print()
    print(attns)
