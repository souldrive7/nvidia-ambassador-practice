# ここでは .bashrc に設定した NVIDIA_API_KEY を取得するために使う
import os
import requests

# NVIDIA Build のチャットAPIの接続先URL
# /v1/chat/completions は、会話形式で文章生成を行うエンドポイント
url = "https://integrate.api.nvidia.com/v1/chat/completions"

# 環境変数 NVIDIA_API_KEY からAPIキーを取得
# WSL上で export NVIDIA_API_KEY="..." と設定した値を読む
api_key = os.environ["NVIDIA_API_KEY"]

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# APIに送る本体データ（ペイロード）
payload = {
    "model": "meta/llama-3.1-8b-instruct",

    # 会話履歴を配列で渡す
    # role が user なので「ユーザーからの質問」という意味
    "messages": [
        {
            "role": "user",
            "content": "NVIDIA student ambassadorとして何を学ぶべきか3つ教えて"
        }
    ],
    "max_tokens": 300
}

# POSTリクエストを送信
# url: 接続先
# headers: 認証やデータ形式の指定
# json=payload: Pythonの辞書をJSON形式に変換して送る
response = requests.post(url, headers=headers, json=payload)

# HTTPエラーがあれば例外を出す
# 例: 401 認証失敗, 404 URL違い, 500 サーバエラー
# 成功時(200番台)はそのまま次へ進む
response.raise_for_status()

# 返ってきたJSON文字列をPythonの辞書型に変換
data = response.json()

# HTTPステータスコードを表示
# 成功なら通常 200
print("HTTPステータス:", response.status_code)

print()

# 見出しを表示
print("モデルの返答:")

# JSONの中から、モデルの返答本文だけを取り出して表示
# choices   : 候補の配列
# [0]       : 最初の候補
# ["message"]: メッセージ本体
# ["content"]: 実際の返答文
print(data["choices"][0]["message"]["content"])
