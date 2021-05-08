class Car:

    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def compare_car(self, car2):
        return 'car1 is better than car2' if self.max_speed > car2.max_speed else 'car2 is better than car1'


car1 = Car('bmw', 'red', 150)
car2 = Car('lexus', 'red', 140)

print(car1.compare_car(car2))
print(car2.compare_car(car1))
