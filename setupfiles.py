from os import path, listdir
from os.path import join
from sys import exit
import pandas as pd


class SetupFiles:
    def __init__(self):
        self._importPath = ''
        self._fileList = []
        self._rawKeywordList = pd.Series([], dtype="string")

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
                self._rawKeywordList = self._rawKeywordList.append(pd.Series(
                    f.read().replace('\n', ' '), dtype="string"))

    def getRawKeywords(self):
        return self._rawKeywordList


def setupFiles():
    importPathIn = input('Enter filepath:\n')
    var = SetupFiles()
    var.setImportPath(importPathIn)
    var.setFilesList(var.getImportPath())
    var.setRawKeywords(var.getFilesList())
    rawKeywordsSeries = var.getRawKeywords()
    return rawKeywordsSeries