from homework3 import problem2


class PersonWithExceptions(problem2.Person):

    def __init__(self, name, last_name, age, gender, student, password):
        try:
            assert age >= 0, 'Age can\'t be negative'
        except Exception as e:
            print(e)

        super().__init__(name, last_name, age, gender, student, password)

    def read_file(self, filename):
        try:
            super().read_file(filename)
        except FileNotFoundError as e:
            print(e)