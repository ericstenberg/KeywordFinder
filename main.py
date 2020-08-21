# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# select path
# import txt files
# place text into data frame
# count distinct words
# create/modify file with word/phrases and word/phrase count
# print report

import importlib


def main():
    setupFilesModule = importlib.import_module('setupfiles')
    filePath = input('Enter filepath:\n')
    rawKeywordsSeries = setupFilesModule.setupFiles(filePath)
    print(rawKeywordsSeries)

if __name__ == '__main__':
    main()