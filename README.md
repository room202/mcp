# MCPサーバーのサンプル

## 動作環境

- Windows11 Pro 23H2
- Python 3.13.2
- uv 0.6.12

## 事前準備

- Visual Studio Codeのインストール
- Pythonのインストール
- uvコマンドのインストール

### uvコマンドのインストール

PowerShellから下記コマンドを実行する

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 初回のプロジェクト作成

```bash
# プロジェクトの新規作成
uv init echo_hello
cd echo_hello

# Python仮想環境を使用
uv venv
.venv\Scripts\activate

# 依存関係をインストールする
uv add mcp[cli] httpx

# MCPサーバーのソースコード作成
# 今回は「hello.py」とする
new-item hello.py
```

## MCPサーバー本体をPythonで作成

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# FastMCPサーバーの初期化
mcp = FastMCP("echo_hello")

# FastMCPサーバーが呼び出された時の処理
@mcp.tool()
async def echo_hello(name: str) -> str:
    # 今回は「コンニチハ、{プロンプトから渡された値}！！！！」と返すだけ
    return f"コンニチハ, {name}！！！！"

if __name__ == "__main__":
    # 初期化とサーバー実行
    mcp.run(transport='stdio')
```

## MCPサーバーの登録

ファイル：`C:\Users\%USERPROFILE%\AppData\Roaming\Code\User\settings.json`

```json
～省略～
"mcp": {
    "inputs": [],
    "servers": {
        "echo_hello": {
            "command": "uv",
            "args": [
                "--directory",
                "C:\\Workspace\\mcp\\mcp_server_demo\\echo_hello",
                "run",
                "echo_hello.py"
            ]
        }
    }
},
```
