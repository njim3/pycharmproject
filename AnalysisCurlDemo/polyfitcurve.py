# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


def processPolynomial():
    coeffList = [-1.5377314516830147e-19, 2.7080330141703354e-16,
                 -2.0354287925224932e-13, 8.509453363535886e-11,
                 -2.1613413908534328e-08, 3.421868220775754e-06,
                 -0.0003338634772017371, 0.019201008587055427,
                 -0.592968080070796, 8.0249123841385, 312.04031790523226]

    z1 = np.array(coeffList)
    p1 = np.poly1d(z1)
    derp1 = np.polyder(p1)

    # print(p1)
    rootndArray = np.sort(np.roots(derp1))
    realRootndArray = rootndArray[np.isreal(rootndArray)]

    realRootList = list(realRootndArray.real)

    start = 0
    end = 350

    rootList = []
    for val in realRootList:
        if start < val <= end:
            rootList.append(val)

    print("All real roots:")
    print(rootList)

    rootList.insert(0, start)
    rootList.append(end)

    incSecList = []
    decSecList = []

    for i in range(1, len(rootList)):
        sec = [rootList[i-1], rootList[i]]
        middle = (rootList[i-1] + rootList[i]) / 2

        derMidVal = derp1(middle)

        if derMidVal > 0:
            incSecList.append(sec)
        elif derMidVal < 0:
            decSecList.append(sec)

    print("\nIncrease Section:")
    for sec in incSecList:
        print(sec)

    print("\nDecrease Section:")
    for sec in decSecList:
        print(sec)

    # plot the result
    xArr = range(start, end)
    yArr = p1(xArr)

    plt.plot(xArr, yArr)

    for i in range(1, len(rootList) - 1):
        plt.scatter(rootList[i], p1(rootList[i]), color='r')

        tmpX = round(rootList[i], 2)
        tmpY = round(p1(tmpX), 2)
        xy = (tmpX, tmpY)

        plt.annotate(str(xy), xy=xy, fontsize=10)

    # get segment poly=1 fit straight line
    for i in range(1, len(rootList)):
        tempX = range(int(rootList[i-1]), int(rootList[i]))
        tempY = p1(tempX)

        tempz = np.polyfit(tempX, tempY, 1)
        tempp = np.poly1d(tempz)

        print(tempp)

        plt.plot(tempX, tempp(tempX), linewidth=2)

    plt.show()


def main():
    processPolynomial()


if __name__ == '__main__':
    main()
