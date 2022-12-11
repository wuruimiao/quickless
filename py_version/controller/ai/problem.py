import cv2 as cv

# 切边，图片周围白边
frame = cv.imread("../../images/qiebian.png")
cv.imshow("1", frame)
cv.waitKey()
# 1、边缘检测+轮廓发现或者直线检测最大外接矩阵
# 测试下不同阈值，拿到的边缘
img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
img = cv.Canny(img, )
contours = cv.findContours()

min_w = frame.cols * 0.75
min_h = frame.rows * 0.75
for point in contours:
    min_rect = cv.minAreaRect(point)
    degree = abs(min_rect.angle)
    if min_rect.size.width > min_w and min_rect.size.height > min_h and min_rect.size.width < (frame.cols - 5):
        min_rect.points()
        color = cv.GScalar()

# 如果图片斜了啥的，需要怎么做？怎么转换成一张斜图？
# 找到最大外接矩形，找到轮廓，
# 2、二值分割+形态学方法+Hough直线 找到最大外接矩阵
