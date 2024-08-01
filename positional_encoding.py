#!/usr/bin/env python3

# reference : https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/

import numpy as np

np.random.seed(3407)  # 'random_state is all you need' :)

text = "pasar pergi ke budi"

vocab = sorted(set(text.split()))  # word vocabulary
word_to_idx = {word: idx for idx, word in enumerate(vocab)}

encode = lambda x: [word_to_idx[word] for word in x]

tokens = encode(text.split())

embed_size = 6

embed = np.random.rand(len(vocab) + 1, embed_size)

vectors = np.array([embed[idx] for idx in tokens])


def getPositionEncoding(seq_len, d, n=10000):
    P = np.zeros((seq_len, d))
    for k in range(seq_len):
        for i in np.arange(int(d / 2)):
            denominator = np.power(n, 2 * i / d)
            P[k, 2 * i] = np.sin(k / denominator)
            P[k, 2 * i + 1] = np.cos(k / denominator)
    return P


vectors = vectors + getPositionEncoding(
    seq_len=vectors.shape[0], d=vectors.shape[1]
)  # vectors with positional encoding
print(vectors)
