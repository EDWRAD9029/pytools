# -*- coding: utf-8 -*-
"""
@author: nomut
"""

import tkinter.filedialog as dialog


class selector_files():
    """
    ファイル選択関連をまとめたクラス。
    
    パラメータ
    ----------
    なし
    
    メソッド
    ----------
    select_file : ファイルを選択すると、そのファイルの絶対参照パスを返す
    
    select_file_csv : CSVファイルを選択すると、そのファイルの絶対参照パスを返す
    
    """
    
    def __init__(self):
        pass
    
    def select_file(self,filetypes=[("ファイル",'*')],data_dir=__file__,fig_title='',multiple=False):
        """
        ファイルを選択する。
    
        パラメータ
        ----------
        filetypes : list
            選択するファイルのタイプ。
            デフォルトは [("ファイル",'*')]。
        
        data_dir : str
            最初に開くディレクトリ。
            デフォルトは __file__。
        
        fig_title : str
            ファイル選択ウインドウのタイトル名。
            デフォルトは ''。
        
        multiple : bool
            ファイルの複数選択を許可するか。trueは許可。
            デフォルトは False。
    
        返り値
        -------
        file_name : str
            ファイルの絶対参照パス。
        
    
        """
        return dialog.askopenfilename(filetypes = filetypes,initialdir = data_dir,title = fig_title)
    
    
    
    def select_file_csv(self,data_dir=__file__,fig_title='',prefix='*',multiple=False):
        """
        CSVファイルを選択する。
    
        パラメータ
        ----------
        data_dir : str
            最初に開くディレクトリ。
            デフォルトは __file__。
        
        fig_title : str
            ファイル選択ウインドウのタイトル名。
            デフォルトは ''。
        
        prefix : str
            ファイル名。指定しない場合はファイル名で候補がしぼられない。
            "*"を使用することで部分検索が可能。
            デフォルトは '*'。
            例："*_log"とすると、ファイル名の最後が"_log.csv"のファイルのみ選択できる。
        
        multiple : bool
            ファイルの複数選択を許可するか。trueは許可。
            デフォルトは False。
    
        返り値
        -------
        file_name : str
            ファイルの絶対参照パス。
        
    
        """
        #csvのファイル拡張子
        csv_filetypes: list = [("CSVファイル",prefix+'.csv')]
        #データを選択する
        return self.select_file(filetypes=csv_filetypes,data_dir=data_dir,fig_title=fig_title,multiple=False)