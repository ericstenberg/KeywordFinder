# License: GNU Affero General Public License v3.0

import importlib


def main():
    setupFilesModule = importlib.import_module('setupfiles')
    cleanDataModule = importlib.import_module('cleandata')
    processDateModule = importlib.import_module('processdata')
    outputReportModule = importlib.import_module('outputreport')
    rawKeywordsList, phraseLength = setupFilesModule.setupFiles()
    cleanedData = cleanDataModule.cleanData(rawKeywordsList)
#    oneWordSeries, twoWordSeries, threeWordSeries = processDateModule.processData(cleanedData)
#    outputReportModule.outputReport(oneWordSeries, twoWordSeries, threeWordSeries)
    outputReport = processDateModule.processData(cleanedData, phraseLength)
    outputReportModule.outputReport(outputReport)


if __name__ == '__main__':
    main()