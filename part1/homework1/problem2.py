import datetime
import time
import calendar

print("2)")
birthday = datetime.datetime(1999, 3, 3)
print(" a)", birthday)
print(" b)", birthday.year)
print(" c)", birthday.month)
print(" d)", birthday.day)
print(" e)", birthday.weekday())

today = datetime.datetime.now()
nextBirthday = datetime.datetime(2021, 3, 3)
print(" f)", (nextBirthday - today).days)

print("3)", "\n", calendar.month(2017, 5))

yesterday = today - datetime.timedelta(days=1)
print("4)", yesterday)
print(" a)", yesterday + datetime.timedelta(days=2))
print(" b)", yesterday - datetime.timedelta(days=3))
