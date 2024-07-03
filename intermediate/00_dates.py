# Dates

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2025, 1, 15)

print_date(year_2023)

from datetime import time
current_time = time()

print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

diff = year_2023 - now  # Siempre que sean del mismo tipo
print(diff)