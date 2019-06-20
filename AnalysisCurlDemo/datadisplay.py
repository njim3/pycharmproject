# coding: utf-8
import xlrd
import datetime
import matplotlib.pyplot as plt


def str2date(strVal, dateFormat="%Y-%m-%d %H:%M:%S"):
    date = datetime.datetime.strptime(strVal, dateFormat)

    return date


def date2Str(date, dateFormat="%Y-%m-%d %H:%M:%S"):
    strVal = date.strftime(dateFormat)

    return strVal


def readDataFromExcelFile(fileName, start, end):
    workbook = xlrd.open_workbook(fileName)
    sheetName = workbook.sheet_names()[0]

    sheet = workbook.sheet_by_name(sheetName)

    print('SheetName: ' + sheetName)
    print('Rows: ' + str(sheet.nrows))
    print('Cols: ' + str(sheet.ncols))

    resultDictArr = []
    for i in range(start, end + 1):
        dateStr = sheet.cell_value(i, 2).strip()
        value = sheet.cell_value(i, 1)

        resultDictArr.append({dateStr: value})

    workbook.release_resources()
    del workbook

    return resultDictArr


def displayAllData(currentArr, kilnendArr, kilnBackendArr):
    timeArr = []
    currentValArr = []
    kilnendValArr = []
    kilnBackendValArr = []

    for i in range(0, len(currentArr)):
        timeArr.append(str2date(list(currentArr[i].keys())[0]))

        currentValArr.append(float(list(currentArr[i].values())[0]))
        kilnendValArr.append(float(list(kilnendArr[i].values())[0]))
        kilnBackendValArr.append(float(list(kilnBackendArr[i].values())[0]))

    print(timeArr)
    print(currentValArr)
    print(kilnendValArr)
    print(kilnBackendValArr)

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    plt.plot(timeArr, currentValArr, label=u"窑主机电流")
    plt.plot(timeArr, kilnendValArr, label=u"窑头温度")
    plt.plot(timeArr, kilnBackendValArr, label=u"窑尾温度")

    plt.legend()
    plt.show()


def main():
    currentArr = readDataFromExcelFile("data/processed/窑主机电流.xls", 1, 10116)
    kilnendArr = readDataFromExcelFile("data/processed/窑头温度.xls", 1, 10116)
    kilnBackendArr = readDataFromExcelFile("data/processed/窑尾温度.xls", 1, 10116)

    displayAllData(currentArr, kilnendArr, kilnBackendArr)


if __name__ == '__main__':
    main()
