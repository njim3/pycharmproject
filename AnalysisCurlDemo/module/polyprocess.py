# coding: utf-8
import numpy as np


def getpolycurve(dataarr, degree):
    coe = np.polyfit(range(0, len(dataarr)), dataarr, degree)
    p = np.poly1d(coe)

    return p


def getpolyrealroots(p, start, end):
    pder = np.polyder(p)

    rootndArray = np.sort(np.roots(pder))
    realRootndArray = rootndArray[np.isreal(rootndArray)]

    realRootList = list(realRootndArray.real)

    rootList = []
    for val in realRootList:
        if start < val <= end:
            rootList.append(val)

    return rootList


def getincanddecsec(p, rootlist):
    pder = np.polyder(p)

    incSecList = []
    decSecList = []

    for i in range(1, len(rootlist)):
        sec = [rootlist[i - 1], rootlist[i]]
        middle = (rootlist[i - 1] + rootlist[i]) / 2

        derMidVal = pder(middle)

        if derMidVal > 0:
            incSecList.append(sec)
        elif derMidVal < 0:
            decSecList.append(sec)

    return incSecList, decSecList


def getpolylineinsec(p, rootlist, start, end):
    rootlist.append(start)
    rootlist.append(end)

    polylineArr = []

    for i in range(1, len(rootlist)):
        tempX = range(int(rootlist[i-1]), int(rootlist[i]))
        tempY = p(tempX)

        tempz = np.polyfit(tempX, tempY, 1)
        tempp = np.poly1d(tempz)

        polylineArr.append(tempp)

    return polylineArr
