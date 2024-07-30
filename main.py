from collections import Counter

def count_words(text):
    """
    This function takes a string of text and returns the number of words in that text.
    """
    words = text.split()
    return len(words)

def load_text_from_file(file_path):
    """
    This function reads the content of a file and returns it as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_characters(text):
    """
    This function takes a string of text and returns a dictionary with the count of each character.
    Characters are converted to lowercase to ensure that duplicates are not counted separately.
    """
    # Convert text to lowercase to ensure characters are counted in a case-insensitive manner
    text = text.lower()
    # Use Counter to count the occurrences of each character
    return dict(Counter(text))

def create_report(word_count, char_count):
    """
    This function takes the word count and character count dictionary,
    and returns a formatted report as a string.
    """
    report = f"The book contains {word_count} words!\n\n"
    report += "Character counts:\n"
    for char, count in sorted(char_count.items()):
        report += f"'{char}': {count}\n"
    return report

def main():
    # Load the book text from the file
    file_path = "books/frankenstein.txt"
    book_text = load_text_from_file(file_path)
    
    if book_text is not None:
        # Count the number of words in the book text
        word_count = count_words(book_text)
        
        # Count the number of each character in the book text
        char_count = count_characters(book_text)
        
        # Create and print the report
        report = create_report(word_count, char_count)
        print(report)

if __name__ == "__main__":
    main()

