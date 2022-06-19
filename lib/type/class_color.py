# -*- coding: utf-8 -*-
"""

"""

class Colors():
    """
    色情報のクラス。
    
    パラメータ
    ----------
    mode : str
    color : list
        色情報。
        RGBでは[R,G,B]で指定。
    
    メソッド
    ----------
    set_color : 色情報を設定する
    
    """
    def __init__(self):
        self.mode = "RGB"
    
    def __str__(self):
        return self.color
    
    def set_color(self,color=None,mode="RGB"):
        """
        色情報を設定する
    
        パラメータ
        ----------
        color : list
            色情報。
            RGBでは[R,G,B]で指定。
        
        mode : str
            色情報の形式。
            デフォルトは "RGB"。
    
        返り値
        -------
        None
        
    
        """
        self.mode = mode
        self.color = color
    
    def get(self):
        return self.color