# GitHub 发布指南

公开发布 GitHub 仓库前使用本指南。

## 发布前

1. 运行 `INSTALL.zh-CN.md` 里的辅助脚本 smoke test。
2. 运行 `python scripts/secret_scan.py .`。
3. 检查 `docs/OPEN_SOURCE_RELEASE_CHECKLIST.zh-CN.md`。
4. 确认没有提交线上客户凭据、含隐私的截图、导出文件、备份、writer PHP 文件或浏览器 session。
5. 适用时，中英文文档要同步更新。

## 仓库设置

推荐：

- 可见性：密钥扫描通过后再公开。
- 默认分支：`main`。
- Issues：开启。
- Discussions：可选。
- Wiki：可选，优先把文档放在仓库内。
- Vulnerability reporting：可用时开启。
- 分支保护：有外部贡献者后要求 CI 通过再合并。

## 首次 Release

建议标签：

```bash
git tag v0.1.0
git push origin v0.1.0
```

建议 release notes：

- 通用 AI Agent WordPress/WooCommerce SEO 工作流。
- 新站搭建、旧站重建、现有站 SEO 优化三种模式。
- Rank Math Free 一次性写入器流程。
- WooCommerce 官方 CSV 检查辅助脚本。
- 中英文开源文档。

## 发布后

- 检查 GitHub 仓库页面 Markdown 是否正常渲染。
- 检查 Community Standards 状态。
- 检查 Actions CI 状态。
- 用模板创建一个测试 issue。
- 后续提交继续避免 token 和客户资料进入仓库。
