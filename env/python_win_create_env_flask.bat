SET ENV=flask
rem 文字コードの変更(UTF8に)
chcp 65001


echo anacondaのversion確認
rem condaが実行可能か確認（エラーが出たら不可）
conda --version
echo;


echo 仮想環境の一覧を表示
conda info -e
echo;


echo 環境作成
conda create -n %ENV%
echo;


echo 仮想環境%ENV%へ切り替え
activate %ENV%
echo;


echo パッケージの更新
conda upgrade -y --all


echo 無駄なファイルを削除
conda clean -y --packages


echo インストール：flask
conda install -y flask
conda install -y flask-sqlalchemy
conda install -y flask-wtf


echo 処理が終了しました
rem ここで処理を止めて、以降入力可
rmd /k