# count distinct words
# create/modify file with word/phrases and word/phrase count
# print report

import importlib


def main():
    setupFilesModule = importlib.import_module('setupfiles')
    # clean data
    # answer question
    #  count of 1 words
    #  count of 2 words
    #  count of 3 words
    # save report
    #  csv
    #  json

    rawKeywordsSeries = setupFilesModule.setupFiles()
    print(rawKeywordsSeries)

if __name__ == '__main__':
    main()