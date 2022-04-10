# coding=UTF-8
import cv2
import numpy as np

img = cv2.imread('test.png')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

# 写入文件
cv2.imwrite("test-rotated.jpg", dst, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
print('rotated and saved.')