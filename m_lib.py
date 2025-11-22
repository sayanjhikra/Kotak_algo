import datetime
import time


######### time functions ###########

# #Current unix time
def unix_time_stamp():
    date= datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)
    return round((date.total_seconds())*1000)

# #date_time to unixTimeStamp
def dt_ut(yyyy,mm,dd,hh,min):
    date_time = datetime.datetime(yyyy,mm,dd,hh,min)
    return round(time.mktime(date_time.timetuple()))*1000

# #unixTimeStamp to date_time
def ut_dt(unixTime):
    return datetime.datetime.fromtimestamp(unixTime / 1000)

# #next wednesday date
def expiry():
    test_date = datetime.date.today()
    days_delta = 3 - test_date.weekday() # 3 isfor thrusday, 0 for monday
    if days_delta <= 0:days_delta += 7
    res = test_date + datetime.timedelta(days_delta)
    return str(res)[2:].replace('-', '').replace('0', '')
# print(expiry())