from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class BackgroundDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        self.setBackgroundImg()

    def setBackgroundImg(self):
        palette = QPalette()
        img = QImage('BusInquiry/img/timg.jpeg')
        bg = img.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio)
        palette.setBrush(QPalette.Window, QBrush(bg))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = BackgroundDialog()
    dialog.show()

    sys.exit(app.exec_())
