import random
import sqlite3


def get_checksum_by_luhn_algorithm(num_card):
    all_sum = 0
    for i, d in enumerate(num_card, 1):
        all_sum += (int(d) * (2 ** (i % 2))) % 9

    ost_10 = all_sum % 10
    last_dig = 0 if not ost_10 else (10 - ost_10)
    return str(last_dig)


class MyBank:

    def __init__(self):
        self.bin_part = "400000"

        self.current_card = None
        self.status = "main_menu"

        self.conn = None
        self.make_base()

    def make_base(self):
        conn = sqlite3.connect("card.s3db")
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE if not exists card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0)""")

        self.conn = conn

    def get_menu_text(self):

        menu_text = ""
        if self.status == "main_menu":
            menu_text = "1. Create an account\n2. Log into account\n0. Exit\n"
        elif self.status == "card_info":
            menu_text = "1. Balance\n2. Log out\n0. Exit\n"

        return menu_text

    def menu_operations(self, user_input: str):

        print()

        if user_input == "0":

            self.exit_bank()

        elif self.status == "main_menu":

            if user_input == "1":
                self.create_account()
            elif user_input == "2":
                self.log_in_acc()

        elif self.status == "card_info":

            if user_input == "1":
                print(f"Balance: {self.current_card['balance']}")
            elif user_input == "2":
                print("You have successfully logged out!")
                self.status = "main_menu"

    def exit_bank(self):
        print("Bye!")
        self.status = "Exit"
        self.conn.close()

    def create_account(self):

        account_part = f"{random.randint(1, 999999999):09d}"
        pin = f"{random.randint(1, 9999):04d}"

        card_num = self.bin_part + account_part
        card_num += get_checksum_by_luhn_algorithm(card_num)

        cursor = self.conn.cursor()
        sql = "INSERT INTO card (number, pin) VALUES (:number, :pin)"
        cursor.execute(sql, {"number": card_num, "pin": pin})
        self.conn.commit()

        print("Your card has been created")
        print("Your card number:", card_num, sep="\n")
        print("Your card PIN:", pin, sep="\n")

    def log_in_acc(self):
        card_num = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")
        print()

        cursor = self.conn.cursor()
        cursor.execute("SELECT number, pin, balance FROM card where number=:number", {"number": card_num})
        result = cursor.fetchone()

        if result is None or pin != result["pin"]:
            print("Wrong card number or PIN!\n")
        else:
            print("You have successfully logged in!\n")
            self.status = "card_info"
            self.current_card = result


bank = MyBank()

while True:

    inp = input(bank.get_menu_text())

    bank.menu_operations(inp)

    if bank.status == "Exit":
        break
