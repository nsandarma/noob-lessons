#!/usr/bin/env python3

# reference : (Anak AI) https://www.youtube.com/watch?v=FQ-rfK-rVtY
import numpy as np


def scaled_dot_product(q, k, v, mask=None):
    attn_logits = q @ k.T
    attn_logits = attn_logits / np.sqrt(k.shape[1])
    if mask is not None:
        attn_logits = attn_logits + mask

    attention = np.exp(attn_logits) / np.sum(
        np.exp(attn_logits), axis=-1, keepdims=True
    )  # softmax

    values = attention @ v
    return values, attention


if __name__ == "__main__":
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

    # Bobot query,key dan value
    n = 5
    query = np.random.randn(vector_size, n)
    key = np.random.randn(vector_size, n)
    value = np.random.randn(vector_size, n)

    # masked attention -> decoder
    mask = np.triu(
        np.ones((vocab_size, vocab_size)) * -np.inf, 1
    )  # (seq_length,seq_length)

    # (n_vectors,n)
    vq = vectors @ query
    vk = vectors @ key
    vv = vectors @ value

    output, attention = scaled_dot_product(vq, vk, vv, mask)
    print(f"output : \n{output}")
    print(f"attention : \n{attention}")

    """
  embedding, dan bobot (query,key,value) akan di update selama proses training
  """
