# This program calculates gross pay.

def main():
    try:
        # Get the number of hours worked.
        hours = int(input('How many hours did you work? '))

        # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))

        # Calculate the gross pay.
        gross_pay = hours * gross_pay

        # Display the gross pay.
        print(f'Gross pay: ${gross_pay:,.2f}')
    except ValueError:
        print('ERROR: Hours worked and hourly pay rates must')
        print('be valid numbers.')

# Call the main function.
if __name__ == '__main__':
    main()