import cv2 as cv


def remove_watermark(origin, watermark=""):
    if watermark:
        # 目标修复图像;
        src_ = cv.imread(origin)
        # 蒙版图（定位修复区域）;
        mask = cv.imread(watermark, cv.IMREAD_GRAYSCALE)
        res_ = cv.resize(src_, None, fx=0.6, fy=0.6, interpolation=cv.INTER_CUBIC)
        mask = cv.resize(mask, None, fx=0.6, fy=0.6, interpolation=cv.INTER_CUBIC)
        # 修复算法(INPAINT_TELEA：基于快速行进算法 算法效果较好
        #         INPAINT_NS:基于流体动力学并使用了偏微分方程)
        # 3=>选取邻域半径;
        dst = cv.inpaint(res_, mask, 3, cv.INPAINT_TELEA)

        cv.imshow('res_', res_)
        cv.imshow('mask', mask)
        cv.imshow('dst', dst)
        cv.waitKey(0)
        cv.destroyAllWindows()
        return dst


def add_watermark():
    pass