SET ENV=flask
rem 文字コードの変更(UTF8に)
chcp 65001


echo anacondaのversion確認
rem condaが実行可能か確認（エラーが出たら不可）
call conda --version
echo;


echo 仮想環境の一覧を表示
call conda info -e
echo;


echo 環境作成
call conda create -y -n %ENV%
echo;

timeout 3

echo 仮想環境%ENV%へ切り替え
call activate %ENV%
echo;

timeout 3

echo インストール：flask
call conda install -y flask
call conda install -y flask-sqlalchemy
call conda install -y flask-wtf

echo 処理が終了しました
cmd /k