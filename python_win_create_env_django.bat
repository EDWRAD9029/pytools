SET ENV=django
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


echo 仮想環境%ENV%へ切り替え
call activate %ENV%
echo;


echo インストール：django
call conda install -y -c conda-forge django


echo 処理が終了しました
cmd /k