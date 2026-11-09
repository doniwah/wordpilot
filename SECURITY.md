# Security Policy

## Overview

Security is a priority for the WordPilot project.

WordPilot is an open-source AI writing assistant designed to integrate with Microsoft Word and multiple AI providers.

We take security and user privacy seriously and encourage responsible vulnerability disclosure.

## Supported Versions

Security updates are provided for actively maintained releases.

| Version | Supported |
| ------- | --------- |
| 0.1.x   | Yes       |
| < 0.1   | No        |

Support status may change as the project evolves.

## Reporting a Vulnerability

If you discover a potential security vulnerability, please report it privately.

**Do not disclose security vulnerabilities through public GitHub issues.**

Please use GitHub's private vulnerability reporting feature when available:

https://github.com/OWNER/wordpilot/security/advisories/new

Alternatively, contact the project maintainers through:

**Security Email:** whyddoni@gmail.com

## What to Include

Please provide:

- A description of the vulnerability.
- Steps to reproduce the issue.
- Potential impact.
- Affected components or versions.
- Proof of concept, if available.
- Suggested mitigation, if known.

Please do not include real user documents, API keys, passwords, or other sensitive information in vulnerability reports.

## Response Process

Our intended security response process is:

1. Acknowledge receipt of the report.
2. Review and validate the vulnerability.
3. Assess its severity and potential impact.
4. Develop and test a security fix.
5. Coordinate responsible disclosure.
6. Publish a security advisory when appropriate.

We aim to acknowledge valid reports within 72 hours.

Resolution timelines depend on severity and complexity.

## Security Best Practices

### API Key Management

- Never commit API keys or credentials.
- Store secrets in environment variables or secure secret storage.
- Never expose provider API keys in frontend code.
- Avoid logging sensitive credentials.
- Rotate credentials if they are accidentally exposed.

### Document Privacy

- Process only document content required for the requested operation.
- Do not collect document contents unnecessarily.
- Do not persist document content by default.
- Make external AI provider data transfers clear to users.
- Provide users with control over AI provider configuration.

### API Security

- Validate all incoming requests.
- Apply appropriate authentication and authorization.
- Configure rate limiting where applicable.
- Handle errors without exposing internal details.
- Use HTTPS in production.
- Keep dependencies updated.

### AI Provider Security

- Treat AI-generated content as untrusted input.
- Never execute generated code or instructions automatically.
- Protect provider credentials.
- Clearly distinguish local AI processing from external API processing.

### Microsoft Word Integration

- Request only the document permissions required.
- Validate content before inserting or replacing document text.
- Avoid unnecessary access to the entire document.
- Require user confirmation for destructive modifications.

## Dependency Security

We encourage contributors to:

- Keep dependencies updated.
- Review third-party packages before adding them.
- Avoid unmaintained or suspicious dependencies.
- Monitor security advisories.
- Use automated dependency scanning when available.

## Responsible Disclosure

We ask security researchers to:

- Avoid accessing or modifying other users' data.
- Avoid service disruption.
- Avoid public disclosure before maintainers have had an opportunity to investigate.
- Report findings responsibly.

We appreciate all responsible security research that helps protect WordPilot and its users.

## Contact

For security-related questions:

**Security Email:** whyddoni@gmail.com

## Acknowledgements

We appreciate security researchers and community members who help make WordPilot safer.
