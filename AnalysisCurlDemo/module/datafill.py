# coding: utf-8
from util import datetimeutil


# dictArr: [{'2019-05-17 09:37:02':370.42},...]
def fillDateAndVal(excelDictArr):
    priorDateDict = excelDictArr[0]
    priorDateStr = list(priorDateDict.keys())[0]

    resultArr = list()

    for i in range(1, len(excelDictArr)):
        curDateStr = list(excelDictArr[i].keys())[0]

        while priorDateStr != curDateStr:
            priorDate = datetimeutil.str2date(priorDateStr) + \
                        datetimeutil.datetime.timedelta(seconds=3)
            curDate = datetimeutil.str2date(curDateStr)

            if priorDate > curDate:
                priorDateStr = datetimeutil.date2Str(
                    datetimeutil.str2date(curDateStr) +
                    datetimeutil.datetime.timedelta(seconds=3))
                break

            tempDict = {priorDateStr: list(excelDictArr[i-1].values())[0]}

            if len(resultArr) == 0 or \
                    tempDict != resultArr[len(resultArr) - 1]:
                resultArr.append(
                    {priorDateStr: list(excelDictArr[i-1].values())[0]})

            priorDateStr = datetimeutil.date2Str(
                datetimeutil.str2date(priorDateStr) +
                datetimeutil.datetime.timedelta(seconds=3))

        resultArr.append(excelDictArr[i])

    print(len(resultArr))

    return resultArr
