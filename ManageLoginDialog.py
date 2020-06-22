import sys
import redis
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from BackgroundDialog import BackgroundDialog
import Ui_ManageLogin


class ManageLoginDialog(BackgroundDialog):
    signal_LoginSuccess = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.initUi()
        self.bindSignalSlots()
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def initUi(self):
        self.ui = Ui_ManageLogin.Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle('管理员登录')

    def bindSignalSlots(self):
        self.ui.btnLogin.clicked.connect(self.vertifyAccount)

    def vertifyAccount(self):
        account = self.ui.leAccount.text()
        passwd = self.ui.lePasswd.text()
        realPasswd = self.r.get('bus:admin:'+account)

        if realPasswd is None:
            QMessageBox.critical(self, '错误', '用户名或密码错误', QMessageBox.Ok)
            self.ui.lePasswd.clear()
            return

        realPasswd = realPasswd.decode('utf-8')
        if passwd == realPasswd:
            self.signal_LoginSuccess.emit()
        else:
            QMessageBox.critical(self, '错误', '用户名或密码错误', QMessageBox.Ok)
            self.ui.lePasswd.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = ManageLoginDialog()
    dialog.show()

    sys.exit(app.exec_())
