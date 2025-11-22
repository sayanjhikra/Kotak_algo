import datetime
import time
#( mili to  second )


def current_time():
    cTime = str(time.strftime("%H:%M:%S")).split(':')
    return[int(cTime[0]), int(cTime[1]), int(cTime[2])]


# #Current unix time
def unix_time_stamp():
    date= datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)
    seconds =(date.total_seconds())
    return round(seconds)


# #date_time to unixTimeStamp
def dt_ut(yyyy,mm,dd,hh,min):
    date_time = datetime.datetime(yyyy,mm,dd,hh,min)
    return round(time.mktime(date_time.timetuple()))


# print(dt_ut(2023, 1, 4, 9, 15))

# today = str(datetime.date.today())
# s_date = list(map(int, today.split('-')))
# print(s_date)
# print(dt_ut(s_date[0], s_date[1], s_date[2], 9, 15))


# #unixTimeStamp to date only 
def ut_d(unixTime):
    my_datetime = str(datetime.datetime.fromtimestamp(unixTime)).split(' ')
    # d_time = my_datetime[1].split(':')
    cDate = my_datetime[0].split('-')
    return [int(cDate[0]), int(cDate[1]), int(cDate[2])]


# #unixTimeStamp to time only 
def ut_t(unixTime):
    my_datetime = str(datetime.datetime.fromtimestamp(unixTime)).split(' ')
    d_time = my_datetime[1].split(':')
    return [int(d_time[0]), int(d_time[1]), int(d_time[2])]


# #unixTimeStamp to date_time
def ut_dt(unixTime):
    my_datetime = str(datetime.datetime.fromtimestamp(unixTime)).split(' ')
    cDate = my_datetime[0].split('-')
    d_time = my_datetime[1].split(':')
    return [int(cDate[0]), int(cDate[1]), int(cDate[2]), int(d_time[0]), int(d_time[1]), int(d_time[2])]


# print(ut_dt(unixTimeStamp()))
# print(type(ut_dt(1673595900)))
# print(ut_dt(1704251098))
