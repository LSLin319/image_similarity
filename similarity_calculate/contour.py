import cv2


def contour_detection(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img, 128, 256)
    return canny


def contour_similarity(file1, file2):
    contour1 = contour_detection(file1)
    contour2 = contour_detection(file2)
    return cv2.matchShapes(contour1, contour2, 1, 0.0)

