"""蓝玫瑰庄园 · AI 玩家入口

用法：
    python play.py                     → 显示帮助 + 状态
    python play.py look                → 观察当前场景
    python play.py look 银勺           → 调查银勺
    python play.py go 厨房             → 前往厨房
    python play.py talk 管家           → 与管家对话
    python play.py "look 银勺; go 厨房; talk 管家"  → 批量指令

存档自动保存在 detective_save.json，每次运行状态自动保持。
重开：删除 detective_save.json 即可。
"""
import sys
import detective

if len(sys.argv) > 1:
    command = " ".join(sys.argv[1:])
    result = detective.cmd(command)
    print(result)
else:
    # 首次运行：显示帮助 + 状态
    detective.cmd("help")
    print()
    print(detective.cmd("status"))
