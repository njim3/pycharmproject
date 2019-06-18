# coding: utf-8
import pandas as pd
import xlrd
import xlwt


def readcsv(filepath, encoding, rowstart, rowend, datecol, valcol, datescope=(),
            valscope=()):
    dataframe = pd.read_csv(filepath, encoding=encoding)

    dateArr = list(dataframe[dataframe.keys()[datecol]])
    valArr = list(dataframe[dataframe.keys()[valcol]])

    if rowend == -1:
        rowend = len(dateArr)

    dataArr = []
    for row in range(rowstart, rowend):
        tmpDateStr = str(dateArr[row]).strip()
        tmpValStr = str(valArr[row]).strip()

        if datescope:
            tmpDateStr = tmpDateStr[datescope[0]:datescope[1]]

        if valscope:
            tmpValStr = tmpValStr[valscope[0]:valscope[1]]

        dataArr.append({tmpDateStr: tmpValStr})

    return dataArr


def readxlsx(filepath, rowstart, rowend, datecol, valcol, datescope=(),
             valscope=()):
    workbook = xlrd.open_workbook(filepath)
    sheetName = workbook.sheet_names()[0]

    sheet = workbook.sheet_by_name(sheetName)

    if rowend == -1:
        rowend = sheet.nrows

    dataArr = []
    for row in range(rowstart, rowend):
        tmpDateStr = str(sheet.cell_value(row, datecol)).strip()
        tmpValStr = str(sheet.cell_value(row, valcol)).strip()

        if datescope:
            tmpDateStr = tmpDateStr[datescope[0]:datescope[1]]

        if valscope:
            tmpValStr = tmpValStr[valscope[0]:valscope[1]]

        dataArr.append({tmpDateStr: tmpValStr})

    return dataArr


def setExcelStyle(fontName, fontHeight, isDate=False,
                  dateformat='yyyy-mm-dd hh:mm:ss'):
    cellStyle = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = fontName
    font.height = fontHeight

    if isDate:
        cellStyle.num_format_str = dateformat

    cellStyle.font = font

    return cellStyle


def writeData2Excel(filePath, sheetName,
                    headerStyle, dataStyle,
                    headerArr, dataArr):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)

    # 写入表头
    for i in range(0, len(headerArr)):
        sheet.write(0, i, headerArr[i], headerStyle)

    for i in range(0, len(dataArr)):
        curArr = dataArr[i]

        for j in range(0, len(curArr)):
            sheet.write(i+1, j, curArr[j], dataStyle)

    workbook.save(filePath)
