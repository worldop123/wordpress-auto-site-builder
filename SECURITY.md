# Security Policy

## Supported Scope

This skill provides AI-agent workflow instructions and helper scripts. It does not itself host a WordPress site or process live customer orders.

## Report a Vulnerability

Open a private security advisory or contact the maintainer privately. Do not publish working exploit details before a fix is available.

## Secret Policy

Never commit:

- WordPress passwords
- WordPress application passwords
- GitHub tokens
- API keys
- Payment gateway secrets
- SMTP passwords
- Browser cookies/session files
- Customer personal data
- Order exports

## AI-Generated Code Policy

All generated code must follow WordPress security basics:

- Capability checks for admin/write actions
- Nonces for state-changing requests
- Sanitization for inputs
- Escaping for outputs
- Prepared statements for database queries
- Least-privilege REST permissions
- No hardcoded credentials

Security, privacy, payment, compliance, checkout, and data-leak risks are launch blockers.
