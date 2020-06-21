import Ui_AddDialog
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from BackgroundDialog import BackgroundDialog


class AddDialog(BackgroundDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.ui = Ui_AddDialog.Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle('添加线路')

        self.ui.leNumber.setValidator(QIntValidator(self))

    # def setBackgroundImg(self):
    #     palette = QPalette()
    #     img = QImage('BusInquiry/img/timg.jpeg')
    #     bg = img.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio)
    #     palette.setBrush(QPalette.Window, QBrush(bg))
    #     self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = AddDialog()
    dialog.show()

    sys.exit(app.exec_())
