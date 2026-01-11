def main():
    # loading from external file if available
    expenses = []
    try:
        with open ('expenses.txt', 'r') as f:
            for line in f:
                file_category_name, file_price_amount, file_note = line.removesuffix("\n").split(",")
                expenses.append({"category": file_category_name, "amount": int(file_price_amount), "note": file_note})
    except FileNotFoundError:
        print("File not found")
    
    # control pannel
    while True:
        
        print("\n")
        
        user_choice = get_option()
        
        if user_choice == 1:
            expense = add_expense(expenses)
            if expense == None:
                continue
            else:
                expenses.append(expense)
            
        elif user_choice == 2:
            view_all_expense(expenses)
            
        elif user_choice == 3:
            total_spent_variable = total_spent(expenses)
            print(total_spent_variable)
            
        elif user_choice == 4:
            total_by_category_variable = total_by_category(expenses)
            
        elif user_choice == 5:
            save_variable = save(expenses)
            break
            
        
# prompts the user and returns the choice
def get_option():
    while True:
        print("\n")
        print("1. Add expense")       
        print("2. View all expenses")       
        print("3. Total spent")       
        print("4. Total by category")       
        print("5. Save & exit")       
            
        user_input = int(input("Choose an option: "))
        
        if user_input not in range(1, 6):
            print("Not a valid option")
            continue
        else:
            return user_input
            
            
# updates the expenses by adding a new dictionary
def add_expense(expenses):
    expense = {}
    category_name = input("Category: ").lower().strip()
    categories = [expense["category"] for expense in expenses]
    if category_name in categories:
        print(f"{category_name} already exists.")
        return
    else:
        while True:
            value = (input("Value (or 'cancel' to stop the operation): "))
            if not value.isnumeric():
                if value.lower() == "cancel":
                    return 
                else:
                    print("Not a valid value. Please retry.")
                    print("")
                    continue
            else:
                value = int(value)
                break
            
        note = input("Note (or 'cancel' to stop the operation): ").lower().strip()
        
        expense.update({"category": category_name, "amount": value, "note": note})
        return expense
            
# prints all dictionaries 
def view_all_expense(expenses):
    for i in expenses:
        print(f"{i['category']} - {i['amount']} ({i['note']})")
    return

# returns the total sum of the amounts
def total_spent(expenses):
    amount_list = []
    for i in expenses:
        amount_list.append(i['amount'])
        
    return sum(amount_list)
    
# merges the price of identical categories into an universal one
def total_by_category(expenses):
    categories = []
    category_value_dict = {}
    for i in expenses:
        if i['category'] not in categories:
            categories.append(i['category'])
        else:
            continue
    for category in categories:
        for i in expenses:
            if category == i['category'] and category not in category_value_dict:
                category_value_dict[category] = i['amount']
            elif category == i['category'] and category in category_value_dict:
                category_value_dict[category] = category_value_dict.get(category) + i['amount']
            else:
                continue
    for i in category_value_dict:
        print(f"{i}: {category_value_dict.get(i)}")
        
    return
            

# saves the updated expenses to an external file
def save(expenses):
    with open ("expenses.txt", 'w') as f:
        for i in expenses:
            f.write(f"{i['category']},{i['amount']},{i['note']}\n")
    return


# calls main
if __name__ == "__main__":
    main()