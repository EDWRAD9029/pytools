SET ENV=tensorflowCpu260

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


echo チャンネルからconda-forgeを削除
conda config --remove channels conda-forge


echo パッケージの更新
conda upgrade -y --all


echo 無駄なファイルを削除
conda clean -y --packages


echo インストール：tensorflow
rem CPU版のtensorflow
conda install -y tensorflow tensorflow-datasets


echo インストール：opencv pytorch dlib
conda install -y opencv pytorch
conda install -y -c conda-forge dlib
conda config --remove channels conda-forge


echo インストール：その他
conda install -y matplotlib numpy scipy h5py scikit-learn scikit-learn-intelex scikit-image seaborn pandas pandasql pillow pytest pyyaml cython


echo インストール：Spyder
rem 仮想環境でspyderを起動するには、個別にspyderを
rem インストールする必要がある
conda install -y spyder

echo インストール：mypy
rem pythonで型確認をするために必要
conda install mypy

rem echo spyderを起動
rem spyder


echo 処理が終了しました
rem ここで処理を止めて、以降入力可
rmd /k