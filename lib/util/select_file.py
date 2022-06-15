# -*- coding: utf-8 -*-
"""

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
    
    select_file_image : 画像ファイルを選択すると、そのファイルの絶対参照パスを返す
    
    select_file_movie : 動画ファイルを選択すると、そのファイルの絶対参照パスを返す
    """
    
    
    
    def __init__(self):
        pass
    
    
    
    def get_filetype(self,filetype="base"):
        """
        ファイルの種類を指定することで、ファイル拡張子を取得する。
    
        パラメータ
        ----------
        filetype : str
            ファイルのタイプ。
            デフォルトは "base"。
        
        返り値
        -------
        filetypes : list
            ファイル拡張子。
            デフォルトは [("ファイル",'*')]。
        
        """
        filetypes = {"base":[("ファイル",'*')],
                     "csv":[("CSVファイル",'.csv')],
                     "image":[("PNGファイル",'.png'),
                              ("JPGファイル",['.jpg','.jpeg']),
                              ("GIFファイル",'.jif'),
                              ("Photoshopファイル",'.psd'),
                              ("TIFFファイル",['.tif','.tiff']),
                              ("ビットマップファイル",'.bmp'),
                              ("TARGAファイル",'.tga')],
                     "movie":[("AVIファイル",'.avi'),
                              ("MPEG4ファイル",'.mp4'),
                              ("MOVファイル",'.mov'),
                              ("WMVファイル",'.wmv'),
                              ("MPEG2ファイル",'.mpg'),
                              ("MKVファイル",'.mkv'),
                              ("FLVファイル",'.flv'),
                              ("ASFファイル",'.asf'),
                              ("VOBファイル",'.vob')]}
        return filetypes[filetype]
    
    
    
    def select_file(self,data_dir=__file__,fig_title='',multiple=False):
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
        filetypes = self.get_filetype("base")
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
        filetypes = self.get_filetype("csv")
        # 拡張子にprefixをつなげる
        filetypes = [(i[0],[prefix+j for j in i[1]]) if type(i[1])==list else (i[0],prefix+i[1]) for i in filetypes]
        # データを選択する
        return self.select_file(filetypes=filetypes,data_dir=data_dir,fig_title=fig_title,multiple=False)
    
    
    
    def select_file_image(self,data_dir=__file__,fig_title='',prefix='*',multiple=False):
        """
        画像ファイルを選択する。
    
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
            例："*_log"とすると、ファイル名の最後が"_log"のファイルのみ選択できる。
        
        multiple : bool
            ファイルの複数選択を許可するか。trueは許可。
            デフォルトは False。
    
        返り値
        -------
        file_name : str
            ファイルの絶対参照パス。
        
    
        """
        filetypes = self.get_filetype("image")
        # 拡張子にprefixをつなげる
        filetypes = [(i[0],[prefix+j for j in i[1]]) if type(i[1])==list else (i[0],prefix+i[1]) for i in filetypes]
        # データを選択する
        return self.select_file(filetypes=filetypes,data_dir=data_dir,fig_title=fig_title,multiple=False)
    
    
    
    def select_file_movie(self,data_dir=__file__,fig_title='',prefix='*',multiple=False):
        """
        動画ファイルを選択する。
    
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
            例："*_log"とすると、ファイル名の最後が"_log"のファイルのみ選択できる。
        
        multiple : bool
            ファイルの複数選択を許可するか。trueは許可。
            デフォルトは False。
    
        返り値
        -------
        file_name : str
            ファイルの絶対参照パス。
        
    
        """
        filetypes = self.get_filetype("movie")
        # 拡張子にprefixをつなげる
        filetypes = [(i[0],[prefix+j for j in i[1]]) if type(i[1])==list else (i[0],prefix+i[1]) for i in filetypes]
        # データを選択する
        return self.select_file(filetypes=filetypes,data_dir=data_dir,fig_title=fig_title,multiple=False)