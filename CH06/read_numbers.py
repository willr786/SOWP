# This program demonstrates how numbers that are
# read from a file must be converted from strings
# before they are used in a math operation.

from cmath import inf
from contextlib import nullcontext


def main():
    # Open a file for reading.
    infile = open('numbers.txt', 'r')

    # Read three numbers from the file.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Close the file.
    infile.close()

    # Add the three numbers.
    total = num1 + num2 + num3

    # Display the numbers and their totol.
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'Thier total is: {total}')

# Call the main function.
if __name__ == '__main__':
    main()