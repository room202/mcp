from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# FastMCPサーバーの初期化
mcp = FastMCP("echo_hello")

# FastMCPサーバーが呼び出された時の処理
# 今回は「コンニチハ、～」と返すだけ
@mcp.tool()
async def echo_hello(name: str) -> str:
    """Echo a hello message"""
    return f"コンニチハ, {name}！！！！"

if __name__ == "__main__":
    # 初期化とサーバー実行
    mcp.run(transport='stdio')