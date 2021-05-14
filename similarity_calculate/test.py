import hash
import histogram
import contour


def test(file1, file2,file3):
    histogram.histogram_gray(file1, file2,file3)
    # a_hash = hash.average_hash(file1, file2)
    # p_hash = hash.perceptual_hash(file1, file2)
    # d_hash = hash.difference_hash(file1, file2)
    # print('平均哈希: %s, 感知哈希: %s, 比较哈希: %s' % (a_hash, p_hash, d_hash))
    # contour.contour_similarity(file1, file2, file3)
    # print('边缘检测: %s' % contour_simi)
    hash.get_hash(file1, file2, file3)


if __name__ == '__main__':
    file1 = 'D:/LSL/watermark/test_imgs/use/13o.png'
    file2 = 'D:/LSL/watermark/test_imgs/use/13wm.png'
    file3 = 'D:/LSL/watermark/test_imgs/use/13r.png'
    print('原图与加水印：')
    # test(file1, file2)
    # print('原图与去水印：')
    # test(file1, file3)
    # print('加水印与去水印：')
    # test(file2, file3)
    test(file1,file2,file3)
