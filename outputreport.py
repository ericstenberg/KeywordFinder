# License: GNU Affero General Public License v3.0

import os


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

    def generateCSV(self, wordCountSeriesIn, outputDirIn):
        outputPath = outputDirIn + r'''\output.csv'''
        wordCountSeriesIn.to_csv(path_or_buf=outputPath)

    def generateJSON(self, wordCountSeriesIn, outputDirIn):
        outputPath = outputDirIn + r'''\output.json'''
        wordCountSeriesIn.to_json(path_or_buf=outputPath)

    def generateSQL(self):
        # Future update
        pass


def outputReport(wordCountSeriesIn):
    var = OutputReport()
    var.setOutputDir()
    var.generateCSV(wordCountSeriesIn, var.getOutputDir())
    var.generateJSON(wordCountSeriesIn, var.getOutputDir())