"""档案室·终点 · AI 玩家入口

用法：
    python play_l5.py                  → 显示帮助 + 状态
    python play_l5.py look             → 查看当前区域
    python play_l5.py "look 左侧文件柜" → 切换到左侧文件柜
    python play_l5.py "read 卷宗"       → 阅读卷宗
    python play_l5.py "read 记事本"     → 阅读记事本
    python play_l5.py "read 陈述信"     → 阅读陈述信
    python play_l5.py "take 药瓶"       → 服用药片（不可逆！）
    python play_l5.py "close 卷宗"      → 合上卷宗
    python play_l5.py leave            → 离开档案室

存档自动保存在 detective_save_l5.json，每次运行状态自动保持。
重开：删除 detective_save_l5.json 即可。
（会自动读取第四关存档中的遗忘程度数据）
"""
import sys
import detective_l5

if len(sys.argv) > 1:
    command = " ".join(sys.argv[1:])
    result = detective_l5.cmd(command)
    print(result)
else:
    print(detective_l5.cmd("help"))
    print()
    print(detective_l5.cmd("status"))
