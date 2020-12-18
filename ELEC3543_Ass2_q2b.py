import math
import time
import numpy as np
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states, xoroshiro128p_uniform_float32

threads_per_block = 64
blocks = 24
rng_states = create_xoroshiro128p_states(threads_per_block * blocks, seed=1)

list_of_iterations = [10000, 25000, 50000, 75000, 100000]

def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier - 0.5) / multiplier

@cuda.jit
def compute_pi(rng_states, iterations, out):
    """Find the maximum value in values and store in result[0]"""
    thread_id = cuda.grid(1)

    # Compute pi by drawing random (x, y) points and finding what
    # fraction lie inside a unit circle

    inside = 0
    for i in range(iterations):
        x = xoroshiro128p_uniform_float32(rng_states, thread_id)
        y = xoroshiro128p_uniform_float32(rng_states, thread_id)
        if x**2 + y**2 <= 1.0:
            inside += 1
    out[thread_id] = 4.0 * inside / iterations

print("Estimating Pi with the JIT function:")

for i in list_of_iterations:
    out = np.zeros(threads_per_block * blocks, dtype=np.float32)
    start_time = time.clock()
    compute_pi[blocks, threads_per_block](rng_states, i, out)
    value = out.mean()
    value = round_half_down(value, 7)
    end_time = time.clock()
    print('pi: {:<10}   iters =  {:>6}          exec. time = {:^10}'.format(value,i,str(end_time - start_time)))