"""褪色车站 · AI 玩家入口

用法：
    python play_l3.py                     → 显示帮助 + 状态
    python play_l3.py look                → 观察当前场景
    python play_l3.py "go 月台"           → 前往月台
    python play_l3.py "talk 退休站务员"    → 与站务员对话
    python play_l3.py "ask 退休站务员 死者出现"  → 询问话题

存档自动保存在 detective_save_l3.json，每次运行状态自动保持。
重开：删除 detective_save_l3.json 即可。
"""
import sys
import detective_l3

if len(sys.argv) > 1:
    command = " ".join(sys.argv[1:])
    result = detective_l3.cmd(command)
    print(result)
else:
    detective_l3.cmd("help")
    print()
    print(detective_l3.cmd("status"))
