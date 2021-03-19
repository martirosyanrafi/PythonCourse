class MyTime:

    def __init__(self, t):
        self.t = t

    def print_time(self):
        print("The current time is", self.t)


class MyDate:

    def __init__(self, d):
        self.d = d

    def print_date(self):
        print("The current date is", self.d)


class DaTeTime(MyTime, MyDate):

    def __init__(self, d, t):
        MyDate.__init__(self, d)
        MyTime.__init__(self, t)


date_time = DaTeTime("13.03.2013", "12 PM")
date_time.print_time()
date_time.print_date()
