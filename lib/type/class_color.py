# -*- coding: utf-8 -*-
"""

"""

class Colors():
    """
    色情報のクラス。
    
    パラメータ
    ----------
    mode : str
    
    メソッド
    ----------
    set_color : 色情報を設定する
    
    """
    def __init__(self):
        self.mode = "RGB"
    
    def set_color(self,color=None,mode="RGB"):
        self.mode = mode
        self.color = color
    
    def get(self):
        return self.color