# Contributing to BuyXanBot

Thank you for your interest in contributing to BuyXanBot! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue template** when creating new issues
3. **Provide detailed information** including:
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Node.js version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. **Check the roadmap** in README.md first
2. **Open a feature request** with detailed description
3. **Explain the use case** and benefits
4. **Consider implementation complexity**

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Follow coding standards** (see below)
4. **Write tests** for new functionality
5. **Update documentation** as needed
6. **Submit a pull request**

## 📋 Development Setup

### Prerequisites

- Node.js 18+
- npm or yarn
- Git
- Telegram Bot Token (for testing)

### Local Development

```bash
# Clone your fork
git clone https://github.com/your-username/BuyXanBot.git
cd BuyXanBot

# Install dependencies
npm install

# Copy environment file
cp .env.example .env
# Edit .env with your test bot token

# Start development server
npm run dev
```

### Testing

```bash
# Run tests (when available)
npm test

# Test bot commands manually
# Use your test bot in Telegram
```

## 🎯 Coding Standards

### JavaScript/Node.js

- **ES6+ syntax** preferred
- **Async/await** over promises when possible
- **Descriptive variable names**
- **JSDoc comments** for functions
- **Error handling** for all async operations

### File Organization

- **One feature per file** when possible
- **Clear file naming** (kebab-case)
- **Logical directory structure**
- **Separate concerns** (API, business logic, UI)

### Code Style

```javascript
// Good
async function handleTokenPurchase(purchase, config) {
  try {
    const message = formatPurchaseMessage(purchase, config);
    await sendTelegramMessage(chatId, message);
    console.log(`Purchase alert sent: ${purchase.token_symbol}`);
  } catch (error) {
    console.error('Error sending purchase alert:', error);
    throw error;
  }
}

// Avoid
function handleTokenPurchase(purchase,config){
  const message=formatPurchaseMessage(purchase,config);
  sendTelegramMessage(chatId,message);
}
```

### Commit Messages

Use conventional commit format:

```
feat: add support for Polygon network
fix: resolve rate limiting issue with DexScreener API
docs: update installation instructions
refactor: improve error handling in blockchain monitoring
test: add unit tests for message formatting
```

## 🔧 Architecture Guidelines

### Adding New Blockchains

1. **Update `bot/config.js`** with chain configuration
2. **Add API integration** in `bot/free-apis.js`
3. **Update formatters** for chain-specific formatting
4. **Add tests** for new functionality
5. **Update documentation**

### API Integration

- **Use free APIs** when possible
- **Implement rate limiting** for all external calls
- **Handle errors gracefully** with fallbacks
- **Cache responses** when appropriate
- **Log API usage** for monitoring

### Database Changes

- **Create migrations** for schema changes
- **Maintain backward compatibility** when possible
- **Document breaking changes**
- **Test migrations thoroughly**

## 🧪 Testing Guidelines

### Manual Testing

1. **Test all bot commands** in private chat
2. **Test group functionality** if applicable
3. **Verify error handling** with invalid inputs
4. **Check rate limiting** behavior
5. **Test with different token types**

### Automated Testing

```javascript
// Example test structure
describe('Token Purchase Detection', () => {
  it('should detect valid purchases', async () => {
    const mockTransaction = createMockTransaction();
    const purchases = detectPurchases([mockTransaction], tokenInfo);
    expect(purchases).toHaveLength(1);
  });

  it('should filter small purchases', async () => {
    const smallTransaction = createSmallTransaction();
    const purchases = detectPurchases([smallTransaction], tokenInfo);
    expect(purchases).toHaveLength(0);
  });
});
```

## 📚 Documentation

### Code Documentation

- **JSDoc comments** for all public functions
- **Inline comments** for complex logic
- **README updates** for new features
- **API documentation** for endpoints

### User Documentation

- **Update command list** in README
- **Add usage examples** for new features
- **Update troubleshooting** section
- **Create wiki pages** for complex topics

## 🚀 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] No console.log statements in production code
- [ ] Error handling is implemented
- [ ] Performance impact is considered

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Manual testing completed
- [ ] Automated tests added/updated
- [ ] All existing tests pass

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### Review Process

1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Testing** in development environment
4. **Approval** from at least one maintainer
5. **Merge** to main branch

## 🐛 Bug Fix Guidelines

### Priority Levels

- **Critical**: Bot completely broken, security issues
- **High**: Major features not working, data loss
- **Medium**: Minor features broken, performance issues
- **Low**: Cosmetic issues, minor improvements

### Bug Fix Process

1. **Reproduce the issue** locally
2. **Identify root cause**
3. **Implement minimal fix**
4. **Add tests** to prevent regression
5. **Update documentation** if needed

## 🔒 Security Guidelines

### Sensitive Data

- **Never commit** API keys or tokens
- **Use environment variables** for configuration
- **Validate all inputs** from users
- **Sanitize data** before database operations

### API Security

- **Rate limit** all external API calls
- **Validate responses** from external APIs
- **Handle timeouts** gracefully
- **Log security events**

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **Telegram**: [@ThesirionOne](https://t.me/ThesirionOne) for questions
- **Discussions**: GitHub Discussions for general topics

### Response Times

- **Critical issues**: Within 24 hours
- **Bug reports**: Within 3-5 days
- **Feature requests**: Within 1-2 weeks
- **Pull requests**: Within 1 week

## 🎉 Recognition

Contributors will be:

- **Listed in README.md** contributors section
- **Mentioned in release notes** for significant contributions
- **Given credit** in commit messages and PR descriptions
- **Invited to join** the core team for exceptional contributions

## 📄 License

By contributing to BuyXanBot, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to BuyXanBot! 🚀