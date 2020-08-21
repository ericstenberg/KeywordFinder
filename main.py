# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0

# count distinct words
# create/modify file with word/phrases and word/phrase count
# print report

import importlib


def main():
    setupFilesModule = importlib.import_module('setupfiles')
    cleanDataModule = importlib.import_module('cleandata')
    # answer question
    #  count of 1 words
    #  count of 2 words
    #  count of 3 words
    # save report
    #  csv
    #  json
    # add GUI

    rawKeywordsSeries = setupFilesModule.setupFiles()
    cleanedData = cleanDataModule.cleanData(rawKeywordsSeries)

if __name__ == '__main__':
    main()