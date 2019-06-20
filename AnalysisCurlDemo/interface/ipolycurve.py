# coding: utf-8
from util import fileutil
from module import dataprocess
from module import dataplot
from module import polyprocess


def getcurveresult(filepath):
    dateValDictArr = fileutil.readcsv(filepath, 'gbk', 0, -1, 2, 1, (1, -1))
    filledDateValArr = dataprocess.fillDateAndVal(dateValDictArr)

    step = 5
    ((dateArr, dataArr), (mergedDateArr, mergedDataArr)) = \
        dataprocess.mergedata(filledDateValArr, step)

    # polyfit
    degree = 10
    pFunc = polyprocess.getpolycurve(mergedDataArr, degree, step)

    # all real roots
    realRootList = polyprocess.getpolyderealroots(pFunc, 0, len(dataArr))

    # increase and decrease section
    (incSecList, decSecList) = polyprocess.getincanddecsec(pFunc, realRootList)

    # fit the date
    (incsecDateArr, decsecDateArr) = polyprocess.getincanddecfitdate(
        incSecList, decSecList, dateArr)

    print(incsecDateArr)
    print(decsecDateArr)

    # line fit
    (incPolylineArr, decPolylineArr) = polyprocess.getpolylineinincdecsec(
        pFunc, incSecList, decSecList)

    # plot
    dataplot.plot2linecurveandpolylinesec(dataArr, mergedDataArr, step,
                                          incSecList, decSecList,
                                          incPolylineArr, decPolylineArr,
                                          pFunc)


def start():
    filePath = 'data/raw/crosssection.csv'

    getcurveresult(filePath)
