from model.log import Log
import os
import re


class UnlockSheet:
    def __init__(self, pathZip):
        self.pathZip = pathZip
        self.sheetsPath = []

        self.searchSheetPath()

    def unlock(self):

        for path in self.sheetsPath:
            data = ""
            Log().writteLog("Read xl/worksheets/" + path)
            with open("TempExtract/xl/worksheets/" + path, "r") as sheet:
                data = self.searchSheetProtection(sheet.read(), path)
            if data != 0:
                with open("TempExtract/xl/worksheets/" + path, "w") as test:
                    test.write(data)
        Log().writteLog("Unlock Sheet Finish")

    def searchSheetPath(self):
        try:
            pathSheets = []
            for path in os.listdir("TempExtract/xl/worksheets"):
                if re.search(".xml", path):
                    pathSheets.append(path)
            pathSheets.sort()
            self.sheetsPath = pathSheets
            Log().writteLog("Sheet Found")
            return len(self.sheetsPath) > 0
        except FileNotFoundError:
            Log().writteLog("Error Sheet Not Found", 1)
            return False

    def searchSheetProtection(self, str, path):
        try:
            s = str.index("<sheetProtection")

            cmp = 1

            for c in str[s:]:
                if c != ">":
                    cmp += 1
                else:
                    Log().writteLog("Protection found")
                    return self.rewriteSheet(str, [s, s + cmp], path)

        except ValueError:
            Log().writteLog("Protection not found")
            return False

    def rewriteSheet(self, str, ind, path):
        Log().writteLog("Rewritte Sheet File in " + path)
        r = ""
        for i in range(len(str)):
            if i < ind[0] or i > ind[1] - 1:
                r += str[i]
        return r
