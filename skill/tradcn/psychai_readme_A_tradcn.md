# PsychAI · Option A 使用說明書

**版本**：v1.1 · 2026-05-15
**作者**：偽63
**許可證**：CC BY-NC-SA 4.0（署名 · 非商業 · 相同方式共享）
**商業授權**：請聯絡 j0sphe8@outlook.com

---

## 這是什麼？

PsychAI Option A 是一個執行在 **Claude Code** 上的本地 Skill。

輸入 `/psychai`，它會自動掃描你電腦上的文字材料——聊天記錄、日記、錄音轉寫稿、隨手寫的任何東西——結合 11 大臨床心理學框架，為你生成一份完整的個人心理檔案。檔案儲存在你本地，每次啟動自動續寫，越用越準。

所有資料留在你的電腦上，不上傳任何伺服器。

---

## Option A 還是 Option B？

| | Option A（本文） | Option B |
|--|--|--|
| 執行方式 | Claude Code 本地 Skill | 貼上提示詞到任意 AI |
| 門檻 | 需要安裝環境（約 30 分鐘） | 零安裝，即開即用 |
| 材料讀取 | 自動掃描本地資料夾 | 手動複製貼上 |
| 檔案儲存 | 本地檔案持久儲存，跨對話無縫續寫 | 每次對話需手動貼上快照 |
| 適合誰 | 想要完整體驗、願意花時間配置的使用者 | 想快速試用的使用者 |

**我更推薦 Option A。** 門檻比 B 高一點，但配置只需要做一次——之後每次啟動都是全自動：材料自動讀取、檔案自動更新、分析持續積累，不需要你手動做任何事。這是 B 無法提供的體驗。

如果你只是想先體驗一下，可以從 **Option B** 開始，感受滿意後再回來配 A。

---

## 安裝影片教程

> 📹 影片教程連結（待補充）

建議先看影片再看文字步驟——影片會一步步演示從安裝到第一次執行的完整過程。

---

## 你需要準備什麼

> ⚠️ **Windows 和 macOS 對應不同的 Skill 檔案，請按你的系統下載對應版本，不要搞混。**

### 必須
- **Claude 賬號**，並訂閱 **Pro 計劃**（$20/月）
  - 註冊地址：claude.ai
  - 訂閱 Pro 即可使用 Claude Code，不需要單獨申請 API key
- **Python 3.11 或以上**
  - Windows：從 python.org 下載安裝包，安裝時勾選"Add to PATH"
  - macOS：終端執行 `brew install python@3.11`（需要先安裝 Homebrew）

### 中國使用者必讀
訪問 Claude 需要以下條件，請提前準備：
- **穩定的代理工具**（梯子），且支援 Claude 的節點（部分節點被封鎖）
- **境外手機號**（用於註冊 claude.ai，國內號碼無法使用）
- **境外信用卡或 PayPal**（用於訂閱 Pro，支付寶/微信支付不支援）

> 如果以上條件暫時無法滿足，建議先使用 Option B（可搭配國內 AI 使用）。

### 可選（微信聊天記錄讀取）
- **WeFlow**（僅 Windows）：用於解密本地微信資料庫，獲取聊天記錄
  - 下載地址：https://github.com/hicccc77/WeFlow
  - 安裝後無需額外配置，PsychAI 會自動檢測

---

## 安裝步驟

### Step 1 · 安裝 Claude Code

開啟終端（Windows 用 PowerShell，macOS 用 Terminal），執行：

```
npm install -g @anthropic-ai/claude-code
```

> 如果提示 `npm` 未找到，需要先安裝 Node.js：https://nodejs.org（下載 LTS 版本）

安裝完成後驗證：
```
claude --version
```
能看到版本號即為成功。

### Step 2 · 登入 Claude 賬號

執行：
```
claude
```

首次啟動會提示在瀏覽器中授權，按提示操作，用你的 claude.ai 賬號登入即可。登入成功後關閉瀏覽器，回到終端繼續。

### Step 3 · 下載 PsychAI 檔案

