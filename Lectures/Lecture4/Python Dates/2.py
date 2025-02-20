import datetime

date_str = "12-02-2025 14:30"
date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print(date_obj) # 2025-02-12 14:30:00 

now = datetime.datetime.now()
delta = datetime.timedelta(days=5)
new_date = now + delta
print(new_date)

date1 = datetime.datetime(2025, 2, 20)
date2 = datetime.datetime(2025, 2, 12)
diff = date1 - date2 
print(diff) # 8 days, 0:00:00