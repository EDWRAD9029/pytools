# pytools
## pythonの様々なライブラリを使いやすいようにしたライブラリです（編集中）。spyderでの実行を想定しています。

## 前準備
### 1. Anacondaをインストールする。
***
[Anaconda配布ページ](https://www.anaconda.com/products/distribution)へ行き、インストーラをダウンロードする。

### 2. Windowsの場合、コマンドプロンプトで"conda"コマンドを使えるようにする。
***
Anacondaをインストールした直後ではコマンドプロンプトで"conda"コマンドを実行できない。Anacondaインストールと同時にインストールされるAnaconda Promptを使う必要がある。そこで、利便性のために、コマンドプロンプトで実行できるようにしておくと良い。必須ではないが、後に便利。

Anaconda Promptを管理者で実行し、以下のコマンドを実行する。

`conda init`

実行すると、コマンドプロンプトで"conda"コマンドを使えるようになる。以降はコマンド実行をコマンドプロンプトで行えるようになる。

### 3. envフォルダのファイルを使い、仮想環境を構築する。
***
Windowsの場合は"win_create"が含まれたファイルを管理者として実行する。
Macの場合は"mac_create"が含まれたファイルを実行する。
各ファイルは以下のライブラリを使うことを目的としている。

|ファイル名|Windows|Mac|説明|注意点|
|:--:|:--:|:--:|:--:|:--:|
|python_win_create_env_tensorflowCpu260.bat|〇||tensorflow、OpenCVの使用を目的とした仮想環境||
|python_win_create_env_flask.bat|〇||flaskの使用を目的とした仮想環境|flaskはコマンドプロンプトで実行するため、spyderでは実行できない|
|python_win_create_env_django.bat|〇||djangoの使用を目的とした仮想環境|djangoはコマンドプロンプトで実行するため、spyderでは実行できない|
|python_mac_create_env_flask.command||〇|flaskの使用を目的とした仮想環境|flaskはターミナルで実行するため、spyderでは実行できない|