從 GitHub 下載 Skill 主檔案：

| 檔案 | 說明 |
|------|------|
| `psychai_skill_windows_tradcn.md`（Windows 用）或 `psychai_skill_mac_tradcn.md`（macOS 用） | 按你的系統選擇對應版本 |

> 檔案讀取指令碼 `extract_text.py` 由 Skill 在首次執行時自動建立，**不需要手動下載**。

### Step 4 · 放置 Skill 檔案

將下載的 skill 檔案（`.md`）放入以下目錄：

**Windows**：
```
C:\Users\你的使用者名稱\.claude\commands\
```

**macOS**：
```
~/.claude/commands/
```

> 如果 `commands` 資料夾不存在，手動建立即可。

檔名可以自定義，但必須保留 `.md` 字尾。PsychAI 觸發命令為 `/psychai`，與檔名無關。

### Step 5 · 安裝 Python 依賴

在終端中執行：

```
pip install python-docx
```

如果需要處理 PDF 檔案，額外執行：
```
pip install pdfplumber
```

### Step 6 · [可選] 安裝 WeFlow（Windows 微信使用者）

WeFlow 用於解密本地微信資料庫，讓 PsychAI 能直接讀取你的聊天記錄。

1. 從 https://github.com/hicccc77/WeFlow 下載最新版
2. 執行 WeFlow，按軟體內提示完成微信資料匯出
3. PsychAI 啟動時會自動檢測 WeFlow 輸出路徑

---

## 快速驗證

安裝完成後，在終端中進入你的工作目錄，啟動 Claude Code：

```
claude
```

然後輸入：

```
/psychai
```

PsychAI 會自動檢測環境並開始引導。如果看到歡迎語和問卷開始，說明安裝成功。

---

## 什麼材料最有用

安裝完成後，把你的文字材料放入工作目錄下的 `input/` 資料夾，PsychAI 會自動讀取。以下這些效果最好：

| 材料型別 | 說明 |
|---------|------|
| **聊天記錄** | 和朋友、家人、伴侶的對話（微信匯出或手動複製均可） |
| **日記 / 隨筆** | 任何關於自己、情緒、事件的文字，不需要正式 |
| **錄音轉寫** | 對自己說話的錄音、和他人對話的錄音，轉成文字後放入 |
| **隨手寫的東西** | 碎片也行，不需要完整 |

材料越多，分析越準確——PsychAI 能看到的行為模式越完整。

---

## 如何更新

當有新版本釋出時，只需要：

1. 從 GitHub 下載新版 skill 檔案
2. 替換掉 `~/.claude/commands/` 裡的舊檔案

不需要重新安裝任何其他內容。每次發版的更新內容見 [CHANGELOG](../../CHANGELOG.md)。

---

## 常見問題

**Q：執行 `/psychai` 後提示"找不到命令"？**
檢查 skill 檔案是否放在正確目錄（`~/.claude/commands/`），且檔案字尾為 `.md`。

**Q：提示 Python 未找到？**
Windows 使用者需確認安裝 Python 時勾選了"Add to PATH"，或使用完整路徑執行。macOS 使用者嘗試 `python3 --version` 確認版本。

**Q：WeFlow 檢測不到微信資料？**
確認微信已在當前裝置登入過，且 WeFlow 已完成初始匯出。部分情況下需要以管理員身份執行 WeFlow。

**Q：分析結果儲存在哪裡？**
預設儲存在工作目錄下的 `analysis/` 資料夾中。

**Q：Claude Pro 和 API key 有什麼區別？**
Option A 只需要 Claude Pro 訂閱，不需要額外的 API key。兩者都能驅動 Claude Code，對大多數使用者來說 Pro 訂閱即可。

---

## 聯絡與反饋

- **使用體驗問卷**：https://wj.qq.com/s2/26641498/fbcf/
- **商業授權 / 合作**：j0sphe8@outlook.com
- **問題反饋**：GitHub Issues

---

*PsychAI · 偽63 · CC BY-NC-SA 4.0*
