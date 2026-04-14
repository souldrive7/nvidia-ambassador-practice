# NVIDIA Ambassador Practice

NVIDIA Build API, Docker, NGC PyTorch Container, GPU-enabled PyTorch を学ぶための練習用プロジェクトです。

## このプロジェクトで確認したこと
- WSL2 Ubuntu で Linux コマンドを使う
- NVIDIA Build API を Python から呼ぶ
- GitHub でコード管理する
- Docker で実行環境を管理する
- NGC の PyTorch コンテナを pull / run する
- GPU がコンテナ内から見えることを確認する
- PyTorch で GPU テンソル計算を行う

## ファイル
- `my_ai_nvidia.py` : NVIDIA Build API を呼ぶサンプル
- `gpu_check.py` : PyTorch と GPU の確認用スクリプト
- `run_pytorch.sh` : NGC PyTorch コンテナ起動用スクリプト

## 事前準備
- Docker が使えること
- `NVIDIA_API_KEY` が環境変数に設定されていること
- NGC にログイン済みであること

## 使い方

### 1. PyTorch コンテナに入る
```bash
./run_pytorch.sh
2. GPU確認
python gpu_check.py
3. NVIDIA Build API確認
python my_ai_nvidia.py

