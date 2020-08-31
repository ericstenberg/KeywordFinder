# License: GNU Affero General Public License v3.0

from os import path, listdir
from os.path import join
from sys import exit


class SetupFiles:
    def __init__(self):
        self._importPath = ''
        self._fileList = []
        self._rawKeywordList = []

    def setImportPath(self, importPathIn):
        if path.isdir(importPathIn):
            print(importPathIn + ' found.')
            self._importPath = importPathIn
        else:
            print('Directory not found. Exiting program.')
            exit()

    def getImportPath(self):
        return self._importPath

    def setFilesList(self, importPathIn):
        self._fileList = [join(importPathIn, f) for f in listdir(importPathIn)
                          if f.endswith('.txt')]

    def getFilesList(self):
        return self._fileList

    def setRawKeywords(self, fileListIn):
        for file in fileListIn:
            with open(file, 'r', encoding='utf8') as f:
                self._rawKeywordList.append(f.read())

    def getRawKeywords(self):
        return self._rawKeywordList


def setupFiles():
    importPathIn = input('Enter filepath:\n')
    while(True):
        phraseLength = input('Enter maximum phrase length: ')
        if int(phraseLength) >= 1:
            print('The maximum phrase length is ' + phraseLength + '.')
            phraselengthInt = int(phraseLength)
            break
        elif int(phraseLength) == 0:
            print('Phrase length 0 is too short. Please try again.')
            continue
        elif phraseLength == 'q':
            print('''"q" selected. Exiting program.''')
            exit()
        else:
            print('Unknown entry. Please try again.')

    var = SetupFiles()
    var.setImportPath(importPathIn)
    var.setFilesList(var.getImportPath())
    var.setRawKeywords(var.getFilesList())
    rawKeywordsList = var.getRawKeywords()
    return rawKeywordsList, phraselengthInt