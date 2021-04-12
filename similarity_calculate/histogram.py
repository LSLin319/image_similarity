import cv2
import numpy
from matplotlib import pyplot


def paint_and_judge(img_obj1, img_obj2, channel):
    hist1 = cv2.calcHist([img_obj1], [channel], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([img_obj2], [channel], None, [256], [0.0, 255.0])
    pyplot.plot(range(256), hist1, 'r')
    pyplot.plot(range(256), hist2, 'b')
    # pyplot.show()
    match1 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    match2 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    match3 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
    print("巴氏距离：%s, 相关性：%s, 卡方：%s" % (match1, match2, match3))


def histogram_RGB(img1, img2):
    img_obj1 = cv2.imread(img1)
    img_obj2 = cv2.imread(img2)
    paint_and_judge(img_obj1, img_obj2, 0)
    paint_and_judge(img_obj1, img_obj2, 1)
    paint_and_judge(img_obj1, img_obj2, 2)
    cv2.waitKey(0)


def histogram_gray(img1, img2):
    img_obj1 = cv2.imread(img1)
    img_obj2 = cv2.imread(img2)
    gray1 = cv2.cvtColor(img_obj1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_obj2, cv2.COLOR_BGR2GRAY)
    paint_and_judge(gray1, gray2, 0)


if __name__ == '__main__':
    # histogram_RGB('D:/LSL/my_blind_watermark/test/images/lena.png',
    #               'D:/LSL/my_blind_watermark/test/outputs/embedded.png')
    histogram_gray('D:/LSL/my_blind_watermark/test/images/lena.png',
                   'D:/LSL/my_blind_watermark/test/outputs/embedded.png')
