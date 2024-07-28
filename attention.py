#!/usr/bin/env python3

# reference : (Anak AI) https://www.youtube.com/watch?v=FQ-rfK-rVtY
import numpy as np

text = "indonesia adalah surga"
np.random.seed(42)
token = text.split()
vocab_size = len(token)
vocab = sorted(set(token))

word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for idx, word in enumerate(vocab)}

encode = lambda x: [word_to_idx[word] for word in x]  # x = token
decode = lambda x: "".join(idx_to_word[word] for word in x)  # x = sequence

data_indices = encode(token)

vector_size = 5
embed = np.random.randn(vocab_size, vector_size)
vectors = np.array([embed[idx].tolist() for idx in data_indices])

n = 5
# Bobot query,key dan value
query = np.random.randn(vector_size, n)
key = np.random.randn(vector_size, n)
value = np.random.randn(vector_size, n)

# (n_vectors,n)
vq = vectors @ query
vk = vectors @ key
vv = vectors @ value


def scaled_dot_product(q, k, v):
    attn_logits = q @ k.T
    attn_logits = attn_logits / np.sqrt(n)
    attention = np.exp(attn_logits) / np.sum(
        np.exp(attn_logits), axis=-1, keepdims=True
    )  # softmax
    values = attention @ v
    return values, attention


output, attention = scaled_dot_product(vq, vk, vv)
print(f"output : \n{output}")
print(f"attention : \n{attention}")

"""
embedding, dan bobot (query,key,value) yang akan dicari oleh ketika training
"""
