# pytools
## pythonの様々なライブラリを使いやすいようにしたライブラリです（編集中）。spyderでの実行を想定しています。




## 前準備



> ***
> ### 1. Anacondaをインストールする
> ***
[Anaconda配布ページ](https://www.anaconda.com/products/distribution)へ行き、インストーラをダウンロードする。インストーラを実行し、指示に従ってインストールする。

tensorflowGPUの環境を整える場合は容量を多く使用するので、Anacondaの保存場所に注意する。



> ***
> ### 2. Windowsの場合、コマンドプロンプトで"conda"コマンドを使えるようにする
> ***
Anacondaをインストールした直後ではコマンドプロンプトで"conda"コマンドを実行できない。Anacondaインストールと同時にインストールされるAnaconda Promptを使う必要がある。そこで、利便性のために、コマンドプロンプトで実行できるようにしておくと良い。必須ではないが、後に便利。

Anaconda Promptを管理者で実行し、以下のコマンドを実行する。

`conda init`

実行すると、コマンドプロンプトで"conda"コマンドを使えるようになる。以降はコマンド実行をコマンドプロンプトで行えるようになる。



> ***
> ### 3. envフォルダのファイルを使い、仮想環境を構築する
> ***
Pythonでは通常、サードパーティ製ライブラリをインポートして使う。そのため、コマンドプロンプト（ターミナル）でコマンドを実行し、インポートできるように準備する必要がある。しかし、ライブラリの互換性やレポジトリの追加などと初心者には難しい。そこで、あらかじめコマンドがまとめられたファイルを実行し、作業を簡略化する。

Windowsの場合は"win_create"が含まれたファイルを管理者として実行する。

Macの場合は"mac_create"が含まれたファイルを実行する。

各ファイルは以下のライブラリを使うことを目的としている。必要な環境を構築する。すべて実行しても良い。

|ファイル名|Windows|Mac|説明|注意点|
|:--:|:--:|:--:|:--:|:--:|
|python_win_create_env_tensorflowCpu260.bat|〇||tensorflow、OpenCVの使用を目的とした仮想環境||
|python_win_create_env_flask.bat|〇||flaskの使用を目的とした仮想環境|flaskはコマンドプロンプトで実行するため、spyderでは実行できない|
|python_win_create_env_django.bat|〇||djangoの使用を目的とした仮想環境|djangoはコマンドプロンプトで実行するため、spyderでは実行できない|
|python_mac_create_env_flask.command||〇|flaskの使用を目的とした仮想環境|flaskはターミナルで実行するため、spyderでは実行できない|



## 使い方



> ***
> ### 1 envフォルダのファイルを使い、仮想環境で実行する
> ***
Windowsの場合は"win_exe"が含まれたファイルを管理者として実行する。

Macの場合は"mac_exe"が含まれたファイルを実行する。

各ファイルは以下のライブラリを使うことを目的としている。必要な環境を実行する。

|ファイル名|Windows|Mac|説明|注意点|
|:--:|:--:|:--:|:--:|:--:|
|python_win_exe_tensorflowCpu260.bat|〇||tensorflow、OpenCVの使用を目的とした仮想環境||
|python_win_exe_flask.bat|〇||flaskの使用を目的とした仮想環境|flaskはコマンドプロンプトで実行するため、spyderでは実行できない|
|python_win_exe_django.bat|〇||djangoの使用を目的とした仮想環境|djangoはコマンドプロンプトで実行するため、spyderでは実行できない、編集中|
|python_mac_exe_flask.command||〇|flaskの使用を目的とした仮想環境|flaskはターミナルで実行するため、spyderでは実行できない|



> ***
> ### 2 mainメソッドでの準備
> ***
mainメソッドの先頭で以下を実行することで、pytoolsライブラリをインポートする。
~~~ruby
if __name__ == "__main__":
    # ツールのパスを追加
    import sys
    import glob
    path_base = "G:\python\lib\pytools" # pytoolsのディレクトリを入力
    
    def append_paths_plus_subDir(dir_base):
        dir_lists = glob.glob(dir_base + "/*")
        if not dir_lists == []:
            for i in dir_lists:
                sys.path.append(i)
                append_paths_plus_subDir(i)
    
    append_paths_plus_subDir(path_base)
~~~

後は各ファイルのドキュメント（説明文）を参考に、必要な機能をインポートするだけです。
