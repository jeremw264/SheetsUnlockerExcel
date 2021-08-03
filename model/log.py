from datetime import datetime

class Log:
    def __init__(self) -> None:

        self.path = "log/log.txt"

    def writteLog(self, str, level=0):

        now = datetime.now()

        if level == 1:
            levelMsg = "[Warning] "
        elif level == 2:
            levelMsg = "[Error] "
        else:
            levelMsg = ""

        with open(self.path, "a") as log:
            log.write(now.strftime("[%d/%m/%Y|%H:%M:%S] ") + levelMsg + str + "\n")
        print(str)
