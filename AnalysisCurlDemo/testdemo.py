# coding: utf-8
import xlrd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline


def readDataFromExcelFile(fileName, start, end):
    workbook = xlrd.open_workbook(fileName)
    sheetNames = workbook.sheet_names()
    sheetName = sheetNames[0]

    sheet = workbook.sheet_by_name(sheetName)

    print('SheetName: ' + sheetName)
    print('Rows: ' + str(sheet.nrows))
    print('Cols: ' + str(sheet.ncols))

    dataArr = []
    per20Arr = []

    for i in range(start, end + 1):
        per20Arr.append(float(sheet.cell_value(i, 1)))
        dataArr.append(per20Arr)
        per20Arr = []
        # per20Arr.append(float(sheet.cell_value(i, 1)))

        # if len(per20Arr) % 20 == 0:
        #     dataArr.append(per20Arr)

        #     per20Arr = []

    workbook.release_resources()
    del workbook

    return dataArr


def processData(dataArr):
    dataLen = len(dataArr)

    xArr = np.arange(1, dataLen + 1, 1)
    yArr = np.array(dataArr)

    step = 20

    while dataLen % step:
        dataLen -= 1

    xShapedArr = np.arange(int(step / 2), dataLen, step)
    yShapeArr = np.array(dataArr[0:dataLen]).reshape(
        int(dataLen / step), step)

    yShapeMeanArr = np.mean(yShapeArr, axis=1)

    xSmoothArr = np.linspace(xShapedArr.min(), xShapedArr.max(),
                             len(xShapedArr) * 4)
    # ySmoothArr = Bspline(xShapedArr, yShapeMeanArr, xSmoothArr)
    ySmoothArr = spline(xShapedArr, yShapeMeanArr, xSmoothArr)

    # poly fit
    deg = 10
    z1 = np.polyfit(xShapedArr, yShapeMeanArr, deg)
    p1 = np.poly1d(z1)

    print(p1)

    plt.plot(xArr, yArr, color='y', label='basic data', linewidth=2)
    plt.plot(xShapedArr, yShapeMeanArr, linewidth=4,
             color='g', label='step=' + str(step))
    plt.plot(xSmoothArr, ySmoothArr, linewidth=2,
             color='b', label='step=' + str(step))
    plt.plot(xShapedArr, p1(xShapedArr), linewidth=1, marker='*',
             color='r', label='Polyfit(deg=' + str(deg) + ')')

    plt.legend()

    plt.show()


def main():
    # datafile: 窑头温度.xlsx
    dataKilnPriorTempArr = readDataFromExcelFile("data/窑头温度.xlsx", 1, 6079)

    # datafile: 窑尾温度.xlsx
    dataKilnRearTempArr = readDataFromExcelFile("data/窑尾温度.xlsx", 1, 3941)

    #datafile: 窑主机电流.xlsx
    dataKilnCurrentArr = readDataFromExcelFile("data/窑主机电流.xlsx", 1, 9960)






if __name__ == '__main__':
    main()
