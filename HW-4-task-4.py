
def parse_input(user_input):    
    """Приймаємо від користувача дані і сортуємо на команди і аргументи,
    приводимо команди в нижній регістр, щоб уникнути помилок команд написаних з великої букви 
    і повертаєм команди в нижнтому регістрі, та аргументи які надав користувач"""

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """При команді add, і наступних аргумантах name phone,
    перевіряємо чи ім'я є в словнику, якщо немає, додаємо його в словник,
    якщо є виводим повідомлення, що таке ім'я вже записане"""

    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "This name is already saved"
    

def change_contact(args, contacts):
    """При команді change, шукаємо імя в словнику, якщо воно є,
    змінєюмо телефон, якщо немає виводим текст контакт не знайдений
    додати новий контакт, і пропонуєм натиснути Y (так) або N (ні).
    Якщо відповідь так, то передаємо аргументи в функцію def add_contact, 
    якщо ні сповіщаєм, що контакт не доданий
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        print(f"Contact not found, you want save this new contact? Y|N  ")
        new_contact = input().upper()
        if new_contact == "Y":
            return add_contact(args, contacts)
        else :
            return "No contact added."

def show_phone(args, contacts):
    """Шукаєм контакт в списку, і виводимо дані,
    якщо немає виводим повідомлення"""
    name = args[0]
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f'Number {name} is not saved')

def show_all(contacts):
    """Виводимо весь список контактів"""
    for name, number in contacts.items():
        print(f'Name: {name}, Phone: {number}')


def main():
    """Функція приймає команди і аргументи і передає їх на виконання іншим функціями"""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            if len(contacts) == 0:
                print("Phone book is empty")
            else:
                show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
