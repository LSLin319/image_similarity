import cv2
import numpy
import matplotlib.pyplot as plt


def paint_and_judge(img_obj1, img_obj2, img_obj3, channel):
    hist1 = cv2.calcHist([img_obj1], [channel], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([img_obj2], [channel], None, [256], [0.0, 255.0])
    hist3 = cv2.calcHist([img_obj3], [channel], None, [256], [0.0, 255.0])
    ln1, = plt.plot(range(256), hist1, 'r')
    ln2, = plt.plot(range(256), hist2, 'b')
    ln3, = plt.plot(range(256), hist3, 'g')
    plt.legend(handles=[ln1, ln2, ln3], labels=['original', 'embedded watermark', 'removed watermark'])
    plt.savefig('pci.png')
    # match1 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    # match2 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    # match3 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
    # print("巴氏距离：%s, 相关性：%s, 卡方：%s" % (match1, match2, match3))


def histogram_RGB(img1, img2):
    img_obj1 = cv2.imread(img1)
    img_obj2 = cv2.imread(img2)
    paint_and_judge(img_obj1, img_obj2, 0)
    paint_and_judge(img_obj1, img_obj2, 1)
    paint_and_judge(img_obj1, img_obj2, 2)
    cv2.waitKey(0)


def histogram_gray(img1, img2, img3):
    img_obj1 = cv2.imread(img1)
    img_obj2 = cv2.imread(img2)
    img_obj3 = cv2.imread(img3)
    gray1 = cv2.cvtColor(img_obj1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_obj2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_obj3, cv2.COLOR_BGR2GRAY)
    paint_and_judge(gray1, gray2, gray3, 0)


if __name__ == '__main__':
    # histogram_RGB('D:/LSL/my_blind_watermark/test/images/lena.png',
    #               'D:/LSL/my_blind_watermark/test/outputs/embedded.png')
    histogram_gray('D:/LSL/my_blind_watermark/test/images/lena.png',
                   'D:/LSL/my_blind_watermark/test/outputs/embedded.png')
