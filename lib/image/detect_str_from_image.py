# -*- coding: utf-8 -*-
"""

"""

from PIL import Image
import pyocr

class detect_str_from_image():
    """
    画像から文字列を検出するクラス。
    
    パラメータ
    ----------
    なし
    
    メソッド
    ----------
    detect_str_from_image_using_OCR : OCRエンジンで文字検出
    
    """
    def __init__(self):
        pass
    
    def detect_str_from_image_using_OCR(self,file=None,lang="eng"):
        """
        OCRエンジンで文字検出
    
        パラメータ
        ----------
        file : str
            検出する対象の画像。
            絶対参照パスでのファイル指定推奨。
        
        lang : str
            検出する言語。
            デフォルトは "eng"(英語)。
    
        返り値
        -------
        text : str
            検出された文字列。
        
    
        """
        # OCRエンジンを取得
        engine = pyocr.get_available_tools()[0]
        
        # 画像の文字を読み込む
        return engine.image_to_string(Image.open(file), lang=lang)