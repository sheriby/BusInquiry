import Ui_SelectDialog
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from BackgroundDialog import BackgroundDialog


class SelectDialog(BackgroundDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.ui = Ui_SelectDialog.Ui_Dialog()
        self.ui.setupUi(self)

    # def setBackgroundImg(self):
    #     palette = QPalette()
    #     img = QImage('BusInquiry/img/timg.jpeg')
    #     bg = img.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio)
    #     palette.setBrush(QPalette.Window, QBrush(bg))
    #     self.setPalette(palette)

    def setFromAndTo(self, start: str, end: str):
        self.ui.lbFrom.setText(start)
        self.ui.lbTo.setText(end)

    def setMinBusDis(self, minBus: str, minDis: str):
        self.ui.lbMinBus.setText(minBus)
        self.ui.lbMinDistance.setText(minDis)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = SelectDialog()
    dialog.show()
    print(dialog.displayAStop([4]))

    sys.exit(app.exec_())
