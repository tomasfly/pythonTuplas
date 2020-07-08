# -*- coding: utf-8 -*-
import datetime

def calculateDate(year,month,day):
    date = datetime.datetime(year,month,day)
    date += datetime.timedelta(days=1)
    return date

print(calculateDate(2003,8,1))