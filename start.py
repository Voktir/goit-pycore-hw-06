# from functools import wraps

# def input_error(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         try:
#             if func.__name__ != "show_phone":
#                 name, phone = args
#                 if len(name[1]) < 10:
#                     raise ValueError
#                 else:                
#                     return func(*args, **kwargs)
#             if func.__name__ == "show_phone":
#                 return func(*args, **kwargs)
#         except ValueError:
#             if func.__name__ != "show_phone":
#                 return "Phone is to short. Give me name and full phone number please."
#             else:
#                 return "Give me name. Enter the argument [name]"
#         except KeyError:
#             return "No such name!"
#         except IndexError:
#             return "Insufficient data. Give me name and full phone number please."

#     return inner


# def parse_input(user_input):
#     cmd, *args = user_input.split()
#     cmd = cmd.strip().lower()
#     return cmd, *args

# @input_error
# def add_contact(args, contacts):
#     # try:        
#         name, phone = args
#         name = name.strip().upper()
#         contacts[name] = phone
#         return "Contact added."
#     # except:
#     #     return "Wrong data! : add [name] [phone nbr]"

# @input_error
# def change_username_phone(args, contacts):
#     # try:        
#         name, phone = args
#         name = name.strip().upper()
#         if name in contacts:
#             contacts[name] = phone
#             return "Contact changed"
#         else:
#             return "Wrong contact"
#     # except:
#     #     return "Wrong data! : change [name] [phone nbr]"
    
# @input_error
# def show_phone(args, contacts):
#     # try:        
#     name, = args
#     name = name.strip().upper()
#     return contacts[name]
#         # if name in contacts:
#             # return [int(contacts.get(name))]
#         # else:
#         #     return "Wrong contact"
#     # except:
#     #     return "Wrong data! : phone [name]"

# def main():
#     contacts = {}
#     print("Welcome to the assistant bot!")
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)

#         if command in ["close", "exit"]:
#             print("Good bye!")
#             break

#         elif command == "hello":
#             print("How can I help you?")
#         elif command == "add":
#             print(add_contact(args, contacts))
#         elif command == "change":
#             print(change_username_phone(args, contacts))
#         elif command == "phone":
#             print(show_phone(args, contacts))
#         elif command == "all":
#             print(contacts)
#         else:
#             print("Invalid command.")

# if __name__ == "__main__":
#     main()

class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

class Cat():
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"

owner1 = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner1)
print(cat.owner.name)
print(cat.get_info())