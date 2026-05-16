# CHANGELOG

所有版本的更新记录。格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

---

## [1.2.0] — 2026-05-15

### Option A（Skill 版）
- 新增：繁體中文版 Skill（Windows / macOS 各一份）及配套說明書
- 新增：英文版 Skill（Windows / macOS 各一份）及配套 Guide
- 改名：简中版 Skill 文件加 `_simpcn` 后缀，与繁中/英文版命名风格统一（`psychai_skill_windows_simpcn.md` / `psychai_skill_mac_simpcn.md`）
- 修复：各语言 Skill 文件第 6 行平台交叉引用现指向同语言版本（不再混指简中文件）

### Option B（提示词版）
- 修复：繁中/英文说明书的"Option A 说明书"跳转链接改为各自语言对应版本（繁中→繁中，英文→英文）

### 文档结构
- 更新：主 README 新增繁體中文、English 两个语言板块（含各自的选版引导、文件链接、文档注释）
- 更新：主 README 顶部加语言切换导航栏；声明 CHANGELOG / LIMITATIONS 仅提供简体中文版

---

## [1.1.0] — 2026-05-15

### Option A（Skill 版）
- 新增：开场声明三项可选功能（自我改变方案 / 知识记录 / 叙事探索记录），询问用户是否开启，可随时切换

### Option B（提示词版）
- 新增：说明书加入"Option A 还是 Option B"对比引导
- 修改：说明书全面适配多 AI 平台表述（Claude、ChatGPT、豆包等）
- 修改：说明书 FAQ 增加多个 AI 选项推荐

### 文档结构
- 新增：总项目 README.md 导航页
- 新增：CHANGELOG.md / ROADMAP.md / LIMITATIONS.md
- 重组：提示词文件夹拆分为 skill/ 和 prompt/ 两个子目录，各含语言子文件夹

---

## [1.0.0] — 2026-05-11

### 首次发布

**Option B（提示词版）**
- 发布简体中文 / 繁体中文 / 英文三语版提示词
- 11 大心理学框架完整覆盖（Big Five / 依恋 / 防御 / Beck / Kernberg / Winnicott / Kohut / Young / 叙事 / Siegel / Karpman）
- 动态问卷（6域必须覆盖，域内追问一次）
- 跨会话快照功能（`【PsychAI档案快照】`格式）
- 大量文本处理协议
- 分析完成后正常化隐瞒的提示语
- 群聊 vs 私聊分析区分

**Option A（Skill 版）**
- 发布 Windows 版（含 WeFlow 微信解密集成）
- 发布 macOS 版（试运行，暂无 WeFlow 集成）
- 自动文件读取（docx / pdf / txt / md）
- 7 个独立档案文件持久保存
- 问卷进度可视化
- 首次分析置信度标签
- 上下文窗口摘要管理
- `/psychai snapshot` 快速输出完整档案命令
- 危机出口提醒（自伤/绝望信号触发时附危机热线）
- 关键洞察前准备度询问

---

*更早的开发历史见项目内部日志*
