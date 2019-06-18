# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    dataframe = pd.read_csv('data/crosssection.csv', encoding='gbk')
    valList = list(dataframe['值'].values)

    step = 10

    # find the proper value
    mergedLen = len(valList)
    while mergedLen % step:
        mergedLen -= 1

    mergedList = []
    tempSum = 0

    for i in range(0, mergedLen):
        if i != 0 and i % step == 0:
            mergedList.append(float(tempSum / step))
            tempSum = 0

        tempSum += valList[i]

    mergedList.append(float(tempSum) / step)

    xArr = range(0, len(valList))
    xMergeArr = range(int(step / 2), mergedLen, step)

    # poly fit
    poly = 10
    z1 = np.polyfit(xMergeArr, mergedList, poly)
    p1 = np.poly1d(z1)

    print(type(z1))
    print(type(p1))

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.plot(xArr, valList)
    plt.plot(xMergeArr, mergedList, label="step=" + str(step))
    plt.plot(xArr, p1(xArr), label="拟合poly=" + str(poly))

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
