# -*- coding: utf-8 -*-
"""

"""

from .util import select_file

class Files():
    """
    ファイル情報のクラス。
    
    パラメータ
    ----------
    filepath : str
    
    
    メソッド
    ----------
    set_dir : ファイル情報を設定する
    
    select : ファイルを選択し、保存する
    
    """
    def __init__(self):
        pass
    
    def set_dir(self,new_path=None):
        self.filepath = new_path
    
    def select(self,filetype=None):
        selector = select_file.selector_files()
        if filetype == None:
            self.set_dir(selector.select_file())
        elif filetype.lower() in ["csv"]:
            self.set_dir(selector.select_file_csv())
        elif filetype.lower() in ["image","img"]:
            self.set_dir(selector.select_file_image())
        elif filetype.lower() in ["images","imgs"]:
            self.set_dir(selector.select_file_image(multiple=True))
        elif filetype.lower() in ["movie"]:
            self.set_dir(selector.select_file_movie())
        elif filetype.lower() in ["movies"]:
            self.set_dir(selector.select_file_movie(multiple=True))
        else:
            import traceback
            import inspect
            try:
                raise Exception("\n"
                    "=========================================================\n"
                    "    問題が発生しました !\n"
                    "=========================================================\n"
                    "モジュール : "+__name__+"\n"+
                    "メソッド : "+inspect.currentframe().f_code.co_name+"\n"+
                    "詳細 : ""引数filetypeは "+filetype+" に対応していません\n"
                    )
            except:
                traceback.print_exc()