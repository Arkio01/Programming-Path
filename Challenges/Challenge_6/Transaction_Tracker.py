def main():
    categories_dict = get_dictionary()
    
    print("\n")
    
    for category in categories_dict:
        category_name = category
        category_value = categories_dict.get(category)
        print(f"{category_name}: {category_value}")
        
    print(f"Total spent: {get_value_sum(categories_dict)}")
        

def get_dictionary():
    categories_dict = {}
    while True:
        single_category = input("Enter category (or 'done' to stop): ").lower()
        if single_category == "done":
            break
        else:
            money_amount = int(input("Enter amount: "))
            if single_category not in categories_dict:
                categories_dict[single_category] = money_amount
            else:
                category_value = categories_dict.get(single_category)
                categories_dict[single_category] = category_value + money_amount
    return categories_dict

def get_value_sum(dictionary):
    values = []
    for category in dictionary:
        values.append(dictionary.get(category))
        
    return sum(values)

if __name__ == "__main__":
    main()
    