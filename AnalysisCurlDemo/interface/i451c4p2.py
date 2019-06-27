# coding: utf-8
from util import fileutil
from module import dataprocess
from module import dataplot
from module import polyprocess
import _thread


def getcurveresult(filledDateValArr):

    step = 5
    ((dateArr, dataArr), (mergedDateArr, mergedDataArr)) = \
        dataprocess.mergedata(filledDateValArr, step)

    # polyfit
    degree = 15
    pFunc = polyprocess.getpolycurve(mergedDataArr, degree, step)

    # all real roots
    realRootList = polyprocess.getpolyderealroots(pFunc, 0, len(dataArr))

    # increase and decrease section
    (incSecList, decSecList) = polyprocess.getincanddecsec(pFunc, realRootList,
                                                           0, len(dataArr) - 1)

    print(incSecList)
    print(decSecList)

    # fit the date
    (incsecDateArr, decsecDateArr) = polyprocess.getincanddecfitdate(
        incSecList, decSecList, dateArr)

    print(incsecDateArr)
    print(decsecDateArr)

    # line fit
    (incPolylineArr, decPolylineArr) = polyprocess.getpolylineinincdecsec(
        pFunc, incSecList, decSecList)

    print([p.coefficients[0] for p in incPolylineArr])
    print([p.coefficients[0] for p in decPolylineArr])

    print('\n')

    # plot
    dataplot.plot2linecurveandpolylinesec(dataArr, mergedDataArr, step,
                                          incSecList, decSecList,
                                          incPolylineArr, decPolylineArr,
                                          pFunc)


def start():
    filePath = 'data/raw/451_c4_p2#mv.csv'
    dateValDictArr = fileutil.readcsv(filePath, 'gbk', rowstart=399245, rowend=-1,
                                      datecol=2, valcol=1, datescope=(1, -1))
    filledDateValArr = dataprocess.fillDateAndVal(dateValDictArr)

    getcurveresult(filledDateValArr)
    getcurveresult(filledDateValArr[10208:10508])
    getcurveresult(filledDateValArr[10376:-1])

    dataplot.showplot()
