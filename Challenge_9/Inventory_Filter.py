def main():
    inventory = {}
    try:
        with open ('inventory.txt', 'r') as f:
            for line in f:
                file_item_name, file_item_quantity, file_item_price = line.removesuffix("\n").split(",")
                inventory[file_item_name] = {"quantity": int(file_item_quantity), "price": int(file_item_price)}
    except FileNotFoundError:
        print("File not found")
    
    while True:
        
        print("\n")
        
        option = get_option()
        
        if option == 1:
            item_name = input("Item: ").lower()
            if item_name in inventory:
                print(f"'{item_name}' already exists.")
            else:
                item_quantity = int(input("Quantity: "))
                item_price = int(input("Price: "))
                inventory[item_name] = {"quantity": item_quantity, "price": item_price}
                print("Inventory was updated")
        elif option == 2:
            item_name = input("Item: ").lower()
            if item_name not in inventory:
                print(f"'{item_name}' doesn't exist.")
            else:
                item_quantity = int(input("New quantity: "))
                inventory[item_name]["quantity"] = item_quantity
                print("Inventory was updated")
        elif option == 3:
            for item in inventory:
                print(f"{item} - Qty: {inventory[item]['quantity']}, Price: {inventory[item]['price']}")
        elif option == 4:
            print(f"Total inventory value: {get_total_inventory_value(inventory)}")
        elif option == 5:
            break
        elif option == 6:
            item_name = input("Item: ").lower()
            if item_name in inventory:
                print(f"{item_name} - Qty: {inventory[item_name]['quantity']}, Price: {inventory[item_name]['price']}")
            else:
                print("Item not found.")
        elif option == 7:
            quantity_threshold = int(input("Quantity: "))
            empty = True
            for item in inventory:
                if inventory[item]['quantity'] < quantity_threshold:
                    empty = False
                    print(f"{item} - Qty: {inventory[item]['quantity']}, Price: {inventory[item]['price']}")
                else:
                    continue
            if empty == True:
                print("No item below this quantity")
    
    with open ('inventory.txt', 'w') as f:
        for item in inventory:
            f.write(f"{item},{inventory[item]['quantity']},{inventory[item]['price']}\n")
                
# Shows the menu and gets the user's input
def get_option():
    while True:
        print("\n")
        print("1. Add item")
        print("2. Update quantity")
        print("3. View inventory")
        print("4. Total value")
        print("5. Quit")
        print("6. Search item")
        print("7. Show items below quantity")
        
        user_input = int(input("Choose an option: "))
        
        if user_input not in range(1, 8):
            print("Not a valid option")
            continue
        else:
            return user_input
        
# Calculates the sum of all the prices multiplied to their quantity
def get_total_inventory_value(dictionary):
    price_list = []
    for item in dictionary:
        price_list.append(dictionary[item]["price"] * dictionary[item]["quantity"])
        
    return sum(price_list)
            
        
if __name__ == "__main__":
    main() 