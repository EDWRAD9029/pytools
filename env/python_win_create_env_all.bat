SET ENV=all

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


echo チャンネルからconda-forgeを削除
call conda config --remove channels conda-forge


echo パッケージの更新
call conda upgrade -y --all


echo 無駄なファイルを削除
call conda clean -y --packages


echo インストール：tensorflow
rem CPU版のtensorflow
call conda install -y tensorflow tensorflow-datasets


echo インストール：opencv pytorch dlib
call conda install -y opencv pytorch
call conda install -y -c conda-forge dlib


echo インストール：Tesseract OCR
call conda install -y -c conda-forge tesseract

echo インストール：PyOCR
call conda install -y -c conda-forge pyocr


echo インストール：その他
call conda install -y matplotlib numpy scipy h5py scikit-learn scikit-learn-intelex scikit-image seaborn pandas pandasql pillow pytest pyyaml cython


echo インストール：Spyder
rem 仮想環境でspyderを起動するには、個別にspyderを
rem インストールする必要がある
call conda install -y spyder

echo インストール：mypy
rem pythonで型確認をするために必要
call conda install mypy

echo 処理が終了しました
cmd /k