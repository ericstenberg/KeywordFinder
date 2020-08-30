# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0
#from os import path
import os
import pandas as pd


class OutputReport:
    def __init__(self):
        self._outputDir = ''

    def setOutputDir(self):
        outputDir = os.getcwd() + r'''\output'''
        if os.path.isdir(outputDir):
            print(outputDir + ' exists.')
        else:
            print(outputDir + ' does not exist.')
            print('Creating new output directory.')
            os.mkdir(outputDir)
        self._outputDir = outputDir

    def getOutputDir(self):
        return self._outputDir

    def generateCSV(self, dataSeriesIn, outputDirIn):
        outputPath = outputDirIn + r'''\output.csv'''
        dataSeriesIn.to_csv(path_or_buf=outputPath)

    def generateJSON(self):
        pass

    def generateTXT(self):
        pass

    def generateSQL(self):
        pass


def outputReport(oneWordSeries, twoWordSeries, threeWordSeries):
    var = OutputReport()
    var.setOutputDir()
    var.generateCSV(oneWordSeries, var.getOutputDir())
    # output CSV
    # output JSON
    # output TXT
    # output SQL