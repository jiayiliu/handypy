"""
Handy CV2
=========

"""
import cv2 as _cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def putText(image: np.ndarray, text: str,
            org=(0, 0),
            font=_cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(0, 0, 255),
            thickness=1,
            lineType=_cv2.LINE_AA,
            bottomLeftOrigin=False):
    return _cv2.putText(image, text, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin)


def putChineseText(image: np.ndarray, text: str,
                   org=(0, 0),
                   font=None,
                   fontScale=1, color=(0, 0, 255),
                   thickness=1,
                   lineType=None,
                   bottomLeftOrigin=False):
    grey_flag = len(image.shape) == 2
    if grey_flag:
        image = _cv2.cvtColor(image, _cv2.COLOR_GRAY2BGR)

    if bottomLeftOrigin:
        org = list(org)
        org[1] = image.shape[1] - org[1]

    fontScale = int(fontScale*12)

    if thickness!=1:
        print("Use fontScale to control thickness.")
    if lineType is not None:
        print("Use font to control style.")

    try:
        if font is None:
            try:
                import importlib.resources as pkg_resources
            except ImportError:
                # Try backported to PY<37 `importlib_resources`.
                import importlib_resources as pkg_resources
            from . import resources
            with pkg_resources.path(resources, 'NotoSansCJK-Bold.ttc') as p:
                font = ImageFont.truetype(str(p), fontScale)
        else:
            font = ImageFont.truetype(font, fontScale)
    except OSError:
        print("Download missing font %s" % font)
        raise

    img_PIL = Image.fromarray(image)
    draw = ImageDraw.Draw(img_PIL)
    draw.text(org, text, font=font, fill=color[::-1], )
    image = np.asarray(img_PIL)
    if grey_flag:
        image = _cv2.cvtColor(image, _cv2.COLOR_BGR2GRAY)
    return image
