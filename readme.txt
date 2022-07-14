1.ライブラリのインストール
$ pip install -r requirements.txt


2.Youtube Data API V3のAPIキーの取得
2.1.任意のGoogleアカウントにログインした状態で、Google Developer Consoleにアクセス
https://console.developers.google.com/
2.2.画面上部の検索ボックスにて「Youtube Data API V3」と検索し、「有効にする」ボタンをクリック
2.3.画面に表示された「認証情報を作成」をクリック
2.4.使用するAPIで「Youtube Data API V3」を選択、アクセスするデータの種類にて「一般公開データ」を選択し次へをクリック
2.5.画面に表示されたAPIキーをコピーし取得、完了をクリック。APIキーが使用可能となります。

※注1　Googleのサイトに更新があった場合、設定方法に変更が生じる可能性がございます。
※注2　記載長くなりますが、完了後、「OAuth 同意画面の設定」（アプリサービス等でAPIを使用する際に、API経由でユーザーのデータにアクセスする時の認証画面の設定)を求められた場合、2.5.完了時に画面右上に表示された「同意画面を構築」から手続きが行えます。


3.APIキーの記入
config.pyの"APIキーを記入"部分にAPIキーを記入


4.スクレイピングの実行
$ python scraping_youtube.py
実行すると該当YouTube動画のコメントを自動で取得し、csvファイルで出力します。


各ファイル/フォルダの簡易説明

・config.py
scraping_youtube.pyから呼び出すモジュール
APIキー、入出力のpath、文字コード等を指定

・「input」
brand, video_idを記載したファイルなどを格納するフォルダ

・video_id.csv
brand, video_id列それぞれに、ブランドとYouTubeのビデオIDを記載。列名は変更不可です。
これを読んで処理を行います。

・「output」
スクレイピングした結果を格納するデフォルトのフォルダ。
video_id.csvのbrandが各出力csvのファイル名になります。

・scraping_youtube.py
実行するとスクレイピングするプログラム

・requirements.txt
必要なライブラリを記載しています
