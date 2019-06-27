# coding: utf-8
import numpy as np


def getpolycurve(dataarr, degree, step):
    xarr = range(int(step / 2), len(dataarr) * step, step)

    coe = np.polyfit(xarr, dataarr, degree)
    p = np.poly1d(coe)

    return p


def getpolyderealroots(p, start, end):
    pder = np.polyder(p)

    rootndArray = np.sort(np.roots(pder))
    realRootndArray = rootndArray[np.isreal(rootndArray)]

    realRootList = list(realRootndArray.real)

    rootList = []
    for val in realRootList:
        if start < val <= end:
            rootList.append(val)

    return rootList


def getincanddecsec(p, rootlist, start, end):
    pder = np.polyder(p)

    incSecList = []
    decSecList = []

    rootlist.insert(start, 0)
    rootlist.append(end)

    for i in range(1, len(rootlist)):
        sec = [rootlist[i - 1], rootlist[i]]
        middle = (rootlist[i - 1] + rootlist[i]) / 2

        derMidVal = pder(middle)

        if derMidVal > 0:
            incSecList.append(sec)
        elif derMidVal < 0:
            decSecList.append(sec)

    return incSecList, decSecList


def getincanddecfitdate(incseclist, decseclist, datearr):
    incsecDateArr = []
    decsecDateArr = []

    for inc in incseclist:
        incsecDateArr.append([datearr[int(inc[0])], datearr[int(inc[1])]])

    for dec in decseclist:
        decsecDateArr.append([datearr[int(dec[0])], datearr[int(dec[1])]])

    return incsecDateArr, decsecDateArr


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


def getpolylineinincdecsec(p, incseclist, decseclist):
    incPolylineArr = []
    decPolylineArr = []

    for inc in incseclist:
        tempX = range(int(inc[0]), int(inc[1]))
        tempY = p(tempX)

        tempz = np.polyfit(tempX, tempY, 1)
        tempp = np.poly1d(tempz)

        incPolylineArr.append(tempp)

    for dec in decseclist:
        tempX = range(int(dec[0]), int(dec[1]))
        tempY = p(tempX)

        tempz = np.polyfit(tempX, tempY, 1)
        tempp = np.poly1d(tempz)

        decPolylineArr.append(tempp)

    return incPolylineArr, decPolylineArr
