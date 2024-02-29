
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name]= phone
        return "Contact updated."
    else:
        return "Error: no contact."

def show_phone(name, contacts):
    if name in contacts:
        return contacts.get(name)
    else:
        return "Error: no contact."

def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items() if phone is not None])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")         
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:                # input_text: "close" або "exit"
            print("Good bye!")                          # output_text: "Good bye!"
            break
        elif command == "hello":                        # input_text: "hello"
            print("How can I help you?")                # output_text: "How can I help you?"
        elif command == "add":                          # "add [ім'я] [номер телефону]" "add John 1234567890"
            print(add_contact(args, contacts))          # output_text: "Contact added."
        elif command == "change":                       # "change [ім'я] [новий номер телефону]"  "change John 0987654321"
            print(change_contact(args, contacts))       # output_text: "Contact updated."
        elif command == "phone":                        # "phone John"
            name = args[0]
            print(show_phone(name, contacts))           # output:  [номер телефону]
        elif command == "all":                          # "all"
            print(show_all(contacts))                   # output: усі збережені контакти
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
