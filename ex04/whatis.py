import sys

def check_number(num):
    if num % 2:
        return "I'm Odd."
    else:
        return "I'm Even."

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        result = check_number(number)
        print(result)
    else:
        print()
except AssertionError as error:
    print(AssertionError.__name__ + ":", error)