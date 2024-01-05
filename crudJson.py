import json

mydict = {}

phone = input("Enter the number: ")

while True:
    print("1. Create\n2. Update\n3. Read\n4. Delete\n5. Exit")
    choose = int(input("Enter the option--->>:"))

    if choose == 1:
        print("Welcome to create")
        name = input("Enter the name->:")
        email = input("Enter the email address---->>:")
        while not email or "@" not in email or "." not in email:
            print("Please enter a valid email address")
            email = input("Enter the email address---->>:")
        number = input("Enter the number---->>:")
        while len(number) != 10 or not number.isdigit():
            print("Please enter a valid 10-digit number")
            number = input("Enter the number---->>:")
        age = int(input("Enter the age----->>:"))
        while age <= 0:
            print("Please enter a valid age")
            age = int(input("Enter the age----->>:"))

        contact = {"name": name, "email": email, "number": number, "age": age}
        mydict[phone] = contact
        # Save the dictionary to a JSON file
        with open("contacts.json", "w") as json_file:
            json.dump(mydict, json_file)

    elif choose == 2:
        if phone in mydict:
            print("1. Update name\n2. Update number\n3. Update email\n4. Update age")
            select = int(input("Enter the option you want to select-->>>:"))
            if select == 1:
                name1 = input("Enter the new name->:")
                mydict[phone]["name"] = name1
            elif select == 2:
                number = input("Enter the new number---->>:")
                while len(number) != 10 or not number.isdigit():
                    print("Please enter a valid 10-digit number")
                    number = input("Enter the new number---->>:")
                mydict[phone]["number"] = number
            elif select == 3:
                email = input("Enter the new email address---->>:")
                while not email or "@" not in email or "." not in email:
                    print("Please enter a valid email address")
                    email = input("Enter the new email address---->>:")
                mydict[phone]["email"] = email
            elif select == 4:
                age = int(input("Enter the new age----->>:"))
                while age <= 0:
                    print("Please enter a valid age")
                    age = int(input("Enter the new age----->>:"))
                mydict[phone]["age"] = age
            print("\n")
        else:
            print(f"The number '{phone}' does not exist in the dictionary.")
            print("\n")

    elif choose == 3:
        if phone in mydict:
            contact = mydict[phone]
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Number: {contact['number']}")
            print(f"Age: {contact['age']}")
        else:
            print(f"The number '{phone}' does not exist in the dictionary.")
        print("\n")

    elif choose == 4:
        if phone in mydict:
            mydict.pop(phone)
            print("Contact deleted.")
        else:
            print(f"The number '{phone}' does not exist in the dictionary.")
        print("\n")

    elif choose == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose a valid option (1-5).")

    print("\n")