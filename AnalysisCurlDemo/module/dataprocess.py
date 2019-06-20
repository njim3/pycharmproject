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


def mergedata(dateValArr, step):
    dateArr = []
    dataArr = []

    for dic in dateValArr:
        dateArr.append(list(dic.keys())[0])
        dataArr.append(float(list(dic.values())[0]))

    # find the proper value
    mergedLen = len(dataArr)
    while mergedLen % step:
        mergedLen -= 1

    mergedDataArr = []
    tempSum = 0

    for i in range(0, mergedLen):
        if i != 0 and i % step == 0:
            mergedDataArr.append(float(tempSum / step))
            tempSum = 0

        tempSum += dataArr[i]

    mergedDataArr.append(float(tempSum) / step)

    mergedDateArr = []

    for i in range(0, len(mergedDataArr)):
        mergedDateArr.append(dateArr[int(step / 2 + i * step)])

    return (dateArr, dataArr), (mergedDateArr, mergedDataArr)
