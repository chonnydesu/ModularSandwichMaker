
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredients, value in ingredients.items():  # loop through all ingredients (bread/ham/cheese)
            if self.machine_resources.get(ingredients, 0) < value:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
                   Hint: no output"""

        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity