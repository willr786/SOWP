# This program displays the total of the 
# amount in the sales_data.txt file.

def main():
    # Initialize an accumulator.
    total = 0.0

    try:
        # Open the sales_data.txt file.
        infile = open('sales_data.txt', 'r')

        # Read the values from the file and
        # accumulate them.
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file.
        infile.close()

        # Print the total.
        print(f'Total: {total:,.2f}')

    except:
        print('An error occured.')

# Call the main function.
if __name__ == '__main__':
    main()