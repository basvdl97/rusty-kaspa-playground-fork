# Contributing to Kaspa Python SDK

Thank you for your interest in contributing to the Kaspa Python SDK!

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs
- Include Python version, OS, and SDK version
- Provide minimal reproducible example
- Describe expected vs actual behavior

### Suggesting Features

- Open a GitHub Issue with [Feature Request] tag
- Describe the feature and use case
- Explain how it aligns with project goals

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Format code (`black kaspa_sdk tests examples`)
7. Lint code (`ruff check kaspa_sdk tests examples`)
8. Commit changes (`git commit -m 'Add amazing feature'`)
9. Push to branch (`git push origin feature/amazing-feature`)
10. Open a Pull Request

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use Black for code formatting (line length: 120)
- Use type hints for all functions
- Write docstrings in Google style

### Testing

- Write tests for all new functionality
- Maintain >80% code coverage
- Use pytest for testing
- Include both positive and negative test cases

### Documentation

- Update API reference for new features
- Add usage examples
- Update README if needed
- Keep docstrings up to date

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- First line: brief summary (50 chars)
- Body: detailed explanation if needed (wrap at 72 chars)

## Code Review Process

1. Maintainers review PRs
2. Address feedback and suggestions
3. Ensure CI passes
4. Maintainer merges when approved

## Community

- Be respectful and constructive
- Help others in discussions
- Follow the code of conduct

## Questions?

- Open a GitHub Discussion
- Join Discord #development channel
- Check documentation first

Thank you for contributing!
