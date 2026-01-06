def main():
    user_input = input("Enter a sentence: ").lower()
    dictionary = get_dict(user_input)
    for pair in dictionary:
        print(f"{pair}: {dictionary.get(pair)}")
    
# Creates the dictionary and updates it as necessary
def get_dict(sentence):
    word_dict = {}
    word_list = sentence.split(" ")
    for word in word_list:
        if word not in word_dict:
            word_dict.update({word: 1})
        else:
            number = word_dict.get(word)
            new_number = number + 1
            word_dict.update({word: new_number})
    return word_dict
        
        
        
if __name__ == "__main__":
    main()