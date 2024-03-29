# This program calculates the length of a right
# triangle's hypotenuse.
import math

def main():
    # Get the length of the triangle's two sides.
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))

    # Calculate the length of the hypotenuse.
    c = math.hypot(a, b)

    # Display the length of teh hyotenuse.
    print(f'The length of the hypotenuse is {c}.')

# Call the main function.
main()