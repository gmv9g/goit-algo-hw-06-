# 1 завдання
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        
        cache[n] = result
        return result
    
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))

# 2 завдання
import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    
    total_sum = sum(numbers_generator)
    
    return total_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 37.45 і 424.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")