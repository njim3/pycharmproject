# coding: utf-8
import datetime


def str2date(strVal, dateFormat="%Y-%m-%d %H:%M:%S"):
    date = datetime.datetime.strptime(strVal, dateFormat)

    return date


def date2Str(date, dateFormat="%Y-%m-%d %H:%M:%S"):
    strVal = date.strftime(dateFormat)

    return strVal
