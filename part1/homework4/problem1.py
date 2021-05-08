class Calculation:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        print(self.x + self.y)

    def subtraction(self):
        print(self.x - self.y)


class MyCalculation(Calculation):

    def __init__(self, x, y):
        super().__init__(x, y)

    def multiplication(self):
        print(self.x * self.y)

    def division(self):
        print(self.x / self.y)


calculation = MyCalculation(3, 5)
calculation.addition()
calculation.subtraction()
calculation.multiplication()
calculation.division()
