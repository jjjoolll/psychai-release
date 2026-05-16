"""
check_skill_sync.py — 检查 psychai_skill_mac_simpcn.md 和 psychai_skill_windows_simpcn.md 的共享段落是否同步

共享段落定义：以下这些章节在两个 skill 文件里应该完全一致，因为它们与操作系统无关：
- 第三节 C：口吻设定协议
- 第四节：初步问卷协议
- 第五节：材料索取与档案构建（不含 WeChat 接入子节，因为 Mac/Windows 描述不同）
- 第六节：心理学分析框架
- 第七节：分析操作原则
- 第八节：输出文件写入规则
- 第十节：纠正与更新机制
- 第十一节：每次结束时

不应该同步的部分（OS-specific）：
- 第一节：检查工作目录（路径不同）
- 第二节：判断运行模式（命令不同，WeFlow 步骤不同）
- 第三节：文件读取规则（命令和格式表不同）
- 第三节 B：WeFlow 集成协议（仅 Windows 有）
- 第九节：错误处理协议（场景列表不同）

用法：
    python check_skill_sync.py

输出：
    - 共享段落 diff（如有差异则报告）
    - 退出码 0 = 同步，1 = 有差异
"""

import sys
import io
import re
from pathlib import Path
from difflib import unified_diff

# 强制 stdout/stderr 用 UTF-8（兼容 Windows GBK 终端）
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# 共享章节边界标记（开始标题, 结束的下一个标题）
SHARED_SECTIONS = [
    ('## 第三节 C：口吻设定协议', '## 第四节'),
    ('## 第四节：初步问卷协议', '## 第五节'),
    ('## 第六节：心理学分析框架', '## 第七节'),
    ('## 第七节：分析操作原则', '## 第八节'),
    ('## 第八节：输出文件写入规则', '## 第九节'),
    ('## 第十节：纠正与更新机制', '## 第十一节'),
    ('## 第十一节：每次结束时', '## 版权声明'),
]


def extract_section(content: str, start_marker: str, end_marker: str) -> str:
    """从全文中按章节标记切出一段。返回 start_marker 到 end_marker 之间（不含 end_marker）的内容。"""
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return ''
    end_idx = content.find(end_marker, start_idx + len(start_marker))
    if end_idx == -1:
        return content[start_idx:]
    return content[start_idx:end_idx]


def main():
    base = Path(__file__).parent
    mac_path = base / 'simpcn' / 'psychai_skill_mac_simpcn.md'
    win_path = base / 'simpcn' / 'psychai_skill_windows_simpcn.md'

    if not mac_path.exists():
        print(f"找不到：{mac_path}")
        sys.exit(2)
    if not win_path.exists():
        print(f"找不到：{win_path}")
        sys.exit(2)

    mac_content = mac_path.read_text(encoding='utf-8')
    win_content = win_path.read_text(encoding='utf-8')

    all_ok = True
    print(f"对比共享段落：{mac_path.name} ↔ {win_path.name}")
    print("=" * 60)

    for start, end in SHARED_SECTIONS:
        mac_section = extract_section(mac_content, start, end).strip()
        win_section = extract_section(win_content, start, end).strip()

        section_name = start.replace('## ', '')

        if not mac_section and not win_section:
            print(f"⚠️  [{section_name}] 两文件都缺失此章节")
            all_ok = False
            continue
        if not mac_section:
            print(f"⚠️  [{section_name}] Mac 版缺失")
            all_ok = False
            continue
        if not win_section:
            print(f"⚠️  [{section_name}] Windows 版缺失")
            all_ok = False
            continue

        if mac_section == win_section:
            print(f"✅ [{section_name}] 一致")
        else:
            all_ok = False
            mac_lines = mac_section.splitlines()
            win_lines = win_section.splitlines()
            diff_lines = list(unified_diff(
                mac_lines, win_lines,
                fromfile='mac', tofile='windows',
                lineterm='', n=2
            ))
            diff_count = sum(1 for line in diff_lines if line.startswith(('+', '-')) and not line.startswith(('+++', '---')))
            print(f"❌ [{section_name}] 不一致（{diff_count} 行差异）")
            print('   --- 差异预览（前 20 行）---')
            for line in diff_lines[:20]:
                print(f'   {line}')
            if len(diff_lines) > 20:
                print(f'   ... 共 {len(diff_lines)} 行差异（已截断）')
            print()

    print("=" * 60)
    if all_ok:
        print("✅ 所有共享段落已同步")
        sys.exit(0)
    else:
        print("❌ 发现差异，需要手动同步两文件")
        sys.exit(1)


if __name__ == '__main__':
    main()
