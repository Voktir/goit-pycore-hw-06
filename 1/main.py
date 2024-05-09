from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def validation():
        pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        print(self.name)
        self.phones = []

    def add_phone(self, p_number: str):
        self.phones.append(Phone(p_number))
        print(self.phones)
    
    def remove_phone():
        pass
    
    def edit_phone():
        pass   
    
    def find_phone():
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        print(self.data)
        print(str(record))
        print(record.name.value)
        self.data[Name] = record
        print(self.data)
        print("..............")

    def find():
        pass

    def delete():
        pass    


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

print(john_record)

# Додавання запису John до адресної книги
book.add_record(john_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(name)
    print(record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(name)
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")