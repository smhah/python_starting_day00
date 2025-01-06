import sys


def countUpperLetters(data):
    """
    Take a string and count upper letters
    return the result
    """
    count = sum(1 for char in data if char.isupper())
    return count


def countLowerLetters(data):
    """
    Take a data and count lower letters
    return the result
    """
    count = sum(1 for char in data if char.islower())
    return count


def countPunctuationMark(data):
    """
    Take a data and count punctuation mark
    return the result
    """
    punctuationMarks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    count = sum(1 for char in data if char in punctuationMarks)
    return count


def countSpaces(data):
    """
    Take a data and count spaces
    return the result

    """
    count = sum(1 for char in data if char.isspace())
    return count


def countDigits(data):
    """
    Take a data and count digits
    return the result
    """
    count = sum(1 for char in data if char.isdigit())
    return count


def main():
    """
    take input and count upper letters,
    lower letters, punctaion mark, spaces and digits.

    exeptions:
    If None or nothing is provided, the user is prompted to provide a string
    errors:
    If more than one argument is provided to the program,
    print an AssertionError.

    return string contains the total number of all characters plus
    each type in its own line

    """
    try:
        if len(sys.argv) == 1:
            text = input("What is the text to count?\n")
        elif len(sys.argv) > 2:
            raise AssertionError("Incorrect number of arguments")
        else:
            text = sys.argv[1]
        totalChars = len(text)
        print(f"The text contains {totalChars} characters:")
        print(f"{countUpperLetters(text)} upper letters")
        print(f"{countLowerLetters(text)} lower letters")
        print(f"{countPunctuationMark(text)} punctuation marks")
        print(f"{countSpaces(text)} spaces")
        print(f"{countDigits(text)} digits")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
