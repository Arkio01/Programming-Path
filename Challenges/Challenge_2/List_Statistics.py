def main():
    n_of_values = int(input("How many numbers would you like to enter? "))
    number_list = get_numbers(n_of_values)
    
# Prints output
    print(f"Numbers: {number_list}")
    print(f"Sum: {sum(number_list)}")
    print(f"Average: {average(number_list)}")
    print(f"Max: {max(number_list)}")
    print(f"Min: {min(number_list)}")
    
    
    
# Gets the amount of numbers necessary
def get_numbers(n_of_values):
    numbers = []
    
    for _ in range(0, n_of_values):
        numbers.append(int(input("Number: ")))
        
    return numbers
        
        
# Calculates the average
def average(number_list):
    count = 0
    
    for n in number_list:
        count += 1
        
    avrg = float(sum(number_list)) / float(count)
        
    return avrg
    
    
    
if __name__ == "__main__":
    main()