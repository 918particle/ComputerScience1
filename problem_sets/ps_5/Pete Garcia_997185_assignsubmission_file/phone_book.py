phone_book = {
"562-555-0142": ["Maria","Garcia"],
"562-555-0188": ["Daniel","Kim"],
"562-555-0125": ["Elena","Garcia"],
"562-555-0171": ["Maria","Lopez"],
"562-555-0194": ["Aisha","Patel"],
"562-555-0160": ["Marcus","Johnson"]
}

print (phone_book)

print(type(phone_book))
print(len(phone_book))

print(phone_book["562-555-0188"])

print(phone_book.get("562-555-0194"))

phone_book["562-555-0110"] = ["Sofia", "Reyes"]

phone_book["562-555-0160"] = ["Marcus", "Johnston"]

del phone_book["562-555-0188"]

print(phone_book.keys())
print(phone_book.values())

def find_first(phone_book, first):
    matches = []

    for phone, person in phone_book.items():
        if person[0].lower() == first.lower():
            matches.append(phone)

    return matches


def find_last(phone_book, last):
    matches = []

    for phone, person in phone_book.items():
        if person[1].lower() == last.lower():
            matches.append(phone)

    return matches


def find_name(phone_book, first, last):
    matches = []

    for phone, person in phone_book.items():
        if person[0].lower() == first.lower() and person[1].lower() == last.lower():
            matches.append(phone)

    return matches


print(find_first(phone_book, "Maria"))
print(find_last(phone_book, "Garcia"))
print(find_name(phone_book, "Maria", "Garcia"))

print("")
print("Phone Book Search")
print("1 - Search by first name")
print("2 - Search by last name")
print("3 - Search by full name")
print("4 - Search by phone number")

choice = input("Enter choice: ")

if choice == "1":
    first = input("First name: ")

    matches = find_first(phone_book, first)

    if len(matches) == 0:
        print("No matching contacts found")
    else:
        for phone in matches:
            print(phone)

elif choice == "2":
    last = input("Last name: ")

    matches = find_last(phone_book, last)

    if len(matches) == 0:
        print("No matching contacts found")
    else:
        for phone in matches:
            print(phone)

elif choice == "3":
    first = input("First name: ")
    last = input("Last name: ")

    matches = find_name(phone_book, first, last)

    if len(matches) == 0:
        print("No matching contacts found")
    else:
        for phone in matches:
            print(phone)

elif choice == "4":
    phone = input("Phone number: ")

    person = phone_book.get(phone)

    if person == None:
        print("Phone number not in the phone book")
    else:
        print(person)

else:
    print("Invalid choice")