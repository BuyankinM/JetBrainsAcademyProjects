from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        pass

    def add_interest(self):
        if self.interest:
            self.sum += self.interest * self.sum


class SavingsAccount(Account):
    def add_money(self, amount):
        if amount < 10:
            print("Cannot add to SavingsAccount: amount too low.")
            return None

        self.sum += amount


class Deposit(Account):
    def add_money(self, amount):
        if amount < 50:
            print("Cannot add to Deposit: amount too low.")
            return None

        self.sum += amount
