import zipfile
import shutil
import os
from model.log import Log
from model.unlockSheet import UnlockSheet

filePath = "filePath"

if __name__ == "__main__":

    Log().writteLog("Launch Program on " + filePath)

    try:
        zipPath = filePath[: len(filePath) - 4] + "zip"
        os.rename(filePath, zipPath)
        zf = zipfile.ZipFile(zipPath)
        nameListOrigin = zf.namelist()
        zf.extractall("TempExtract/")

        Log().writteLog("Extract Finish")

        UnlockSheet(zipPath).unlock()
        with zipfile.ZipFile(zipPath, "w") as myzip:
            for name in nameListOrigin:
                myzip.write("TempExtract/" + name, name)

        Log().writteLog("Rewritte ZIP Finish")

        shutil.rmtree("TempExtract/")
        os.mkdir("TempExtract")
        os.rename(zipPath, filePath)

    except FileNotFoundError:
        Log().writteLog("File " + filePath + " not Found", 2)
