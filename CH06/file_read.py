# This program reads and dsiplays the contents
# of the philosophers.txt file.
def main():
    # Open a file nameed philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(file_contents)

# Call the main function.
if __name__ == '__main__':
    main()