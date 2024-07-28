#!/usr/bin/env python
import torch
import time

N = 1000

a = torch.rand(N, N).cuda()
b = torch.rand(N, N).cuda()

start = time.monotonic()

c = torch.matmul(a, b)

end = time.monotonic()

times = end - start

num_ops = 2 * N**3

gflops = num_ops / times / 1e9

print(f"GFLOPS : {gflops:.2f}")
