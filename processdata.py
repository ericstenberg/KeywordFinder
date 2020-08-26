"""
Author: Eric Stenberg
License: GNU Affero General Public License v3.0


processdata.py inputs the raw keywords list and outputs word and phrase counts
pandas series.

Sample directory:
C:\Users\ericd\Documents\Job\Descriptions\Quality Engineer (Hardware)

"""

import pandas as pd


class ProcessData:
    def __init__(self):
        self._oneWordSeries = pd.Series([])
        self._twoWordSeries = pd.Series([])
        self._threeWordSeries = pd.Series([])

    def setOneWordSeries(self,someInputIn):
        for idxTopLevel in someInputIn: # range(0, len(someInputIn)):
            for idxBottomLevel in idxTopLevel: # range(0, len(idxTopLevel)):
                if idxBottomLevel in self._oneWordSeries.index:
                    temp = self._oneWordSeries.get(idxBottomLevel) + 1
                    self._oneWordSeries = self._oneWordSeries.update(
                        pd.Series(temp, index=[idxBottomLevel]))
                elif idxBottomLevel not in self._oneWordSeries.index:
                    self._oneWordSeries = self._oneWordSeries.append(
                        pd.Series(1, index=[idxBottomLevel]))
                else:
                    print('Value not recognized')

    def setTwoWordSeries(self):
        pass

    def setThreeWordSeries(self):
        pass

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