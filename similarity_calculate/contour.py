import cv2


def contour_detection(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img, 128, 256)
    return canny


def contour_similarity(file1, file2, file3):
    contour1 = contour_detection(file1)
    contour2 = contour_detection(file2)
    contour3 = contour_detection(file3)
    cv2.imwrite('1oc.png', contour1)
    cv2.imwrite('1wmc.png', contour2)
    cv2.imwrite('1rc.png', contour3)
    print('原图和加水印：%s' % cv2.matchShapes(contour1, contour2, 1, 0.0))
    print('原图和去水印：%s' % cv2.matchShapes(contour1, contour3, 1, 0.0))
    print('加水印和去水印：%s' % cv2.matchShapes(contour2, contour3, 1, 0.0))
    # return cv2.matchShapes(contour1, contour2, 1, 0.0)
