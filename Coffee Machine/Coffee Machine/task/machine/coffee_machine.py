class CoffeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.status = "main menu"

    def get_command(self, user_input):

        if user_input == "exit":

            self.status = "exit"

        elif user_input == "remaining":

            self.print_status()

        elif oper == "buy":

            self.status = "choose coffee"
            print()

        elif self.status == "choose coffee":

            self.buy_coffee(user_input)

        elif user_input == "fill":

            self.status = "fill water"

        elif self.status.startswith("fill"):

            self.fill_coffee(user_input)

        else:

            self.take_money()

    def print_status(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{'$' if self.money else ''}{self.money} of money\n")

    def buy_coffee(self, coffee_type):
        water_cup, milk_cup, beans_cup, money_cup = 0, 0, 0, 0

        if coffee_type == "1":
            water_cup, beans_cup, money_cup = 250, 16, 4
        elif coffee_type == "2":
            water_cup, milk_cup, beans_cup, money_cup = 350, 75, 20, 7
        elif coffee_type == "3":
            water_cup, milk_cup, beans_cup, money_cup = 200, 100, 12, 6
        elif coffee_type == "back":
            self.status = "main menu"
            return

        list_error = []
        if self.water < water_cup:
            list_error.append("water")
        if self.beans < beans_cup:
            list_error.append("coffee beans")
        if self.milk < milk_cup:
            list_error.append("milk")
        if self.cups == 0:
            list_error.append("disposable cups")

        if list_error:
            print(f"Sorry, not enough {' '.join(list_error)}!\n")
        else:
            self.water -= water_cup
            self.beans -= beans_cup
            self.milk -= milk_cup
            self.cups -= 1
            self.money += money_cup
            print("I have enough resources, making you a coffee!\n")

        self.status = "main menu"

    def fill_coffee(self, fill_add):

        if self.status == "fill water":

            self.water += int(fill_add)
            self.status = "fill milk"

        elif self.status == "fill milk":

            self.milk += int(fill_add)
            self.status = "fill beans"

        elif self.status == "fill beans":

            self.beans += int(fill_add)
            self.status = "fill cups"

        elif self.status == "fill cups":

            self.cups += int(fill_add)
            self.status = "main menu"

    def take_money(self):

        print(f"I gave you ${self.money}")
        self.money = 0


my_lovely_coffee_machine = CoffeMachine()

while True:

    status_text = ""

    if my_lovely_coffee_machine.status == "main menu":

        status_text = "Write action (buy, fill, take, remaining, exit):\n"

    elif my_lovely_coffee_machine.status == "choose coffee":

        status_text = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"

    elif my_lovely_coffee_machine.status == "fill water":

        status_text = "Write how many ml of water do you want to add:\n"

    elif my_lovely_coffee_machine.status == "fill milk":

        status_text = "Write how many ml of milk do you want to add:\n"

    elif my_lovely_coffee_machine.status == "fill beans":

        status_text = "Write how many grams of coffee beans do you want to add:\n"

    elif my_lovely_coffee_machine.status == "fill cups":

        status_text = "Write how many disposable cups of coffee do you want to add:\n"

    elif my_lovely_coffee_machine.status == "exit":

        break

    oper = input(status_text)
    my_lovely_coffee_machine.get_command(oper)
