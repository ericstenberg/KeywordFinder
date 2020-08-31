# License: GNU Affero General Public License v3.0

import string as s


class CleanData:
    def __init__(self):
        self._cleanSeries = []

    def setCleanSeries(self, rawKeywordsListIn):
        for idx in range(0, len(rawKeywordsListIn)):
            rawKeywordsListIn[idx] = rawKeywordsListIn[idx].lower()
            rawKeywordsListIn[idx] = rawKeywordsListIn[idx].replace('\n', ' ')
            rawKeywordsListIn[idx] = rawKeywordsListIn[idx].translate(
                rawKeywordsListIn[idx].maketrans('', '', s.punctuation))
            rawKeywordsListIn[idx] = rawKeywordsListIn[idx].replace('''©''', '')
            rawKeywordsListIn[idx] = rawKeywordsListIn[idx].split()
        self._cleanSeries = rawKeywordsListIn

    def getCleanSeries(self):
        return self._cleanSeries


def cleanData(rawKeywordsList):
    var = CleanData()
    var.setCleanSeries(rawKeywordsList)
    return var.getCleanSeries()