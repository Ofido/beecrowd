
import asyncio

MEMO = {}
def decorator(func):
    def do_func(*args, **kwargs):
        if MEMO.get(args[0]):
            return MEMO[args[0]]
        MEMO[args[0]] = func(*args, **kwargs)
        return MEMO[args[0]]
    return do_func

@decorator
def fib(x) -> int:
    if x <= 2:
        return 1
    return fib(x-1) + fib(x-2)

print(fib(199))
