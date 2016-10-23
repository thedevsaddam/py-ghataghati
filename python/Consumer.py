class Consumer(object):
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError("You don't have sufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance


motin = Consumer("Motin")
motin.deposit(1200)
print(motin.get_balance())
motin.withdraw(90)
print(motin.get_balance())
