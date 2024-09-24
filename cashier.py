class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        print(f"Please insert coins.")

        coins = {'large dollars': 1, 'half dollars': 0.5, 'quarters': 0.25,
                 'nickels': 0.05}  # create a dictionary for the money
        total = 0
        for option in coins:
            try:
                amount = int(input(f'how many {option}?: '))
                total += amount * coins[option]

            except ValueError:
                pass

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

        if coins < cost:
            return False

        else:
            change = coins - cost
            if change >= 0:
                print(f'Here is ${change} in change')
            return True