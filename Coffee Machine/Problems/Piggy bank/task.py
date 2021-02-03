class PiggyBank:
    def __init__(self, dollars, cents):
        self.cents = cents
        self.dollars = dollars

    def add_money(self, deposit_dollars, deposit_cents):
        new_sum_of_cents = self.cents + deposit_cents
        self.dollars += deposit_dollars + new_sum_of_cents // 100
        self.cents = new_sum_of_cents % 100