#F(0) = 0
#F(1) = 1
#F(n) = F(n-1) + F(n-2), pentru n ≥ 2

n = int(input("Fibonacci pentru n = "))

if n == 0:
    fb = 0
elif n == 1:
    fb = 1
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    fb = b

print(f"F({n}) = {fb}")



#biblioteca python
# informatie de pe chat gpt
#

from sympy import fibonacci

n = int(input("Fibonacci pentru n = "))

print(f"F({n}) = {fibonacci(n)}")