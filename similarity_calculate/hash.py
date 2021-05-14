import cv2
import numpy as np


def get_img_gray(filename, shape=(8, 8)):
    img = cv2.imread(filename)
    img = cv2.resize(img, shape)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 计算汉明距离
def hamming_distance(hash1, hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num


# 输入灰度图，返回hash
def get_aHash(image):
    average = np.mean(image)  # 计算像素平均值
    aHash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > average:
                aHash.append(1)
            else:
                aHash.append(0)
    return aHash


def average_hash(img1, img2):
    shape = (8, 8)
    gray1 = get_img_gray(img1, shape)
    gray2 = get_img_gray(img2, shape)

    # 获取哈希
    hash1 = get_aHash(gray1)
    hash2 = get_aHash(gray2)

    ham_distance = hamming_distance(hash1, hash2)

    return ham_distance


def get_pHash(gray):
    dct_low = cv2.dct(np.float32(gray))[0:8, 0:8]
    return get_aHash(dct_low)


def perceptual_hash(img1, img2):
    shape = (32, 32)
    gray1 = get_img_gray(img1, shape)
    gray2 = get_img_gray(img2, shape)

    hash1 = get_pHash(gray1)
    hash2 = get_pHash(gray2)

    ham_dis = hamming_distance(hash1, hash2)
    return ham_dis


def get_dHash(gray):
    d_hash = []
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j+1]:
                d_hash.append(1)
            else:
                d_hash.append(0)
    return d_hash


def difference_hash(img1, img2):
    shape = (9, 8)
    gray1 = get_img_gray(img1, shape)
    gray2 = get_img_gray(img2, shape)

    hash1 = get_dHash(gray1)
    hash2 = get_dHash(gray2)

    ham_dis = hamming_distance(hash1, hash2)
    return ham_dis

def get_hash(file1, file2, file3):
    a_hash1 = average_hash(file1, file2)
    a_hash2 = average_hash(file1, file3)
    a_hash3 = average_hash(file2, file3)
    print('平均哈希 %s %s %s' % (a_hash1, a_hash2, a_hash3))
    p_hash1 = perceptual_hash(file1, file2)
    p_hash2 = perceptual_hash(file1, file3)
    p_hash3 = perceptual_hash(file2, file3)
    print('感知哈希 %s %s %s' % (p_hash1, p_hash2, p_hash3))
    d_hash1 = difference_hash(file1, file2)
    d_hash2 = difference_hash(file1, file3)
    d_hash3 = difference_hash(file2, file3)
    print('比较哈希 %s %s %s' % (d_hash1, d_hash2, d_hash3))
