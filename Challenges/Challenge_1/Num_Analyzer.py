def main():
    user_input = int(input("Enter int: "))
    if user_input != 0:
        position, status = analyze(user_input)
        print(f"The number is {position} and {status}")
    else:
        print(f"The number is zero")
    
    
# Analyzes the int
def analyze(i):
    position = ""
    status = ""
    
    if i > 0:
        position = "positive"
    else:
        position = "negative"
    
    if is_even(i):
        status = "even"
    else:
        status = "odd"
        
    return position, status
    
    
    
# Checks if int is even or odd
def is_even(i):
    if i % 2 == 0:
        return True
    else:
        return False
    
    

if __name__ == "__main__":
    main()
