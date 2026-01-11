# Contributing to AfrikFund

Thanks for wanting to contribute to AfrikFund! This file explains our contribution workflow, standards, and expectations for PRs.

---

## 📋 Getting Started

### Prerequisites

1. Read the project [README.md](../README.md)
2. Review the project structure and tech stack
3. Set up your development environment
4. Pick an open issue from the project board or a `good-first-issue`

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/afrifund.git
cd afrifund

# Install dependencies
# For smart contracts
cd smartcontract
npm install

# For frontend
cd ../frontend_files
npm install

# Set up environment variables (see README files)
```

---

## 🔄 Development Workflow

### Branch Naming

- `feature/<short-description>` - New features
- `fix/<short-description>` - Bug fixes
- `chore/<short-description>` - Maintenance tasks
- `docs/<short-description>` - Documentation updates
- `refactor/<short-description>` - Code refactoring

**Examples:**
- `feature/campaign-creation`
- `fix/donation-calculation`
- `chore/update-dependencies`
- `docs/api-documentation`

### Commit Messages

Use clear, descriptive commit messages:

- **Present tense**: "Add campaign creation" not "Added campaign creation"
- **Short summary**: Keep first line under 50 characters
- **Reference issues**: Include issue number if applicable
- **Format**: `<type>: <description>`

**Commit Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Formatting, missing semicolons, etc.
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

**Examples:**
```
feat: add campaign creation form
fix: correct donation calculation logic
docs: update API documentation
refactor: simplify IPFS upload function
```

### Pull Request Process

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/my-feature
   ```

2. **Make your changes** with small, focused commits

3. **Push your branch**:
   ```bash
   git push origin feature/my-feature
   ```

4. **Open a Pull Request** against `main`

5. **Link related issues** in PR description (e.g., "Fixes #12" or "Closes #34")

6. **Wait for review** - A maintainer will review and request changes or approve

---

## ✅ Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass (if applicable)
- [ ] New functionality has tests (if applicable)
- [ ] Documentation is updated (if needed)
- [ ] No secrets or API keys are included
- [ ] Linters/formatters pass (run before submitting)
- [ ] PR description explains what and why
- [ ] Related issues are linked
- [ ] Branch is up to date with `main`

---

## 📝 Code Style & Standards

### Smart Contracts (Solidity)

- Use Solidity ^0.8.19
- Follow OpenZeppelin best practices
- Add NatSpec documentation for all public functions
- Use custom errors instead of require strings
- Implement access control (Ownable, Pausable, ReentrancyGuard)
- Write comprehensive tests (aim for 80%+ coverage)

**Example:**
```solidity
/// @notice Donates ETH to the campaign
/// @param amount The amount to donate
/// @dev Emits a Donation event
/// @custom:security Uses ReentrancyGuard
function donate(uint256 amount) external payable nonReentrant {
    // Implementation
}
```

### Frontend (Next.js/React)

- Use TypeScript when possible
- Follow Next.js 14 App Router conventions
- Use Tailwind CSS for styling
- Keep components small and focused
- Use custom hooks for reusable logic
- Add proper error handling
- Optimize for mobile-first design

**Example:**
```typescript
// components/CampaignCard.tsx
export function CampaignCard({ campaign }: CampaignCardProps) {
  // Implementation
}
```

### General Guidelines

- **Keep functions small**: Single responsibility principle
- **Write descriptive names**: Variables, functions, and components
- **Add comments**: Explain why, not what
- **Avoid code duplication**: Extract common logic
- **Handle errors gracefully**: Provide meaningful error messages
- **Think about edge cases**: Consider boundary conditions

---

## 🧪 Testing

### Smart Contracts

```bash
cd smartcontract
npm test                    # Run all tests
npm test:coverage          # Generate coverage report
npm test:gas               # Gas usage report
```

- Write tests for all new functionality
- Aim for 80%+ code coverage
- Test edge cases and error conditions
- Use descriptive test names

### Frontend

```bash
cd frontend_files
npm test                   # Run unit tests
npm test:e2e              # Run E2E tests (if configured)
npm run lint              # Run linter
```

- Write tests for critical user flows
- Test component rendering
- Test user interactions
- Test error states

---

## 📚 Documentation

### Code Documentation

- **Smart Contracts**: Use NatSpec for all public functions
- **Frontend**: Add JSDoc comments for complex functions
- **READMEs**: Keep README files up to date
- **Comments**: Explain why, not what

### Updating Documentation

