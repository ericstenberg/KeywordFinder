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
                    if tempStr in stopwords:
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
    #
    # def setOneWordSeries(self, cleanedDataIn):
    #     for idxTopLevel in cleanedDataIn:
    #         for idx in range(0, len(idxTopLevel)):
    #             if idxTopLevel[idx] in self._oneWordSeries.index:
    #                 temp = self._oneWordSeries.get(idxTopLevel[idx]) + 1
    #                 self._oneWordSeries.update(pd.Series(
    #                     temp, index=[idxTopLevel[idx]]))
    #             elif idxTopLevel[idx] not in self._oneWordSeries.index:
    #                 self._oneWordSeries = self._oneWordSeries.append(
    #                     pd.Series(1, index=[idxTopLevel[idx]]))
    #             else:
    #                 print('Value not recognized')
    #     self._oneWordSeries = self._oneWordSeries.sort_values(
    #         ascending=False, kind='mergesort')
    #
    # def setTwoWordSeries(self, cleanedData):
    #     for idxTopLevel in cleanedData:
    #         for idx in range(0, len(idxTopLevel)-1):
    #             tempStr = idxTopLevel[idx] + ' ' + idxTopLevel[idx + 1]
    #             if tempStr in self._twoWordSeries.index:
    #                 temp = self._twoWordSeries.get(tempStr) + 1
    #                 self._twoWordSeries.update(pd.Series(
    #                     temp, index=[tempStr]))
    #             elif tempStr not in self._twoWordSeries.index:
    #                 self._twoWordSeries = self._twoWordSeries.append(
    #                     pd.Series(1, index=[tempStr]))
    #             else:
    #                 print('Value not recognized')
    #     self._twoWordSeries = self._twoWordSeries.sort_values(
    #         ascending=False, kind='mergesort')
    #
    # def setThreeWordSeries(self, cleanedData):
    #     for idxTopLevel in cleanedData:
    #         for idx in range(0, len(idxTopLevel)-2):
    #             tempStr = idxTopLevel[idx] + ' ' + idxTopLevel[idx + 1] + ' '\
    #                       + idxTopLevel[idx + 2]
    #             if tempStr in self._threeWordSeries.index:
    #                 temp = self._threeWordSeries.get(tempStr) + 1
    #                 self._threeWordSeries.update(pd.Series(
    #                     temp, index=[tempStr]))
    #             elif tempStr not in self._threeWordSeries.index:
    #                 self._threeWordSeries = self._threeWordSeries.append(
    #                     pd.Series(1, index=[tempStr]))
    #             else:
    #                 print('Value not recognized')
    #     self._threeWordSeries = self._threeWordSeries.sort_values(
    #         ascending=False, kind='mergesort')
    #
    # def getOneWordSeries(self):
    #     return self._oneWordSeries
    #
    # def getTwoWordSeries(self):
    #     return self._twoWordSeries
    #
    # def getThreeWordSeries(self):
    #     return self._threeWordSeries

    def getWordCountSeries(self):
        return self._wordCountSeries


def processData(cleanedDataIn, phraseLengthIn):
    var = ProcessData()
    # var.setOneWordSeries(cleanedData)
    # var.setTwoWordSeries(cleanedData)
    # var.setThreeWordSeries(cleanedData)
    var.setWordCountSeries(cleanedDataIn,phraseLengthIn)
    return var.getWordCountSeries()
#    return var.getOneWordSeries(), var.getTwoWordSeries(), var.getThreeWordSeries()