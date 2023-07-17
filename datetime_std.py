from datetime import date, datetime, timedelta
from pprint import pprint


pprint(dir(datetime))

# date constructor
date_obj = date(2021, 8, 17)
# methods for date class

print(date_obj.day, date_obj.month, date_obj.year,
      date_obj.weekday(),
      date_obj.isoweekday(),
      date_obj.replace(month=11))
# for weekday(): Monday = 0, Sunday = 6
# for isoweekday() Monday = 1, Sunday = 7

print('Isoformat: ', date_obj.isoformat(), "\nCtime: ", date_obj.ctime())

# or https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# print(datetime.now().strftime(format_string))
format_string = '%m-%d-%Y %H:%M:%S'
print(datetime.now().strftime(format_string))
format_string = '%m-%d-%Y %H:%M'
print(datetime.now().strftime(format_string))
format_string = '%m-%d-%Y'
print(datetime.now().strftime(format_string))
format_string = '%H:%M:%S'
print(datetime.now().strftime(format_string))
format_string = '%b-%d-%Y %H:%M:%S'
print(datetime.now().strftime(format_string))
format_string = '%B-%A-%Y %H:%M:%S:%f'
print(datetime.now().strftime(format_string))


# Strptime(): converts a string into a datetime object
datetime_string = '2021-07-26T16:39:07.104867'
date_obj = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S.%f')
assert isinstance(date_obj, datetime)
print("default format:", date_obj, "isoformat:", date_obj.isoformat())


# timedelta
now = datetime.now()
thirty_days = timedelta(days=30, hours=2, minutes=10)
print(now + thirty_days)

tomorrow = timedelta(days=+1)
print(now + tomorrow)

delta = timedelta(days=+3, hours=-4)
print(now + delta)
