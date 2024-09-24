import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_machine = SandwichMaker(resources)
cashier_instance = Cashier()
ordering = True


def main():
    while ordering:

        choice = input("What would you like? (small / medium / large / off / report) ")

        if choice == "small" or choice == "medium" or choice == "large":
            orderIngredients = recipes[choice]["ingredients"]
            orderCost = recipes[choice]["cost"]

            if sandwich_machine.check_resources(orderIngredients):
                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, orderCost):
                    sandwich_machine.make_sandwich(choice, orderIngredients)
                    print(f'{choice} sandwich is ready. Bon Appetit!')
                    print("")
                else:
                    print("Sorry that's not enough money. Money refunded. ")
                    print("")

            else:
                print("Sorry, there is not enough bread.")

        elif choice == "off":
            break

        elif choice == "report":

            print(f"Bread: {sandwich_machine.machine_resources["bread"]} slice(s)")
            print(f"Ham: {sandwich_machine.machine_resources["ham"]} slice(s)")
            print(f"Cheese: {sandwich_machine.machine_resources["cheese"]} pound(s)")


if __name__=="__main__":
    main()