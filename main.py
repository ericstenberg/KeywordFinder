# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0

# count distinct words
# create/modify file with word/phrases and word/phrase count
# print report

import importlib


def main():
    setupFilesModule = importlib.import_module('setupfiles')
    cleanDataModule = importlib.import_module('cleandata')
    processDateModule = importlib.import_module('processdata')
    generateSaveReportModule = importlib.import_module('generatesavereport')
    # answer question/process data
    #  count of 1 words
    #  count of 2 words
    #  count of 3 words
    # generate/ave report
    #  csv
    #  json
    # add GUI

    rawKeywordsList = setupFilesModule.setupFiles()
    cleanedData = cleanDataModule.cleanData(rawKeywordsList)
    processedData = processDateModule.processData(cleanedData)
    print(cleanedData)

if __name__ == '__main__':
    main()