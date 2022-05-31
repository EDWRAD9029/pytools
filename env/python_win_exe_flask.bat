rem 文字コードの変更(UTF8に)
chcp 65001

SET ENV=flask

call activate %ENV%

echo 処理が終了しました
rem ここで処理を止めて、以降入力可
rmd /k