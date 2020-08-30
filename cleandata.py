# License: GNU Affero General Public License v3.0

import string as s


class CleanData:
    def __init__(self):
        self._cleanSeries = []

    def setCleanSeries(self, rawKeywordsList):
        for idx in range(0, len(rawKeywordsList)):
            rawKeywordsList[idx] = rawKeywordsList[idx].replace('\n', ' ')
            rawKeywordsList[idx] = rawKeywordsList[idx].translate(
                rawKeywordsList[idx].maketrans('', '', s.punctuation))
            rawKeywordsList[idx] = rawKeywordsList[idx].replace('''©''', '')
            rawKeywordsList[idx] = rawKeywordsList[idx].lower()
            rawKeywordsList[idx] = rawKeywordsList[idx].split()
        self._cleanSeries = rawKeywordsList

    def getCleanSeries(self):
        return self._cleanSeries


def cleanData(rawKeywordsList):
    var = CleanData()
    var.setCleanSeries(rawKeywordsList)
    return var.getCleanSeries()