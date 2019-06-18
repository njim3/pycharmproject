# coding: utf-8
from util import fileutil
from module import dataprocess
from module import dataplot


def getcurveresult(filepath):
    dateValDictArr = fileutil.readcsv(filepath, 'gbk', 0, -1, 2, 1, (1, -1))
    filledDateValArr = dataprocess.fillDateAndVal(dateValDictArr)

    dateArr = []
    dataArr = []

    for dic in filledDateValArr:
        dateArr.append(list(dic.keys())[0])
        dataArr.append(float(list(dic.values())[0]))

    dataplot.plotsimpleline(dataArr)


def start():
    filePath = 'data/raw/crosssection.csv'

    getcurveresult(filePath)
