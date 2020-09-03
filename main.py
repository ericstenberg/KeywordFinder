# License: GNU Affero General Public License v3.0

import importlib


def main():
    setupFilesModule = importlib.import_module('setupfiles')
    cleanDataModule = importlib.import_module('cleandata')
    processDataModule = importlib.import_module('processdata')
    outputReportModule = importlib.import_module('outputreport')
    rawKeywordsList, phraseLength = setupFilesModule.setupFiles()
    cleanedData = cleanDataModule.cleanData(rawKeywordsList)
    wordCountSeries = processDataModule.processData(cleanedData, phraseLength)
    outputReportModule.outputReport(wordCountSeries)


if __name__ == '__main__':
    main()