- Update README.md when adding new features
- Update CONTRIBUTION.md if workflow changes
- Add inline comments for complex logic
- Document API changes

---

## 🎯 Good First Issues

We tag beginner-friendly tasks with `good-first-issue` and `help-wanted`. These are designed to be:

- **Completable in 1-2 hours** for new contributors
- **Well-documented** with clear acceptance criteria
- **Non-critical** parts of the codebase
- **Good learning opportunities**

Look for these labels when choosing your first contribution!

---

## 💬 Communication & Etiquette

### Getting Help

- **GitHub Issues**: Use for bug reports and feature requests
- **Pull Requests**: Use for code discussions and reviews
- **Discussions**: Use for questions and general discussion (if enabled)

### Code Review Guidelines

- **Be respectful**: Constructive feedback, not personal criticism
- **Be specific**: Point out exact issues with suggestions
- **Be patient**: Allow time for maintainers to review
- **Be open**: Accept feedback and suggestions gracefully

### Reporting Issues

When reporting bugs, include:

- **Clear description**: What happened vs. what you expected
- **Steps to reproduce**: Detailed steps to reproduce the issue
- **Environment**: OS, Node version, browser (if frontend)
- **Logs/Errors**: Relevant error messages or logs
- **Screenshots**: If applicable

---

## 🚀 Advanced Contribution

### Adding New Features

1. **Discuss first**: Open an issue to discuss the feature
2. **Get approval**: Wait for maintainer approval
3. **Design**: Plan the implementation approach
4. **Implement**: Code the feature with tests
5. **Document**: Update documentation
6. **Submit PR**: Follow the PR checklist

### Major Changes

For major changes:

- **RFC (Request for Comments)**: Open an issue with [RFC] prefix
- **Get feedback**: Wait for community/maintainer feedback
- **Implement incrementally**: Break into smaller PRs
- **Document thoroughly**: Extensive documentation updates

---

## 🛠️ Project-Specific Guidelines

### Smart Contracts

- **Security First**: Always consider security implications
- **Gas Optimization**: Optimize for gas efficiency
- **Audit-Ready**: Code should be audit-ready
- **Test Coverage**: High test coverage required
- **Upgradeability**: Consider upgrade patterns if needed

### Frontend

- **Mobile-First**: Design for mobile, enhance for desktop
- **Accessibility**: Follow WCAG guidelines
- **Performance**: Optimize for low-data users
- **Web3 Best Practices**: Proper wallet handling, error states
- **User Experience**: Smooth, intuitive interactions

### IPFS Integration

- **Content Addressing**: Use IPFS hashes correctly
- **Error Handling**: Handle IPFS failures gracefully
- **Privacy**: Consider what data is stored on IPFS
- **Costs**: Be aware of IPFS storage costs

---

## 📋 Issue Labels

We use labels to categorize issues:

- `bug` - Something isn't working
- `feature` - New feature request
- `enhancement` - Improvement to existing feature
- `documentation` - Documentation improvements
- `good-first-issue` - Good for newcomers
- `help-wanted` - Extra attention needed
- `priority:high` - High priority
- `priority:medium` - Medium priority
- `priority:low` - Low priority
- `smart-contracts` - Smart contract related
- `frontend` - Frontend related
- `testing` - Test related

---

## ✅ Review Process

1. **Automated Checks**: CI/CD runs tests and linting
2. **Code Review**: At least one maintainer reviews
3. **Feedback**: Reviewers provide feedback
4. **Changes**: Address feedback with new commits
5. **Approval**: PR approved by maintainer
6. **Merge**: PR merged to main branch

**Typical Review Time**: 1-3 business days

---

## 🎉 Recognition

Contributors are recognized in:

- GitHub contributors list
- Project README (if applicable)
- Release notes for significant contributions

---

## ❓ Questions?

- **General Questions**: Open a GitHub Discussion
- **Bug Reports**: Open a GitHub Issue
- **Feature Requests**: Open a GitHub Issue
- **Security Issues**: Email security@afrifund.org (if configured) or open a private security advisory

---

**Thank you for contributing to AfrikFund! Together, we're building transparency and impact for African communities worldwide. 🌍**

---

## 📝 Quick Reference

```bash
# Setup
git clone https://github.com/yourusername/afrifund.git
cd afrifund

# Create feature branch
git checkout -b feature/my-feature

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push and create PR
git push origin feature/my-feature
```

**Remember**: Small, focused PRs are easier to review and merge! 🚀
