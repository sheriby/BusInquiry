#! /usr/bin/python3

import sys
import redis
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Ui_MainWindow

from BusManager import BusManager
from QueryDialog import QueryDialog
from AddDialog import AddDialog
from SelectDialog import SelectDialog
from ManageLoginDialog import ManageLoginDialog
from ManageDialog import ManageDialog


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.busManager = BusManager()

        self.initUI()
        self.bindActions()
        self.bindSignalSlots()
        self.hasLogined = False

    def initUI(self):
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('公交查询系统')

        self.resize(1600, 900)
        self.center()
        self.setAutoFillBackground(True)
        self.setBackgroundImg()

    def setBackgroundImg(self):
        palette = QPalette()
        img = QImage('BusInquiry/img/bus.jpg')
        bg = img.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio)
        palette.setBrush(QPalette.Window, QBrush(bg))
        self.setPalette(palette)

    def paintEvent(self, a0):
        pass

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        win = self.geometry()
        left = (screen.width() - win.width()) >> 1
        top = (screen.height() - win.height()) >> 1
        self.move(left, top)

    def bindActions(self):
        self.ui.actionAbout.triggered.connect(self.onActionAboutTriggered)
        self.ui.actionHelp.triggered.connect(self.onActionHelpTriggered)

        # self.ui.actionAdd.triggered.connect(self.onClicked_btnAdd)
        # self.ui.actionDel.triggered.connect(self.onClicked_btnDel)
        self.ui.actionManage.triggered.connect(self.onClicked_btnManage)
        self.ui.actionQuery.triggered.connect(self.onClicked_btnQuery)

    def bindSignalSlots(self):
        # self.ui.btnAdd.clicked.connect(self.onClicked_btnAdd)
        # self.ui.btnDel.clicked.connect(self.onClicked_btnDel)
        self.ui.btnQuery.clicked.connect(self.onClicked_btnQuery)
        self.ui.btnManage.clicked.connect(self.onClicked_btnManage)
        self.ui.btnSelect.clicked.connect(self.onClicked_btnSelect)
        self.ui.btnJsonOut.clicked.connect(self.onClicked_btnJsonOut)

    def openQueryDialog(self, num: int, content: str):
        queryDialog = QueryDialog()
        queryDialog.showInfo(num, content)
        queryDialog.show()
        queryDialog.exec()

    def onActionAboutTriggered(self):
        QMessageBox.about(
            self, 'About', 'This program is written by using lib PyQt5, and the author is sheriby.')

    def onActionHelpTriggered(self):
        QMessageBox.question(
            self, 'Help', 'If having questions about this program or needing help, please contact me. My email is hony_sher@foxmail.com',
            QMessageBox.Ok)

    def onClicked_btnManage(self):
        if self.hasLogined == True:
            self.loginSuccess()
        else:
            manageLoginDialog = ManageLoginDialog()
            manageLoginDialog.setWindowModality(Qt.ApplicationModal)
            manageLoginDialog.signal_LoginSuccess.connect(self.on_LoginSuccess)
            manageLoginDialog.show()
            manageLoginDialog.exec()

    def loginSuccess(self):
        manageDialog = ManageDialog()
        manageDialog.setWindowModality(Qt.ApplicationModal)
        manageDialog.ui.btnAdd.clicked.connect(self.onClicked_btnAdd)
        manageDialog.ui.btnDel.clicked.connect(self.onClicked_btnDel)
        manageDialog.ui.btnWrite.clicked.connect(self.onClicked_btnWrite)
        manageDialog.show()
        manageDialog.exec()

    def on_LoginSuccess(self):
        self.sender().close()
        self.hasLogined = True
        self.loginSuccess()

    def onClicked_btnAdd(self):
        addDialog = AddDialog()
        addDialog.ui.pushButton.clicked.connect(
            lambda: self.getAddData(addDialog))
        addDialog.ui.btnJson.clicked.connect(
            lambda: self.onClicked_btnJson(addDialog))
        addDialog.setWindowModality(Qt.ApplicationModal)
        addDialog.show()
        addDialog.exec()

    def getAddData(self, dialog):
        num = dialog.ui.leNumber.text()
        strRoute = dialog.ui.leRoute.text()
        strDistance = dialog.ui.leDistance.text()
        dialog.close()

        route = strRoute.split(';')
        if len(route) == 1:
            route = strRoute.split('；')
        distance = strDistance.split(';')
        if len(distance) == 1:
            distance = strDistance.split('；')
        distance = list(map(lambda x: int(x), distance))
        self.busManager.addBusRoute(int(num), route, distance)

    def onClicked_btnDel(self):
        num, ok = QInputDialog.getInt(self, '删除', '删除线路: ')
        if ok and num:
            res = QMessageBox.question(self, '删除', '你确定要删除线路%d吗' %
                                       num, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if res == QMessageBox.Yes:
                suc = self.busManager.deleteBusRoute(num)
                if suc == False:
                    QMessageBox.critical(self, '错误', '该线路不存在!', QMessageBox.Ok)

    def onClicked_btnQuery(self):
        num, ok = QInputDialog.getInt(self, '查询', '查询线路:')
        if ok and num:
            result = self.busManager.queryBusRoute(num)
            if result is None:
                QMessageBox.critical(self, '错误', '该线路不存在!', QMessageBox.Ok)
                return None

            content = ''
            for res in result[0:-1]:
                content += self.busManager.busId2NameMap[res] + ' => '
            content += self.busManager.busId2NameMap[result[-1]]
            self.openQueryDialog(num, content)

    def onClicked_btnSelect(self):
        start = self.ui.leStart.text()
        end = self.ui.leEnd.text()
        if start not in self.busManager.busName2IdMap or end not in self.busManager.busName2IdMap:
            QMessageBox.critical(self, '错误', '线路不存在，请尝试其他线路', QMessageBox.Ok)
            self.ui.leStart.clear()
            self.ui.leEnd.clear()
            return None
        startId = self.busManager.busName2IdMap[start]
        endId = self.busManager.busName2IdMap[end]
        result = self.busManager.selectBusRoute(startId, endId)
        selectDialog = SelectDialog()
        selectDialog.setFromAndTo(start, end)
        if (len(result[0]) <= 200):
            selectDialog.ui.lbMinBus.setStyleSheet('font: 57 16pt "WenQuanYi Zen Hei Sharp";\
            background-color: rgba(211, 215, 207, 0.85);')
            selectDialog.ui.lbMinDistance.setStyleSheet('font: 57 16pt "WenQuanYi Zen Hei Sharp";\
            background-color: rgba(211, 215, 207, 0.85);')
        selectDialog.setMinBusDis(result[0], result[1])
        selectDialog.setWindowModality(Qt.ApplicationModal)
        selectDialog.show()
        selectDialog.exec()

        self.ui.leStart.clear()
        self.ui.leEnd.clear()

    def onClicked_btnWrite(self):
        self.busManager.writeDataIntoRedis()
        QMessageBox.information(self, '写入成功', '数据库写入成功', QMessageBox.Ok)

    def onClicked_btnJson(self, dialog):
        dialog.close()
        fileName = QFileDialog.getOpenFileName(
            self, '选择一个json文件', './', 'json文件(*.json)')[0]
        self.busManager.loadJson(fileName)
        QMessageBox.information(self, '导入成功', 'json文件导入成功', QMessageBox.Ok)

    def onClicked_btnJsonOut(self):
        fileName = QFileDialog.getSaveFileName(
            self, '选择写入的位置和文件', './', 'json文件(*.json)')[0]
        jsonStr = self.busManager.getAllRouteAndWeightJson()
        with open(fileName, 'w') as f:
            f.write(jsonStr)
        QMessageBox.information(self, '导出成功', 'json文件导出成功', QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwin = MainWin()
    mainwin.show()

    sys.exit(app.exec_())
