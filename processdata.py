# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0

import pandas as pd


class ProcessData:
    def __init__(self):
        self._oneWordSeries = pd.DataFrame([], dtype='string')
        self._twoWordSeries = pd.DataFrame([], dtype='string')
        self._threeWordSeries = pd.DataFrame([], dtype='string')

    def setOneWordSeries(self,someInputIn):
        pass
        for idxTopLevel in range(0, len(someInputIn)):
            for idxBottomLevel in range(0, len(idxTopLevel)):
                if idxBottomLevel in self._oneWordSeries.index:
                    pass # increment word count up 1
                elif idxBottomLevel not in self._oneWordSeries.index:
                    self._oneWordSeries = self._oneWordSeries.append(pd.Series(1, index=[idxBottomLevel]))
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