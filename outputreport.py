# Author: Eric Stenberg
# License: GNU Affero General Public License v3.0
#from os import path
import os


class OutputReport:
    def __init__(self):
        pass

    def setDir(self):
        # does output directory exist in pwd?
        # if not, create dir named "output"
        outputDir = os.getcwd() + r'''\output'''
        if os.path.isdir(outputDir):
            print(outputDir + ' exists.')
        else:
            print(outputDir + ' does not exist. Creating new output directory.')
            os.mkdir(outputDir)

    def generateCSV(self):
        pass

    def generateJSON(self):
        pass

    def generateTXT(self):
        pass

    def generateSQL(self):
        pass


def outputReport():
    var = OutputReport()
    var.setDir()
    # output CSV
    # output JSON
    # output TXT
    # output SQL