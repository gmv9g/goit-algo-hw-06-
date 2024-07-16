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


# 4 завдання 

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Введіть ім'я та номер телефону, будь ласка."
        except KeyError:
            return "Неправильна команда або ім'я контакту."
        except IndexError:
            return "Неправильна кількість аргументів."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def find_phone(name):
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Контакт '{name}' не знайдено."

@input_error
def list_all_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Контакти не знайдено."

def main():
    while True:
        command = input("Введіть команду: ").strip().lower()

        if command.startswith("add"):
            try:
                _, arg = command.split(maxsplit=1)
                result = add_contact(arg.split())
                print(result)
            except Exception as e:
                print(f"Сталася помилка: {e}")
        
        elif command.startswith("phone"):
            try:
                _, arg = command.split(maxsplit=1)
                result = find_phone(arg.strip())
                print(result)
            except Exception as e:
                print(f"Сталася помилка: {e}")

        elif command.startswith("all"):
            try:
                result = list_all_contacts()
                print(result)
            except Exception as e:
                print(f"Сталася помилка: {e}")
        
        else:
            print("Неправильна команда.")

if __name__ == "__main__":
    main()