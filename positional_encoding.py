#!/usr/bin/env python3

# reference : https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/

import numpy as np

np.random.seed(3407)  # 'random_state is all you need' :)

text = "pasar pergi ke budi"

vocab = sorted(set(text.split()))  # word vocabulary
word_to_idx = {word: idx for idx, word in enumerate(vocab)}

encode = lambda x: [word_to_idx[word] for word in x]

tokens = encode(text.split())

embed_size = 3

embed = np.random.rand(len(vocab) + 1, embed_size)

vectors = np.array([embed[idx] for idx in tokens])

# Ada dua jenis fungsi yang umum digunakan dalam positional encoding :

# 1. Sine and Cosine Functions
def getPositionEncoding(seq_len, d, n=10000):
    P = np.zeros((seq_len, d))
    for k in range(seq_len):
        for i in np.arange(int(d / 2)):
            denominator = np.power(n, 2 * i / d)
            P[k, 2 * i] = np.sin(k / denominator)
            P[k, 2 * i + 1] = np.cos(k / denominator)
    return P

# 2. Learnable Positional Encoding :
# positional encoding juga bisa dipelajari langsung oleh model selama proses pelatihan.
# Dalam metode ini, vektor posisi diperlakukan sebagai parameter yang dioptimalkan selama pelatihan model, mirip dengan cara embedding kata dioptimalkan.

def getPositionEncoding2(seq_len,d):
  pos_encoding = np.random.rand(seq_len, d)
  positions = np.arange(0,seq_len)
  return [pos_encoding[idx] for idx in positions]

print(f"sequences :\n{tokens}\n")
print(f"word embed : \n{vectors}\n")
sine_cosine = vectors + getPositionEncoding(vectors.shape[0],vectors.shape[1])
print(f"word embed + positional (sine and cosine) : \n{sine_cosine}\n")
learnable = vectors + getPositionEncoding2(vectors.shape[0],vectors.shape[1])
print(f"word embed + positional (learnable): \n{learnable}\n")
