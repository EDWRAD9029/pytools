# -*- coding: utf-8 -*-
"""

"""

from PIL import Image
import pyocr

class detect_str_from_image():
    """
    
    """
    def __init__(self):
        pass
    
    def detect_str_from_image_using_OCR(self,file=None,lang="eng"):
        # OCRエンジンを取得
        engines = pyocr.get_available_tools()
        engine = engines[0]
        
        # 画像の文字を読み込む
        return engine.image_to_string(Image.open(file), lang=lang)