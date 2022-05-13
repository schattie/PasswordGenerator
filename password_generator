from src.password_generator import PasswordGenerator

def main():
    password_generator = PasswordGenerator()
    choice = "0"
    password_size = "0"

    print("This program generates random passwords.\nPasswords can include numbers, special characters, and letters\nPasswords must include letters.")

    while choice != "6":
        print("-------------------Menu-------------------")
        print("1. Toggle special characters")
        print("2. Toggle numbers")
        print("3. Set password size")
        print("4. Generate Password")
        print("5. Show previously generated password")
        print("6. Exit program")

        choice = input("Enter selection:")

        if(choice == "1"):
            print("1. On")
            print("2. Off")
            choice = input("Enter selection:")

            if(choice == "1"):
                password_generator.set_special_characters(True)
            elif(choice == "2"):
                password_generator.set_special_characters(False)
        elif(choice == "2"):
            print("1. On")
            print("2. Off")
            choice = input("Enter selection:")

            if(choice == "1"):
                password_generator.set_numbers(True)
            elif(choice == "2"):
                password_generator.set_numbers(False)
        elif(choice == "3"):
            password_size = int(input("Enter password size:"))
            password_generator.set_password_size(password_size)
        elif(choice == "4"):
            password_generator.generate_password()
        elif(choice == "5"):
            print(password_generator.get_password())
        elif(choice != "6"):
            print("Selection does not exit. Try again.")        

if __name__ == "__main__":
    main()