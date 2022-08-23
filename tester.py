import datetime
from dateutil.relativedelta import relativedelta
from datetime import date,datetime, timedelta
# today = date.today()
# first = today.replace(day=1)
# last_month = first -relativedelta(months=6)
# print(last_month)


# today = date.today()
# first = today.replace(day=1)
# last_month = first -relativedelta(months=1)
# print(last_month.strftime("%Y-%m-%d"))

# def last_day_of_month(any_day):
#     # The day 28 exists in every month. 4 days later, it's always next month
#     next_month = any_day.replace(day=28) + timedelta(days=4)
#     # subtracting the number of the current day brings us back one month
#     return next_month - timedelta(days=next_month.day)

# month=date.today().strftime("%m")
# yr=date.today().strftime("%Y")
# print(type(datetime(month)))
# print(yr)
# in_dat=last_day_of_month(date(yr, month, 1))
# print(in_dat) today6 = date.today()
today1 = date.today()
first1 = today1.replace(day=1)
last_month1 = first1 -relativedelta(months=5)

end_today1 = date.today()
end_first1 = end_today1.replace(day=1)
end_month1 = end_first1 -relativedelta(days=1)+relativedelta(months=1)

print(first1)
print(end_month1)