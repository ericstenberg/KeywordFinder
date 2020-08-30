# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0
#
# count distinct words
# create/modify file with word/phrases and word/phrase count
# print report


import importlib


def main():
    setupFilesModule = importlib.import_module('setupfiles')
    cleanDataModule = importlib.import_module('cleandata')
    processDateModule = importlib.import_module('processdata')
    outputReportModule = importlib.import_module('outputreport')
    # add GUI
    # add web scraper
    # add keyword extractor from potential position

    rawKeywordsList = setupFilesModule.setupFiles()
    cleanedData = cleanDataModule.cleanData(rawKeywordsList)
    oneWordSeries, twoWordSeries, threeWordSeries = processDateModule.processData(cleanedData)
    outputReportModule.outputReport(oneWordSeries, twoWordSeries, threeWordSeries)


if __name__ == '__main__':
    main()