def sum_of_squares(N):
    result = 0
    for i in range(1, N+1):
        result += i*i
    return result

def sum_of_squares_optimized(N):
    return N*(N+1)*(2*N+1)//6

N = 5
print("Unoptimized version - Sum of squares from 1 to", N, ":", sum_of_squares(N))
print("Optimized version   - Sum of squares from 1 to", N, ":", sum_of_squares_optimized(N))
