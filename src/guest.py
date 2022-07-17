class Guest:
    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash

    def pay_for_room(self, cost):
        self.cash -= cost