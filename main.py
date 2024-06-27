import sys
import cv2 as cv

from PySide6 import QtCore, QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from PySide6.QtCore import QFile
from mainWindow import Ui_mainWindow  # UI文件
from openCV import openCV_image, openCV_video


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        # 初始化
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # 定时器
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Camera_video)
        # 摄像头
        self.cap_video = 0
        # 记录定时器工作状态
        self.flag = 0
        # 存放每一帧读取的图像
        self.img = []
        # 数据检查
        # self.temData = 0
        # self.dataCheck = []

        # 添加控件对象并连接信号槽
        self.toolButton = self.ui.toolButton
        self.toolButton.clicked.connect(self.Select_a_single_file)
        self.toolButton2 = self.ui.toolButton_2
        self.toolButton2.clicked.connect(self.Select_Camera_path)
        self.pushButton = self.ui.pushButton
        self.pushButton.clicked.connect(self.Image_process)
        self.pushButton2 = self.ui.pushButton_2
        self.pushButton2.clicked.connect(self.Camera_process)
        self.comboBox = self.ui.comboBox
        self.comboBox2 = self.ui.comboBox_2
        self.texBrowser = self.ui.textBrowser
        self.label = self.ui.label_2
        self.file_path = None  # 初始化 file_path 属性
        self.camera_path = None  # 初始化 camera_path 属性

    def Select_a_single_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                        "Text Files(*.jpg);; Text Files(*.png);; Text Files("
                                                        "*.jpeg)")
        if self.file_path:
            self.comboBox.clear()
            self.comboBox.addItem(self.file_path)

        self.file_path = self.comboBox.currentText()
        pixMap = QPixmap(self.file_path)
        self.label.setScaledContents(True)
        self.label.setPixmap(pixMap)

    def Select_Camera_path(self):
        self.camera_path = QInputDialog.getText(self, "输入相机路径", "相机路径：")

        if self.camera_path[1]:
            self.comboBox2.clear()
            self.comboBox2.addItem(self.camera_path[0])

        self.camera_path = self.comboBox2.currentText()

    def Image_process(self):
        # 调用openCV_image函数
        self.texBrowser.setText(openCV_image(self.file_path) + '\n')

    def Camera_process(self):
        self.texBrowser.clear()

        if self.flag == 0:
            if self.camera_path is None or type(self.camera_path) != type(1):  # 相机路径异常处理
                try:
                    int(self.camera_path)  # 看能不能转成整形
                except:
                    self.texBrowser.setText("相机路径未填写或填写错误")

            self.cap_video = cv.VideoCapture(int(self.camera_path))
            self.timer.start(50)
            self.flag += 1
            # openCV_image(img)
            self.pushButton2.setText("关闭摄像头")

        else:
            self.timer.stop()
            self.cap_video.release()
            self.label.clear()
            self.pushButton2.setText("视频检测")
            self.flag = 0

    def Camera_cv_img(self, img):
        shrink = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        QtImg = QtGui.QImage(shrink.data,
                             shrink.shape[1],
                             shrink.shape[0],
                             shrink.shape[1] * 3,
                             QtGui.QImage.Format.Format_RGB888)
        jpg_out = QtGui.QPixmap(QtImg).scaled(
            self.label.width(), self.label.height())

        self.label.setPixmap(jpg_out)

    # 视频检测在这处理
    def Camera_video(self):
        ret, self.img = self.cap_video.read()
        if ret:
            self.Camera_cv_img(self.img)
            self.texBrowser.setText(openCV_video(self.img))
            # 数据检查， 满足五个相同才输出结果(好像没用。。)
            # self.temData = openCV_video(self.img)
            # if len(self.dataCheck) > 0:
            #     if self.dataCheck[len(self.dataCheck) - 1] == self.temData:
            #         self.dataCheck.append(self.temData)
            #         if len(self.dataCheck) == 5:
            #             temStore = self.dataCheck[0]
            #             self.dataCheck.clear()
            #             self.texBrowser.setText(temStore)
            # elif len(self.dataCheck) == 0:
            #     self.dataCheck.append(self.temData)
            # else:
            #     self.texBrowser.setText('错误， 没有目标')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainWindow()
    window.show()

    sys.exit(app.exec())
