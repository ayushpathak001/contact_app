contacts = {}

while True :
    print("\nContact Book App !")
    print("1. Create Contact ")
    print("2. View Contact ")
    print("3. Update Contact ")
    print("4. Delete Contact ")
    print("5. Search Contact ")
    print("6. Count Contact ")
    print("7. Exit")

    choice = input("Enter Your Choice = ")

    if choice == "1":
        name = input("Enter Your name =")
        if name in contacts :
            print(f"Contact name {name} already exists !")
        else:
            age = input("Enter age =")
            email = input("Enter  Email =")
            mobile = input("Enter  mobile Number =")
            contacts[name] = {"age":int(age) , "email":(email) , "mobile":(mobile)}
            print(f"Contact name {name} as been created successfully !")
    elif choice =='2':
        name = input("Enter Your Name =")
        if name in contacts:
            contacts = contacts[name]
            print(f"Name: {name}, Age:{age}, email {email} , Mobile Number:{mobile} ")
        else:
            print("Contact not Found !")

    elif choice =='3':
        name = input("Enter Your Name =")
        if name in contacts:
            age = input("Enter updated age =")
            email = input("Enter updated email =")
            mobile = input("Enter updated mobile number =")
            contacts[name] = {"age":int(age) , "email":(email) , "mobile":(mobile)}
        else:
            print("Contact not found !")
    
    elif choice == '4':
        name = input("Enter Your name =")
        if name in contacts :
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully !")
        else:
            print("Contact not found !")

    elif choice == '5':
        search_name = input("Enter contact name to search  =")
        found = False
        for name , contact in contacts.items():
            if search_name.lower() in name.lower() :
                print(f"Found -- Name: {name} , age: {age} , email: {email} , mobile Number: {mobile}")
                found = True
        if not found :
            print("No contact with that name !")
        
    elif choice == '6':
        print(f"Total contact in your book : {len(contacts)}")
    
    elif choice == '7':
        print("Okay Good Bye...Closing the Program !")
        break
    
    else :
        print("""Something went wrong!
                 Invalid Choice ! 
                 plz Again Try Enter Valid Choice !""")


