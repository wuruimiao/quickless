import cv2 as cv
import matplotlib.pyplot as plt

# cap = cv.VideoCapture('./buyu.mp4')
# while True:
#     ret, frame = cap.read()
#     cv.imshow("capture", frame)
#     if cv.waitKey(100) & 0xFF == ord('q'):
#         break
#
#
# cap.release()
# cv.destroyAllWindows()


import numpy as np

img0 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
# plb.imshow(img0, cmap="gray")
# plt.show()

# cap = cv.VideoCapture('./buyu.mp4')
# ret, frame = cap.read()
# cv.imwrite("buyu.png", frame)
# cap.release()

frame = cv.imread("../../images/buyu.png")

# plt.imshow(frame, cmap='gray')
# plt.imshow(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
# plt.show()

# roi = frame[100:200, 300:400] # ROI
# plt.imshow(cv.cvtColor(roi, cv.COLOR_BGR2RGB))
# plt.show()

# plt.imshow(cv.cvtColor(frame, cv.COLOR_BGR2GRAY), cmap='gray')
# plt.show()

# plt.imshow(cv.cvtColor(frame, cv.COLOR_BGR2HSV), cmap='hsv') # 肤色检测
# plt.show()

# _, _frame = cv.threshold(frame, 128, 256, cv.THRESH_BINARY)
# plt.imshow(_frame[:, :, 1], cmap='gray')
# plt.show()

# plt.imshow(cv.resize(frame, (500, 300)))
# plt.show()

# 移动
# [1 0 tx]  点乘 [x]  =  [x+tx]       (x,y)像素坐标，移动到(tx, ty)
# [0 1 ty]      [y]     [y+ty]
#               [1]
# m = np.float32([[1, 0, 300], [0, 1, 200]])
# plt.imshow(cv.warpAffine(frame, m, (2000, 2000)))
# plt.show()


# 缩放
# m = np.float32([[1, 0, 0], [0, 1, 0]]) # 原图
# m = np.float32([[2, 0, 0], [0, 10, 0]])
# plt.imshow(cv.warpAffine(frame, m, (2000, 2000)))
# plt.show()

# 旋转
# [cos -sin 0] 点乘 [x] = [xcos-ysin]
# [sin cos 0]      [y]   [xsin+ycos]
#                  [1]
theta = 0.5
# m = np.float32([[np.cos(theta), -np.sin(theta), 100],
# #                 [np.sin(theta), np.cos(theta), 200]])
m = np.float32([[np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0]])
# plt.imshow(cv.warpAffine(frame, m, (2000, 2000)))
# plt.show()

# 斜切=拉伸变换+透视变换
m = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
m1 = np.float32([[0, 0], [100, 0], [0, 300], [300, 300]])
M = cv.getPerspectiveTransform(m, m1)
# plt.imshow(cv.warpPerspective(frame, M, (2000, 2000)))
# plt.show()

# 模糊
# plt.imshow(cv.GaussianBlur(frame, (49, 49), 1, 0))
# plt.show()

# 锐化，求梯度的过程
# plt.imshow(cv.Canny(frame, 30, 150))
# plt.show()
# kernal = np.ones((3,3), np.float32) / 8
# kernal = - kernal
# kernal[0, :] = [-1, -1, -1]
# kernal[1, :] = [0, 0, 0]
# kernal[2, :] = [1, 1, 1]
# plt.imshow(cv.filter2D(frame, -1, kernal))
# plt.show()


# 水印
wm = cv.imread("../../images/water.png")
wrm = cv.resize(wm, (300, 300))
wm = 255 - wm
print(wm.shape)
img1 = cv.resize(frame, (300, 300))
plt.imshow(cv.add(wm, img1))
# plt.imshow(cv.addWeighted(wm, 0.9, img1, 1, 0))
plt.show()
