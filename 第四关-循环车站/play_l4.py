"""循环车站 · AI 玩家入口

用法：
    python play_l4.py                       → 显示帮助 + 状态
    python play_l4.py look                  → 观察当前场景
    python play_l4.py "look 站牌残骸"        → 调查站牌残骸
    python play_l4.py "go 候车室"            → 前往候车室
    python play_l4.py "listen 月台广播喇叭"   → 收听广播
    python play_l4.py "question 为什么..."    → 记录未解问题
    python play_l4.py notebook              → 打开循环记录面板
    python play_l4.py trajectory            → 查看循环轨迹

存档自动保存在 detective_save_l4.json，每次运行状态自动保持。
重开：删除 detective_save_l4.json 即可。
"""
import sys
import detective_l4

if len(sys.argv) > 1:
    command = " ".join(sys.argv[1:])
    result = detective_l4.cmd(command)
    print(result)
else:
    print(detective_l4.cmd("help"))
    print()
    print(detective_l4.cmd("status"))
