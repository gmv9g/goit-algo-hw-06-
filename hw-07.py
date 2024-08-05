import pickle
from datetime import datetime, timedelta

class Birthday:
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None
    
    def add_phone(self, phone):
        self.phones.append(phone)
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def __str__(self):
        return f"Name: {self.name}, Phones: {', '.join(self.phones)}, Birthday: {self.birthday if self.birthday else 'Not set'}"

class AddressBook:
    def __init__(self):
        self.records = {}
    
    def add_record(self, record):
        self.records[record.name] = record
    
    def find(self, name):
        return self.records.get(name, None)
    
    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        upcoming = []
        for record in self.records.values():
            if record.birthday:
                birthday = record.birthday.value
                # Assuming birthday this year
                birthday_this_year = birthday.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                days_until_birthday = (birthday_this_year - today).days
                if 0 <= days_until_birthday <= 30:  # Within a month
                    upcoming.append((record.name, birthday_this_year))
        return upcoming

def handle_add_record(address_book, name, phone=None, birthday=None):
    record = address_book.find(name)
    if not record:
        record = Record(name)
        address_book.add_record(record)
    if phone:
        record.add_phone(phone)
    if birthday:
        record.add_birthday(birthday)

def handle_find_record(address_book, name):
    record = address_book.find(name)
    if record:
        print(record)
    else:
        print("Record not found")

def handle_upcoming_birthdays(address_book):
    birthdays = address_book.get_upcoming_birthdays()
    if birthdays:
        for name, date in birthdays:
            print(f"{name}'s birthday is on {date.strftime('%d.%m.%Y')}")
    else:
        print("No upcoming birthdays within the next 30 days")

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

def main():
    address_book = load_data()
    
    while True:
        command = input("Enter command (add/find/upcoming/exit): ").strip().lower()
        
        if command == "add":
            name = input("Enter name: ").strip()
            phone = input("Enter phone (or leave empty): ").strip()
            birthday = input("Enter birthday (DD.MM.YYYY) (or leave empty): ").strip()
            handle_add_record(address_book, name, phone if phone else None, birthday if birthday else None)
        
        elif command == "find":
            name = input("Enter name: ").strip()
            handle_find_record(address_book, name)
        
        elif command == "upcoming":
            handle_upcoming_birthdays(address_book)
        
        elif command == "exit":
            save_data(address_book)  # Зберегти дані перед виходом
            print("Exiting...")
            break
        
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()