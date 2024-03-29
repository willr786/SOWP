# This program imports the coin module and 
# creates an instance of the Coin class.

import coin

# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = coin.Coin()

    # Display the side of teh ocin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am going to toss teh coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Call the main function
if __name__ == '__main__':
    main()