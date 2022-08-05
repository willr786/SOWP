# This program gets three names from the user
# and writes them to a file.

def main():
    # Get three names of three names.
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    # Open a file named fiends.txt.
    myFile = open('friends.txt', 'w')

    # Write the names to the file.
    myFile.write(name1 + '\n')
    myFile.write(name2 + '\n')
    myFile.write(name3 + '\n')

    # Close the file.
    myFile.close()
    print('The names were written to the friends.txt.')

# Call the main function.
if __name__ == '__main__':
    main()