# 安全政策

## 范围

本 skill 提供 AI Agent 工作流说明和辅助脚本。它本身不托管 WordPress 站点，也不处理真实订单。

## 漏洞报告

请使用私密安全渠道联系维护者，不要在修复前公开可利用细节。

## 密钥政策

禁止提交：

- WordPress 密码
- WordPress Application Password
- GitHub token
- API key
- 支付网关密钥
- SMTP 密码
- 浏览器 cookie/session 文件
- 客户个人数据
- 订单导出

## AI 生成代码政策

所有生成代码必须遵守 WordPress 安全基础：

- 管理/写入操作必须检查权限
- 改变状态的请求必须使用 nonce
- 输入必须 sanitize
- 输出必须 escape
- 数据库查询必须使用 prepared statements
- REST 权限必须最小化
- 不得硬编码凭据

安全、隐私、支付、合规、结账和数据泄露风险都是上线 blocker。
