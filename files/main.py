# --------------------------------------------------------------------------------------
# | Py module: main.py                                                                 |
# | Author: David García Rincón                                                        |
# | Date: 20210719                                                                     |
# | Version: 1.0 x64                                                                   |
# | Purpose: free software for testing and developing. Right working is not guarantied |
# --------------------------------------------------------------------------------------
# |                                        description                                 |
# --------------------------------------------------------------------------------------
# | This module is opening the ui form in #1                                           |
# | Generate the proccedure of the button read data in #2 calling the function readDB  |
# | included in module readDB.py mandatory                                             |
# --------------------------------------------------------------------------------------


import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile
import readDB


class mainFormReadDB():
    # 1. Declaration of the mainform and call functions
    def __init__(self):
        super(mainFormReadDB, self).__init__()
        self.ui = QUiLoader().load(QFile("main_window.ui"))
        self.ui.btnRead.clicked.connect(self.read)

    # 2. ReadDB function when click on ReadDB button

    def read(self):
        # 2.0 get data by running readDB function in readDB.py
        readDB.readDB()
        datos = readDB.readDB()
        cpuType = datos[0]
        cpuStatus = datos[1]
        name = datos[2]
        value = datos[3]
        status = datos[4]

        # 2.1 CPU data
        self.ui.txtCpuType.setText("{}".format(cpuType))  

        if cpuStatus == 'S7CpuStatusRun':
            self.ui.ledCpuStatus.setStyleSheet(u"background-color: rgb(0, 255, 0);border-radius:15px;")
        else:
            self.ui.ledCpuStatus.setStyleSheet(u"background-color: rgb(255, 0, 0);border-radius:15px;")

        # 2.2 DB data
        self.ui.txtName.setText("{}".format(name))
        self.ui.lcdValue.setProperty("intValue", value)
        if status == True:
            self.ui.ledStatus.setStyleSheet(
                u"background-color: rgb(0, 255, 0);border-radius:30px;")
        else:
            self.ui.ledStatus.setStyleSheet(
                u"background-color: rgb(255, 0, 0);border-radius:30px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = mainFormReadDB()
    myapp.ui.show()
    sys.exit(app.exec_())
