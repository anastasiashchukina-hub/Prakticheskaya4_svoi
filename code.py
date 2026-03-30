list = [0] * 100
def fib(n):
    if list[n] != 0:
        return list[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        list[n] = fib(n-1) + fib(n-2)
        return list[n]

for i in range(100):
    print(f"F({i}) = {fib(i)}")