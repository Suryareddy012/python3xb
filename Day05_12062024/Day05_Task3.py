
n = 12
fib_series = [0, 1]
for i in range(2, n):
    fib_series.append(fib_series[i-1] + fib_series[i-2])

print(f"Fibonacci series for n = {n}: {fib_series}")