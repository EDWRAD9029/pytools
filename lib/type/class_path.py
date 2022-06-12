# -*- coding: utf-8 -*-
"""

"""

import sys,os
import numpy as np
import glob

class Paths():
    """
    ファイルディレクトリ名のクラス。
    
    パラメータ
    ----------
    data : list
    
    メソッド
    ----------
    __init__ : ライブラリpytoolのpathを通すための名前空間を読み込む
        
    add : ディレクトリを入力することで、メンバー変数dataに追加する
    
    """
    dir_pytools = None
    data = []
    
    def __init__(self,*args,**kwargs):
        # pathが設定されていない場合は環境構築用の名前空間を読み込む
        self.set_path_pytools()
    
    def set_path_pytools(self):
        tmp = __file__.split("\\")
        s = [i=="pytools" for i in tmp]
        s = np.arange(len(tmp))[s][0]+2
        self.dir_pytools = "\\".join(tmp[:s])
    
    def append_paths_pytools(self):
        self.append_paths_plus_subDir(self.dir_pytools)
    
    def append_paths_plus_subDir(self,dir_base):
        dir_lists = glob.glob(dir_base + "/*")
        if not dir_lists == []:
            for i in dir_lists:
                sys.path.append(i)
                self.append_paths_plus_subDir(i)
    
    def read_config(self,*args,**kwargs):
        if len(args)==0 and len(kwargs)==0:
            print(self.dir_pytools + "\\lib\\util")
    
    def add(self,*args):
        for path in args:
            if type(path)==str:
                self.data.append(path)
            
            print(self.data)