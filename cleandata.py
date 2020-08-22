# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0

import string as s
import pandas as pd
import unicodedata

class CleanData:
    def __init__(self):
        self._cleanSeries = pd.Series([], dtype='string')

    def setCleanSeries(self, rawKeywordsList):
    # remove hyperlinks
        #exclude = s.punctuation

        for idx in range(0, len(rawKeywordsList)):
            rawKeywordsList[idx] = rawKeywordsList[idx].replace(unicode.translate(s.punctuation), ' ')
            rawKeywordsList[idx] = rawKeywordsList[idx].replace(unicode.translate(s.whitespace), ' ')
            rawKeywordsList[idx] = rawKeywordsList[idx].lower()
            print(rawKeywordsList[idx])


#        ['' if ]
 #       for item in rawKeywordsSeries:
  #          self._cleanSeries = self._cleanSeries.append(pd.Series(
   #             item.lower(), dtype='string'))

    def getCleanSeries(self):
        return self._cleanSeries

    def setKeywordCountSeries(self):
        pass

    def getKeywordCountSeries(self):
        pass

def cleanData(rawKeywordsList):
    var = CleanData()
    var.setCleanSeries(rawKeywordsList)
#    print(var.getCleanSeries())
#    return var.getCleanSeries()