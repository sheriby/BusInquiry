import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from BackgroundDialog import BackgroundDialog
import Ui_ManageDialog


class ManageDialog(BackgroundDialog):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.ui = Ui_ManageDialog.Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = ManageDialog()
    dialog.show()

    sys.exit(app.exec_())
