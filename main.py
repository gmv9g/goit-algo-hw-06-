# 1 завдання
from datetime import datetime, date
def get_days_from_today(date_str):
    try:
        
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        
        today = date.today()
        
        
        difference = today - input_date
        
        
        return difference.days
    
    except ValueError:
        print("Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'.")
        return None


today = date.today() 

print(get_days_from_today("2021-10-09"))  
print(get_days_from_today("2020-01-01")) 
print(get_days_from_today("2021/05/05"))  


# 2 завдання

import random

def get_numbers_ticket(minimum, maximum, quantity):
    if minimum < 1 or maximum > 1000 or quantity < 0 or quantity > (maximum - minimum + 1):
        print("Неправильні вхідні дані. Перевірте умови задачі.")
        return []
    

    random_numbers = set()
    
    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(minimum, maximum))
    

    sorted_numbers = sorted(random_numbers)
    
    return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)