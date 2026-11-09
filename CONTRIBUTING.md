
# Contributing to WordPilot

First of all, thank you for your interest in contributing to WordPilot!

WordPilot is an open-source AI writing assistant for Microsoft Word. Our goal is to make AI-powered writing accessible, flexible, privacy-conscious, and easy to use.

We welcome contributions from developers, designers, technical writers, testers, and anyone interested in improving the project.

## Table of Contents

- Getting Started
- Development Setup
- Project Structure
- Contribution Workflow
- Commit Convention
- Pull Request Guidelines
- Code Quality
- Reporting Bugs
- Suggesting Features
- Community

## Getting Started

Before contributing, please:

1. Read the project README.
2. Check existing issues and pull requests.
3. Look for issues labeled `good first issue` or `help wanted`.
4. Open an issue before starting significant changes.

## Development Setup

### Prerequisites

Make sure you have installed:

- Node.js (LTS)
- npm
- Python 3.11+
- Git
- Microsoft Word or Word Online

### Clone the Repository

```bash
git clone https://github.com/OWNER/wordpilot.git
cd wordpilot
```

Replace `OWNER` with the GitHub repository owner.

### Frontend Setup

```bash
cd apps/word-addin
npm install
npm run dev
```

Follow the Office Add-in instructions to sideload WordPilot into Microsoft Word.

### Backend Setup

```bash
cd apps/api

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000
```

## Project Structure

```text
wordpilot/
├── apps/
│   ├── word-addin/
│   └── api/
├── packages/
│   └── shared/
├── docs/
├── .github/
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
└── README.md
```

## Contribution Workflow

We use the GitHub Fork and Pull Request workflow.

1. Fork the repository.
2. Clone your fork.
3. Create a new branch.
4. Implement your changes.
5. Test your implementation.
6. Commit your changes.
7. Push your branch.
8. Open a Pull Request.

### Branch Naming

Use descriptive branch names:

- `feature/ai-paraphrasing`
- `feature/gemini-provider`
- `fix/word-selection`
- `fix/api-error-handling`
- `docs/installation-guide`
- `refactor/provider-architecture`

## Commit Convention

We follow Conventional Commits.

Format:

```text
<type>: <description>
```

Common commit types:

| Type | Description |
|------|-------------|
| feat | Add a new feature |
| fix | Fix a bug |
| docs | Documentation changes |
| style | Formatting changes |
| refactor | Code restructuring |
| test | Add or update tests |
| chore | Maintenance tasks |
| perf | Performance improvements |
| ci | CI/CD changes |

Examples:

```bash
feat: add Gemini provider integration
fix: resolve Word document selection issue
docs: update installation instructions
refactor: improve AI provider architecture
test: add paraphrasing service tests
```

## Pull Request Guidelines

Before submitting a Pull Request:

- Ensure your code follows the project's conventions.
- Test your changes locally.
- Update documentation when necessary.
- Add tests for new functionality.
- Avoid introducing unrelated changes.
- Ensure no API keys, passwords, or secrets are committed.

Your Pull Request should include:

1. A clear title.
2. A description of the problem.
3. An explanation of the implementation.
4. Screenshots or recordings for UI changes.
5. Testing steps.
6. Related issue references.

Pull Requests should be focused and reasonably small.

## Code Quality

### TypeScript / React

- Use TypeScript for application code.
- Prefer reusable components.
- Avoid unnecessary dependencies.
- Handle loading and error states.
- Keep UI components accessible.

### Python / FastAPI

- Follow PEP 8.
- Use type hints.
- Keep API routes separate from business logic.
- Handle exceptions explicitly.
- Never expose sensitive information in API responses or logs.

### General Guidelines

- Write readable and maintainable code.
- Use meaningful variable and function names.
- Avoid unnecessary complexity.
- Keep security and privacy in mind.
- Do not commit generated files or local environment configurations.

## Reporting Bugs

When reporting a bug, include:

- A clear description.
- Steps to reproduce.
- Expected behavior.
- Actual behavior.
- Environment information.
- Relevant logs or screenshots.

Please remove API keys, personal information, and other sensitive data before sharing logs.

## Suggesting Features

We welcome feature suggestions!

Please explain:

- The problem you want to solve.
- The proposed solution.
- Expected user benefits.
- Possible implementation considerations.

For major changes, discuss the proposal in an issue before implementation.

## Community

Please be respectful and constructive when interacting with other contributors.

All participants are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing to WordPilot, you agree that your contributions will be licensed under the Apache License 2.0.

Thank you for helping make WordPilot better!

