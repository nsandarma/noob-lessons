#!/usr/bin/env python3

# reference : (Anak AI) https://www.youtube.com/watch?v=FQ-rfK-rVtY
import numpy as np

text = "indonesia adalah surga"

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

# (3,5) * (5,2)

vq = vectors @ query
vk = vectors @ key
vv = vectors @ value

result = []

for q in vq:
    v = []
    for i, k in enumerate(vk):
        r = q.dot(k) / np.sqrt(n)
        v.append(r)

    attention_weights = np.exp(v) / np.sum(np.exp(v), axis=0)
    attention_outputs = np.matmul(attention_weights, vv)
    result.append(attention_outputs)

result = np.array(result)

print(f"vectors (embed): \n{vectors}")
print(f"vectors + context(attention): \n{result}")
