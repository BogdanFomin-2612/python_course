import datetime

# utc_time = datetime.datetime.now(datetime.UTC)
# current_time = datetime.datetime.now()

# print(utc_time)
# print(current_time)
# print("Год ", current_time.year)
# print("Месяц ", current_time.month)
# print("День ", current_time.day)
# print("Час ", current_time.hour)
# print("Минута ", current_time.minute)
# print("Секунда", current_time.second)

# some_datetime = datetime.datetime(year=2021, month=5, day=8, hour=12, minute=33, second=45)
# print(some_datetime)

# current_datetime = datetime.date.today()
# print(current_date)

# current_datetime = datetime.datetime.now()
# day_ago = current_datetime - datetime.timedelta(days=1)
# print(day_ago)

# current_datetime = datetime.datetime.now()
# print(current_datetime.strftime("%A, %d %B %Y"))    #? Понятный формат для чтения

isoformat = "2026-09-09 17:27:43.138876"
my_datetime = datetime.datetime.fromisoformat(isoformat)
print(type(my_datetime))
print(my_datetime)