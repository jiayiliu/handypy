import numpy as np
from handypy import hcv2 as cv2
import pytest


def test_putText():
    img = np.zeros((256, 256, 3), np.uint8)
    cv2.putText(img, "msg")

    img = np.zeros((256, 256), np.uint8)
    cv2.putText(img, "msg")


def test_put_chinese_text():
    img = np.zeros((256, 256, 3), np.uint8)
    cv2.putChineseText(img, "中文", bottomLeftOrigin=True, thickness=2, lineType=0)

    img = np.zeros((256, 256), np.uint8)
    cv2.putChineseText(img, "中文")

    with pytest.raises(OSError):
        cv2.putChineseText(img, "中文", font="unknown")
