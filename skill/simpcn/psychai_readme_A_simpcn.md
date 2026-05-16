# PsychAI · Option A 使用说明书

**版本**：v1.1 · 2026-05-15
**作者**：伪63
**许可证**：CC BY-NC-SA 4.0（署名 · 非商业 · 相同方式共享）
**商业授权**：请联系 j0sphe8@outlook.com

---

## 这是什么？

PsychAI Option A 是一个运行在 **Claude Code** 上的本地 Skill。

输入 `/psychai`，它会自动扫描你电脑上的文字材料——聊天记录、日记、录音转写稿、随手写的任何东西——结合 11 大临床心理学框架，为你生成一份完整的个人心理档案。档案保存在你本地，每次启动自动续写，越用越准。

所有数据留在你的电脑上，不上传任何服务器。

---

## Option A 还是 Option B？

| | Option A（本文） | Option B |
|--|--|--|
| 运行方式 | Claude Code 本地 Skill | 粘贴提示词到任意 AI |
| 门槛 | 需要安装环境（约 30 分钟） | 零安装，即开即用 |
| 材料读取 | 自动扫描本地文件夹 | 手动复制粘贴 |
| 档案保存 | 本地文件持久保存，跨对话无缝续写 | 每次对话需手动粘贴快照 |
| 适合谁 | 想要完整体验、愿意花时间配置的用户 | 想快速试用的用户 |

**我更推荐 Option A。** 门槛比 B 高一点，但配置只需要做一次——之后每次启动都是全自动：材料自动读取、档案自动更新、分析持续积累，不需要你手动做任何事。这是 B 无法提供的体验。

如果你只是想先体验一下，可以从 **Option B** 开始，感受满意后再回来配 A。

---

## 安装视频教程

> 📹 视频教程链接（待补充）

建议先看视频再看文字步骤——视频会一步步演示从安装到第一次运行的完整过程。

---

## 你需要准备什么

> ⚠️ **Windows 和 macOS 对应不同的 Skill 文件，请按你的系统下载对应版本，不要搞混。**

### 必须
- **Claude 账号**，并订阅 **Pro 计划**（$20/月）
  - 注册地址：claude.ai
  - 订阅 Pro 即可使用 Claude Code，不需要单独申请 API key
- **Python 3.11 或以上**
  - Windows：从 python.org 下载安装包，安装时勾选"Add to PATH"
  - macOS：终端运行 `brew install python@3.11`（需要先安装 Homebrew）

### 中国用户必读
访问 Claude 需要以下条件，请提前准备：
- **稳定的代理工具**（梯子），且支持 Claude 的节点（部分节点被封锁）
- **境外手机号**（用于注册 claude.ai，国内号码无法使用）
- **境外信用卡或 PayPal**（用于订阅 Pro，支付宝/微信支付不支持）

> 如果以上条件暂时无法满足，建议先使用 Option B（可搭配国内 AI 使用）。

### 可选（微信聊天记录读取）
- **WeFlow**（仅 Windows）：用于解密本地微信数据库，获取聊天记录
  - 下载地址：https://github.com/hicccc77/WeFlow
  - 安装后无需额外配置，PsychAI 会自动检测

---

## 安装步骤

### Step 1 · 安装 Claude Code

打开终端（Windows 用 PowerShell，macOS 用 Terminal），运行：

```
npm install -g @anthropic-ai/claude-code
```

> 如果提示 `npm` 未找到，需要先安装 Node.js：https://nodejs.org（下载 LTS 版本）

安装完成后验证：
```
claude --version
```
能看到版本号即为成功。

### Step 2 · 登录 Claude 账号

运行：
```
claude
```

首次启动会提示在浏览器中授权，按提示操作，用你的 claude.ai 账号登录即可。登录成功后关闭浏览器，回到终端继续。

### Step 3 · 下载 PsychAI 文件

从 GitHub 下载 Skill 主文件：

| 文件 | 说明 |
|------|------|
| `psychai_skill_windows_simpcn.md`（Windows 用）或 `psychai_skill_mac_simpcn.md`（macOS 用） | 按你的系统选择对应版本 |

> 文件读取脚本 `extract_text.py` 由 Skill 在首次运行时自动创建，**不需要手动下载**。

### Step 4 · 放置 Skill 文件

将下载的 skill 文件（`.md`）放入以下目录：

**Windows**：
```
C:\Users\你的用户名\.claude\commands\
```

**macOS**：
```
~/.claude/commands/
```

> 如果 `commands` 文件夹不存在，手动创建即可。

文件名可以自定义，但必须保留 `.md` 后缀。PsychAI 触发命令为 `/psychai`，与文件名无关。

### Step 5 · 安装 Python 依赖

在终端中运行：

```
pip install python-docx
```

如果需要处理 PDF 文件，额外运行：
```
pip install pdfplumber
```

### Step 6 · [可选] 安装 WeFlow（Windows 微信用户）

WeFlow 用于解密本地微信数据库，让 PsychAI 能直接读取你的聊天记录。

1. 从 https://github.com/hicccc77/WeFlow 下载最新版
2. 运行 WeFlow，按软件内提示完成微信数据导出
3. PsychAI 启动时会自动检测 WeFlow 输出路径

---

## 快速验证

安装完成后，在终端中进入你的工作目录，启动 Claude Code：

```
claude
```

然后输入：

```
/psychai
```

PsychAI 会自动检测环境并开始引导。如果看到欢迎语和问卷开始，说明安装成功。

---

## 什么材料最有用

安装完成后，把你的文字材料放入工作目录下的 `input/` 文件夹，PsychAI 会自动读取。以下这些效果最好：

| 材料类型 | 说明 |
|---------|------|
| **聊天记录** | 和朋友、家人、伴侣的对话（微信导出或手动复制均可） |
| **日记 / 随笔** | 任何关于自己、情绪、事件的文字，不需要正式 |
| **录音转写** | 对自己说话的录音、和他人对话的录音，转成文字后放入 |
| **随手写的东西** | 碎片也行，不需要完整 |

材料越多，分析越准确——PsychAI 能看到的行为模式越完整。

---

## 如何更新

当有新版本发布时，只需要：

1. 从 GitHub 下载新版 skill 文件
2. 替换掉 `~/.claude/commands/` 里的旧文件

不需要重新安装任何其他内容。每次发版的更新内容见 [CHANGELOG](../../CHANGELOG.md)。

---

## 常见问题

**Q：运行 `/psychai` 后提示"找不到命令"？**
检查 skill 文件是否放在正确目录（`~/.claude/commands/`），且文件后缀为 `.md`。

**Q：提示 Python 未找到？**
Windows 用户需确认安装 Python 时勾选了"Add to PATH"，或使用完整路径运行。macOS 用户尝试 `python3 --version` 确认版本。

**Q：WeFlow 检测不到微信数据？**
确认微信已在当前设备登录过，且 WeFlow 已完成初始导出。部分情况下需要以管理员身份运行 WeFlow。

**Q：分析结果保存在哪里？**
默认保存在工作目录下的 `analysis/` 文件夹中。

**Q：Claude Pro 和 API key 有什么区别？**
Option A 只需要 Claude Pro 订阅，不需要额外的 API key。两者都能驱动 Claude Code，对大多数用户来说 Pro 订阅即可。

---

## 联系与反馈

- **使用体验问卷**：https://wj.qq.com/s2/26641498/fbcf/
- **商业授权 / 合作**：j0sphe8@outlook.com
- **问题反馈**：GitHub Issues

---

*PsychAI · 伪63 · CC BY-NC-SA 4.0*
