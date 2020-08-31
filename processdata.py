# License: GNU Affero General Public License v3.0
#
#
# processdata.py inputs the raw keywords list and outputs word and phrase
# counts pandas series.

import pandas as pd
from nltk.corpus import stopwords


class ProcessData:
    def __init__(self):
        self._wordCountSeries = pd.Series([])

    def setWordCountSeries(self, cleanedDataIn, phraseLength):
        for idxTopLevel in cleanedDataIn:
            for n in range(0, phraseLength):
                for idx in range(0, len(idxTopLevel)-n):
                    tempStr = " ".join(idxTopLevel[idx:idx+n+1])
                    if tempStr in stopwords.words("english"):
                        continue
                    if tempStr in self._wordCountSeries.index:
                        temp = self._wordCountSeries.get(tempStr) + 1
                        self._wordCountSeries.update(pd.Series(
                            temp, index=[tempStr]))
                    elif tempStr not in self._wordCountSeries.index:
                        self._wordCountSeries = self._wordCountSeries.append(
                            pd.Series(1, index=[tempStr]))
                    else:
                        print('Value not recognized')
        self._wordCountSeries = self._wordCountSeries.sort_values(
            ascending=False, kind='mergesort')

    def getWordCountSeries(self):
        return self._wordCountSeries


def processData(cleanedDataIn, phraseLengthIn):
    var = ProcessData()
    var.setWordCountSeries(cleanedDataIn, phraseLengthIn)
    return var.getWordCountSeries()