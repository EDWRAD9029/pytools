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
    
    def __str__(self):
        return self.filepath
    
    
    def set_dir(self,new_path=None):
        """
        絶対参照パスを保存する。
        
        パラメータ
        ----------
        new_path : str
            ファイルの絶対参照パス。
        
        返り値
        -------
        None
        
        """
        self.filepath = new_path
    
    
    
    def select(self,filetype=None):
        """
        ファイルを選択し、絶対参照パスを保存する。
        
        パラメータ
        ----------
        filetype : str
            ファイルの種類。指定しない場合は全てのファイルから選択できる。
            大文字は全て小文字として判断される。
            対応していない文字列の場合はエラーを表示する。
            デフォルトは None。
            ---------------------------------
            |   filetype  |       対象       |
            =================================
            |     None    | 全てのファイル 複数  |
            ---------------------------------
            |     csv     | CSVファイル 1つ     |
            ---------------------------------
            |     csvs    | CSVファイル 複数   |
            ---------------------------------
            |  image,img  | 画像ファイル 1つ    |
            ---------------------------------
            | images,imgs | 画像ファイル 複数  |
            ---------------------------------
            |    movie    | 動画ファイル 1つ    |
            ---------------------------------
            |    movies   | 動画ファイル 複数  |
            ---------------------------------
            例："image"とすると、画像ファイル名のみ選択できるようになる。
        
        返り値
        -------
        None
        
        """
        selector = select_file.selector_files()
        if filetype == None:
            self.set_dir(selector.select_file(multiple=True))
        elif filetype.lower() in ["csv"]:
            self.set_dir(selector.select_file_csv())
        elif filetype.lower() in ["csvs"]:
            self.set_dir(selector.select_file_csv(multiple=True))
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