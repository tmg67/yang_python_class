def store_contact(name,number,contact={}):
    contact[name.lower()] = number
    return contact
def phone_book():
    contacts = {}
    while True:
        name = input("enter name")
        number = input("enter number")
        contacts = store_contact(name, number, contacts)
        user_choice = input("""
        do you want to exit
        1.yes
        2.no """ )
        if user_choice == "1":
            return contacts
            break

my_contact_book = phone_book()
def get_phone_number( name, contact):
    return contact.get(name.lower())

user_name = input("enter name to find the phone number")
print(get_phone_number(user_name, my_contact_book))