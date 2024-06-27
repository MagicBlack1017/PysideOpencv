import ctypes

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QLabel,
                               QPushButton, QTextBrowser, QToolButton,
                               QWidget)


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(439, 552)
        icon = QIcon()
        icon.addFile(u"./resource/icon.png", QSize(), QIcon.Mode.Normal,
                     QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid") # 设置托盘图标与窗口一致

        self.pushButton_2 = QPushButton(mainWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 340, 91, 31))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton = QPushButton(mainWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 290, 91, 31))
        self.pushButton.setFont(font)
        self.textBrowser = QTextBrowser(mainWindow)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 390, 411, 121))
        self.textBrowser.setFrameShape(QFrame.Shape.StyledPanel)
        self.textBrowser.setFrameShadow(QFrame.Shadow.Plain)
        self.textBrowser.setLineWidth(0)
        self.label_2 = QLabel(mainWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 411, 241))
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_2.setLineWidth(1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(mainWindow)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 300, 271, 21))
        self.label = QLabel(mainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 54, 16))
        self.label_3 = QLabel(mainWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 370, 54, 16))
        self.toolButton = QToolButton(mainWindow)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(290, 301, 24, 21))
        self.label_4 = QLabel(mainWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 280, 81, 16))
        self.comboBox_2 = QComboBox(mainWindow)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(10, 340, 271, 21))
        self.toolButton_2 = QToolButton(mainWindow)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(290, 341, 24, 21))
        self.label_5 = QLabel(mainWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 320, 81, 16))
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.toolButton_2)
        QWidget.setTabOrder(self.toolButton_2, self.textBrowser)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)

    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow",
                                                             u"\u57fa\u4e8eOpenCV\u548cPySide\u7684\u6a21\u677f\u6570"
                                                             u"\u5b57\u8bc6\u522b",
                                                             None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"\u89c6\u9891\u68c0\u6d4b", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u56fe\u7247\u68c0\u6d4b", None))
        self.textBrowser.setHtml(QCoreApplication.translate("mainWindow",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                            u"\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                                            "/><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "hr { height: 1px; border-width: 0; }\n"
                                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                                            "</style></head><body style=\" font-family:'Microsoft "
                                                            "YaHei UI'; font-size:9pt; font-weight:400; "
                                                            "font-style:normal;\">\n"
                                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                            "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                            "-qt-block-indent:0; text-indent:0px;\"><br "
                                                            "/></p></body></html>",
                                                            None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u56fe\u7247/\u89c6\u9891", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u8f93\u51fa", None))
        self.toolButton.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u56fe\u7247\u8def\u5f84\u8bbe\u7f6e", None))
        self.toolButton_2.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.label_5.setText(
            QCoreApplication.translate("mainWindow", u"\u6444\u50cf\u5934\u8def\u5f84\u8bbe\u7f6e", None))
