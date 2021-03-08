from time import time


def timing(function):
    def wrap(self, second_person):
        start = time()
        function(self, second_person)
        end = time()
        print(end - start)

    return wrap


class Person:

    def __init__(self, name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password

    @timing
    def greeting(self, second_person):
        print('Welcome dear', second_person.name)

    def goodbye(self):
        print('Bye everyone!')

    def favorite_num(self, num1):
        return 'My favorite number is ' + str(num1)

    def read_file(self, filename):
        open(filename + ".txt", "r")

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

