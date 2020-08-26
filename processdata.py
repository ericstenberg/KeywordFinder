# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0
#
#
# processdata.py inputs the raw keywords list and outputs word and phrase
# counts pandas series.
#
# Sample directory:
# C:\Users\ericd\Documents\Job\Descriptions\Quality Engineer (Hardware)


import pandas as pd


class ProcessData:
    def __init__(self):
        self._oneWordSeries = pd.Series([])
        self._twoWordSeries = pd.Series([])
        self._threeWordSeries = pd.Series([])

    def setOneWordSeries(self, cleanedData):
        for idxTopLevel in cleanedData:
            for idxBottomLevel in idxTopLevel:
                if idxBottomLevel in self._oneWordSeries.index:
                    temp = self._oneWordSeries.get(idxBottomLevel) + 1
                    self._oneWordSeries.update(pd.Series(
                        temp, index=[idxBottomLevel]))
                elif idxBottomLevel not in self._oneWordSeries.index:
                    self._oneWordSeries = self._oneWordSeries.append(
                        pd.Series(1, index=[idxBottomLevel]))
                else:
                    print('Value not recognized')
#        self._oneWordSeries.sort_values() # ascending=False, kind='mergesort'

    def setTwoWordSeries(self, cleanedData):
        for idxTopLevel in cleanedData:
            for idxBottomLevel in idxTopLevel:
                if idxBottomLevel in self._twoWordSeries.index:
                    temp = self._twoWordSeries.get(idxBottomLevel) + 1
                    self._twoWordSeries.update(pd.Series(
                        temp, index=[idxBottomLevel]))
                elif idxBottomLevel not in self._twoWordSeries.index:
                    self._twoWordSeries = self._twoWordSeries.append(
                        pd.Series(1, index=[idxBottomLevel]))
                else:
                    print('Value not recognized')

    def setThreeWordSeries(self, cleanedData):
        for idxTopLevel in cleanedData:
            for idxBottomLevel in idxTopLevel:
                if idxBottomLevel in self._threeWordSeries.index:
                    temp = self._threeWordSeries.get(idxBottomLevel) + 1
                    self._threeWordSeries.update(pd.Series(
                        temp, index=[idxBottomLevel]))
                elif idxBottomLevel not in self._threeWordSeries.index:
                    self._threeWordSeries = self._threeWordSeries.append(
                        pd.Series(1, index=[idxBottomLevel]))
                else:
                    print('Value not recognized')

    def getOneWordSeries(self):
        return self._oneWordSeries

    def getTwoWordSeries(self):
        return self._twoWordSeries

    def getThreeWordSeries(self):
        return self._threeWordSeries


def processData(cleanedData):
    var = ProcessData()
    var.setOneWordSeries(cleanedData)
    var.setTwoWordSeries(cleanedData)
    var.setThreeWordSeries(cleanedData)
    return var.getOneWordSeries(), var.getTwoWordSeries(), var.getThreeWordSeries()