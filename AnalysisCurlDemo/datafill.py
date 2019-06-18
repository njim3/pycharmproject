# coding: utf-8
import xlrd
import datetime
import xlwt


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
        dateStr = sheet.cell_value(i, 2).strip()[1:-1]
        value = sheet.cell_value(i, 1)

        resultDictArr.append({dateStr: value})

    workbook.release_resources()
    del workbook

    return resultDictArr


def fillDateAndVal(excelDictArr):
    priorDateDict = excelDictArr[0]
    priorDateStr = list(priorDateDict.keys())[0]

    resultArr = list()

    for i in range(1, len(excelDictArr)):
        curDateStr = list(excelDictArr[i].keys())[0]

        while priorDateStr != curDateStr:
            priorDate = str2date(priorDateStr) + \
                        datetime.timedelta(seconds=3)
            curDate = str2date(curDateStr)

            if priorDate > curDate:
                priorDateStr = date2Str(str2date(curDateStr) +
                                        datetime.timedelta(seconds=3))
                break

            tempDict = {priorDateStr: list(excelDictArr[i-1].values())[0]}

            if len(resultArr) == 0 or \
                    tempDict != resultArr[len(resultArr) - 1]:
                resultArr.append(
                    {priorDateStr: list(excelDictArr[i-1].values())[0]})

            priorDateStr = date2Str(str2date(priorDateStr) +
                                    datetime.timedelta(seconds=3))

        resultArr.append(excelDictArr[i])

    return resultArr


def setExcelStyle(fontName, fontHeight, isDate=False):
    cellStyle = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = fontName
    font.height = fontHeight

    if isDate:
        cellStyle.num_format_str = 'yyyy-mm-dd hh:mm:ss'

    cellStyle.font = font

    return cellStyle


def writeData2Excel(filePath, sheetName, dataArr):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)

    excelHeaderStyle = setExcelStyle(u'微软雅黑', 200)
    excelStyle = setExcelStyle(u'等线', 220)
    excelDateStyle = setExcelStyle(u'等线', 220, True)

    # 如果有表头的话，需要先写入一下表头数据
    headerArr = ["#", "值", "时间戳"]

    # 写入表头
    for i in range(0, len(headerArr)):
        sheet.write(0, i, headerArr[i], excelHeaderStyle)

    for i in range(0, len(dataArr)):
        curDict = dataArr[i]

        no = i + 1
        value = list(curDict.values())[0]
        time = list(curDict.keys())[0]

        sheet.write(i + 1, 0, no, excelStyle)
        sheet.write(i + 1, 1, value, excelStyle)
        sheet.write(i + 1, 2, time, excelDateStyle)

    workbook.save(filePath)


def main():
    fileName = "data/窑尾温度.xlsx"

    excelDictArr = readDataFromExcelFile(fileName, 1, 3941)

    filledArr = fillDateAndVal(excelDictArr)

    writeData2Excel("dataprocessed/窑尾温度.xls", "data", filledArr)


if __name__ == '__main__':
    main()
