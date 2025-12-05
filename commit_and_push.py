#!/usr/bin/env python3
"""
commit_and_push.py
用于在本地将更改提交并推送到远端（仅作为参考脚本）。
注意：脚本使用本地 git 环境和远程凭证（SSH key 或已配置的 HTTPS 凭证）。
在自动化环境中请慎重使用并确保凭证安全。

用法:
  python commit_and_push.py "commit message"

行为:
  - git add ai_app .github generate_code.py commit_and_push.py
  - git commit -m "<message>"
  - git push origin main

如果仓库尚未初始化或没有远端，请先在本地运行 git init / git remote add origin <url>。
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run(cmd, check=True):
    print(">", " ".join(cmd))
    return subprocess.run(cmd, cwd=ROOT, check=check)

def main():
    if len(sys.argv) < 2:
        print("Usage: commit_and_push.py \"commit message\"")
        sys.exit(2)
    msg = sys.argv[1]

    files = ["ai_app", ".github", "generate_code.py", "commit_and_push.py"]
    try:
        run(["git", "add"] + files)
        run(["git", "commit", "-m", msg])
        run(["git", "push", "origin", "main"])
        print("Pushed to origin/main")
    except subprocess.CalledProcessError as e:
        print("Git command failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
