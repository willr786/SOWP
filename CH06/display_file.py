# This program displays the contents
# of a file.

from importlib.resources import contents


def main():
    # Get the name of a file.
    filename = input('Enter a filename: ')

    # Open the file.
    infile = open(filename, 'r')

    # Read the file's contents.
    contents = infile.read()

    # Display the file's contents
    print(contents)

    # Close the file.
    infile.close()

# Call the main function.
if __name__ == '__main__':
    main()