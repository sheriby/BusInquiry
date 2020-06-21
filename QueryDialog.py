import Ui_QueryDialog
import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *

from BackgroundDialog import BackgroundDialog

class QueryDialog(BackgroundDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.ui = Ui_QueryDialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('查询线路')


    # def setBackgroundImg(self):
    #     palette = QPalette()
    #     img = QImage('BusInquiry/img/timg.jpeg')
    #     bg = img.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio)
    #     palette.setBrush(QPalette.Window, QBrush(bg))
    #     self.setPalette(palette)

    def showInfo(self, num: int, content: str):
        self.ui.label.setText('线路 %d' % num)
        self.ui.plainTextEdit.setPlainText(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = QueryDialog()
    dialog.show()

    sys.exit(app.exec_())
