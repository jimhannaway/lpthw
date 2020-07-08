# Create the blockchain as a list
blockchain = [] # initialise and initially an empty list


# define a function to get the last value in the blockchain

def get_last_blockchain_value():
    """ index -1 accesses end of list and returns the last value of the blockchain """
    return blockchain[-1]


# function to add new values to the blockchain
# passes in arguments and also uses default argument of [1]
def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain
    Arguments:
        :transaction_amount: The new amount that should be added
        :last_transaction: The last blockchain transaction (default[1]).
        """
    blockchain.append([last_transaction, transaction_amount])



def get_user_input():
    """ Returns the user input, a new transaction amount, as a float """
    return float(input("Please enter your transaction amount: "))

# create nested list of blockchain values calling input function
tx_amount = get_user_input()
add_value(tx_amount)

# sample of using keyword arguments to call the function
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
