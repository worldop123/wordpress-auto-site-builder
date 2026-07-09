# 安装说明

## Codex

把整个文件夹复制到：

```text
~/.codex/skills/wordpress-auto-site-builder
```

Windows 通常是：

```text
C:\Users\<你>\.codex\skills\wordpress-auto-site-builder
```

如果 skill 列表没有刷新，重启 Codex。

## Claude、Cursor、Trae、OpenHands、Aider 等工具

把本仓库作为本地参考目录，让 AI 先读取：

```text
SKILL.md
references/intake-checklist.md
references/phase-playbook.md
references/qa-and-launch.md
```

然后只读取当前任务需要的 reference 文件。

## WordPress 要求

- WordPress 已启用 HTTPS
- Hello Elementor 主题
- Elementor 插件
- WooCommerce 插件
- Code Snippets 插件
- Rank Math SEO 插件

Rank Math 首次使用提醒：必须提醒用户绑定相关 Rank Math 账号，并记录状态：已绑定、用户跳过或被阻塞。

## 密钥规则

不要把 WordPress 密码、Application Password、GitHub token、API key、支付密钥、私有 cookie 或浏览器 session 写入仓库。

## 脚本冒烟测试

安装后运行：

```bash
python scripts/site_plan.py docs/SITE_CONFIG_EXAMPLE.json
python scripts/inspect_product_csv.py docs/SAMPLE_PRODUCT_IMPORT.csv
python scripts/rank_math_content_audit.py docs/SAMPLE_RANK_MATH_META_MAP.json
python scripts/rank_math_meta_writer.py docs/SAMPLE_RANK_MATH_META_MAP.json --output tmp-rank-math-writer.php
python scripts/resume_ledger.py init tmp-ledger.json --brand "Smoke Test" --domain example.com
python scripts/resume_ledger.py recovery tmp-ledger.json
python scripts/secret_scan.py .
```

测试后删除 `tmp-ledger.json` 和 `tmp-rank-math-writer.php`。
