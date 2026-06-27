"""午夜特快 · AI 玩家入口

用法：
    python play_l2.py                     → 显示帮助 + 状态
    python play_l2.py look                → 观察当前场景
    python play_l2.py "look 门链"         → 调查门链
    python play_l2.py "go 餐车"           → 前往餐车
    python play_l2.py "talk 乘务长"        → 与乘务长对话
    python play_l2.py "ask 乘务长 巡逻路线" → 询问话题
    python play_l2.py "combine needle_hole_metal door_gap_height"  → 组合证据

存档自动保存在 detective_save_l2.json，每次运行状态自动保持。
重开：删除 detective_save_l2.json 即可。
"""
import sys
import detective_l2

if len(sys.argv) > 1:
    command = " ".join(sys.argv[1:])
    result = detective_l2.cmd(command)
    print(result)
else:
    detective_l2.cmd("help")
    print()
    print(detective_l2.cmd("status"))
