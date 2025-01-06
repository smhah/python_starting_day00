import sys
from ft_filter import ft_filter


def main():
    """
    program that accepts two arguments: a string S and an integer N.
    output a list of words from S that have length greater than N.
    errors: If the number of argument is different from 2,
    or if the type of any argument is wrong,
    the program prints an AssertionError
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        lst = string.split()
        res = list(ft_filter(lambda word: len(word) > number, lst))
        print(res)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
