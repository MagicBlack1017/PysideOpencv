import cv2 as cv
import imutils
import numpy as np

from imutils import contours
from imutils.perspective import four_point_transform

# 引入模板
digits = {}
for i in range(0, 8):
    digits[i] = imutils.resize(cv.imread('./template/{}.png'.format(i + 1)), height=300, width=200)
    digits[i] = cv.cvtColor(digits[i], cv.COLOR_BGR2GRAY)
    ref, digits[i] = cv.threshold(digits[i], 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)


def openCV_main(img):
    gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)

    # 高斯滤波？
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # Canny边缘检测
    edged = cv.Canny(blurred, 50, 200, 255)

    # 在边缘映射中查找轮廓，然后按照它们的大小降序排序
    cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,
                           cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv.contourArea, reverse=True)

    displayCnt = None
    # 遍历轮廓
    for c in cnts:
        # 近似轮廓
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.02 * peri, True)
        # 如果轮廓有四个顶点，那么我们已经找到了需要的区域
        if len(approx) == 4:
            displayCnt = approx
            break

    # 提取需要的区域，对其应用透视变换
    warped = four_point_transform(gray, displayCnt.reshape(4, 2))
    output = four_point_transform(img, displayCnt.reshape(4, 2))

    # 对变换后的图像进行阈值处理，然后应用一系列形态学操作来清理阈值化后的图像
    thresh = cv.threshold(warped, 0, 255,
                          cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (1, 5))
    thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)

    # 设定裁剪比例，比如裁剪掉10%的边缘
    crop_percent = 0.08

    # 计算裁剪的像素值
    y, x = thresh.shape[:2]
    x_crop = int(x * crop_percent)
    y_crop = int(y * crop_percent)

    # 裁剪图像, 获取无边框图像
    no_border = thresh[y_crop:y - y_crop, x_crop:x - x_crop]

    # 调整模板大小与裁切区域大小，使得高度匹配
    no_border = imutils.resize(no_border, height=300, width=200)
    # template = imutils.resize(template, height=no_border.shape[0])

    res = ''
    scores = []
    for j in range(8):
        result = cv.matchTemplate(no_border, digits[j], cv.TM_CCOEFF)  # result为一个输出矩阵
        (_, score, _, _) = cv.minMaxLoc(result)  # 这个方法会返回最小值，最大值，最小值位置和最大值位置
        scores.append(score)
    res = res + str(np.argmax(scores) + 1)
    return res


def openCV_image(imagePath):
    try:
        # 调整大小，宽高比是固定的，仅图片调整
        img = cv.imread(imagePath)
        img = imutils.resize(img, height=500)
        message = "结果为： " + openCV_main(img)
    except:
        message = '错误, 没有上传图片'

    return message


# 在主函数内看摄像头， 模块仅处理
def openCV_video(frame):
    img = frame
    try:
        return "结果为： " + openCV_main(img)
    except:
        print('err')
        return '错误， 没有目标'

# 测试代码
# if __name__ == "__main__":
# openCV_video('0')
