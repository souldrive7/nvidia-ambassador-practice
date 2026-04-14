# NVIDIA Ambassador Practice

NVIDIA Build API を使って、WSL Ubuntu から Python で推論APIを呼び出す練習用コードです。

## 実行前提
- WSL2 Ubuntu
- Python 3
- requests
- NVIDIA_API_KEY を環境変数に設定済み

## 使い方
```bash
python3 my_ai_nvidia.py

## Git 初期化
```bash
git init
git status
cat > .gitignore <<'EOF'
__pycache__/
*.pyc
response.json
.env
