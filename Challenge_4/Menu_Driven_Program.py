def main():
    num_list = []
    while True:
        option_selector = get_option()
        # Case 1
        if option_selector == 1:
            user_input = int(input("What number would you like to add: "))
            if user_input not in num_list:
                num_list.append(user_input)
                print(f"{user_input} added.")
            else:
                print("The number already exists.")
        # Case 2
        elif option_selector == 2:
            user_input = int(input("What number would you like to remove: "))
            if user_input in num_list:
                num_list.remove(user_input)
                print(f"{user_input} removed.")
            else:
                print("Number not found.")
        # Case 3
        elif option_selector == 3:
            print(num_list)
        # Case 4
        else:
            break
            
    
# Gets the user's answer
def get_option():
    while True:
        print("\n")
        print("1. Add number")
        print("2. Remove number")
        print("3. View numbers")
        print("4. Quit number")
        
        user_input = int(input("Choose an option: "))
        
        if user_input not in range(1, 5):
            print("Not a valid option")
            continue
        else:
            return user_input
        
if __name__ == "__main__":
    main()