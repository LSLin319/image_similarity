import hash
import histogram
import contour

if __name__ == '__main__':
    file1 = 'D:/LSL/watermark/test_imgs/lena.png'
    file2 = 'D:/LSL/watermark/test_imgs/lena_wm_35.png'
    histogram.histogram_gray(file1, file2)
    a_hash = hash.average_hash(file1, file2)
    p_hash = hash.perceptual_hash(file1, file2)
    d_hash = hash.difference_hash(file1, file2)
    print('平均哈希: %s, 感知哈希: %s, 比较哈希: %s' % (a_hash, p_hash, d_hash))
    contour = contour.contour_similarity(file1, file2)
    print('边缘检测: %s' % contour)
