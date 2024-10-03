def main():
    book_path = "books/mobydick.txt" # defines the path to the book being read and manipulated
    text = get_words(book_path) # gets the text of the book defined above
    word_count = count_words(text) # counts the amount of words in the book
    char_count = count_characters(text) # counts the amount of characters in the book
    char_count_list = [{"char": char, "num": count} for char, count in char_count.items()] # creates a list of the char_count dictionary's values
    char_count_list.sort(reverse=True, key=sort_and_count_letters)
    #print(text) # prints the entire book
    print (f"--- Begin report of {book_path} ---") # opening line of report
    print() # deadspace
    print(f"The book has {word_count} words.") # prints total amount of words in book
    print()
    print("The following is a count of all of the characters in the book, including spaces and non-letter characters:")
    print()
    print(char_count)
    print()
    print("Here is a list of the amount of times each letter appears in the book, sorted alphabetically:")
    for char in char_count_list:
        if char['char'].isalpha():
            print(f"The letter '{char['char']}' appears {char['num']} times")

# the following function reads the book
def get_words(book):
    with open(book) as f:
        return f.read()

# the following function takes a book and counts the words in it
def count_words(book):
    count = book.split()
    return len(count)

# the following function takes a book, counts the characters in it, and returns those characters in a dictionary
def count_characters(book):
    char_dict = {} 
    lowered = book.lower() # uses the lower function to make all of the characters in the book lowercase
    for char in lowered:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

# the following function sorts the letters in the book alphabetically and returns the amount of times they appear
def sort_and_count_letters(dict):
    return dict["num"]
main()