from pathlib import Path

# youtube動画のurlが記載されたファイルを指定
INPUT_FILE = Path("input/video_id.csv")

# 取得したコメントを保存するpathを指定
OUTPUT_PATH = Path("output")

# 文字コードを指定
# cp932には非対応の文字も含まれるため、utf-8-sigを指定
ENCODING = "utf-8-sig"

# APIのキーを指定
API_KEY = "APIキーを記入"

# YouTube Data API v3へリクエストを送る際のベースとなるURLを記載
URL = 'https://www.googleapis.com/youtube/v3/'
