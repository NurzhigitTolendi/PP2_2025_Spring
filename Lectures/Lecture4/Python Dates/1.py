import datetime

now = datetime.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

my_date = datetime.datetime(2023, 9, 21, 22, 35, 0)
print(my_date)


formatted_date = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted_date)