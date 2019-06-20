# coding: utf-8
import matplotlib.pyplot as plt


def plotsimpleline(dataArr):
    plt.plot(dataArr)

    plt.show()


def plot2lines(dataArr, mergedDataArr, step):
    xArr = range(0, len(dataArr), 1)
    xMergedArr = range(int(step / 2), len(mergedDataArr) * step, step)

    plt.plot(xArr, dataArr)
    plt.plot(xMergedArr, mergedDataArr)

    plt.show()


def plot2linesandcurve(dataArr, mergedDataArr, step, pFunc):
    xArr = range(0, len(dataArr))
    xMergedArr = range(int(step / 2), len(mergedDataArr) * step, step)

    plt.plot(xArr, dataArr)
    plt.plot(xMergedArr, mergedDataArr)
    plt.plot(xArr, pFunc(xArr))

    plt.show()


def plot2linecurveandpolylinesec(dataArr, mergedDataArr, step,
                                 incsecList, decsecList,
                                 incPolylineArr, decPolylineArr,
                                 pFunc):
    xArr = range(0, len(dataArr))
    xMergedArr = range(int(step / 2), len(mergedDataArr) * step, step)

    plt.plot(xArr, dataArr)
    plt.plot(xMergedArr, mergedDataArr)
    plt.plot(xArr, pFunc(xArr))

    for i in range(0, len(incsecList)):
        tempx = range(int(incsecList[i][0]), int(incsecList[i][1]))
        tempp = incPolylineArr[i]

        plt.plot(tempx, tempp(tempx), linewidth=2)

    for i in range(0, len(decsecList)):
        tempx = range(int(decsecList[i][0]), int(decsecList[i][1]))
        tempp = decPolylineArr[i]

        plt.plot(tempx, tempp(tempx), linewidth=2)

    plt.show()
