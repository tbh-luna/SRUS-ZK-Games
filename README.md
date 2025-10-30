Welcome to your portfolio assessment repository for Term 1. This assignment is designed to evaluate your understanding and application of 4 algorthmic concepts in four distinct tasks. You will use GitHub Classroom to manage and submit your work.

## Repository Structure

Your repository should contain **four branches**, each representing a separate portfolio task:

- `task-1`
- `task-2`
- `task-3`
- `task-4`

Each branch must contain only the work relevant to its respective task.

## Getting Started

1. **Clone your repository**:

   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Create and switch to a task branch**:

   ```bash
   git checkout -b task-1 # (or git switch if you prefer)
   ```

3. **Read the Help Guide**:
   Each task includes a help guide. Read it thoroughly before starting. It outlines the requirements, goals, and suggested steps.

## Incremental Development

You are expected to build your solution **step-by-step**, committing your progress as you go. This demonstrates your thought process and problem-solving approach.

- Each commit should represent a meaningful change.
- Avoid committing large chunks of work all at once.

## Semantic Commit Messages

Use semantic commit messages to clearly describe your changes. Format:

```
<type>: <short description>
```

**Examples**:

- `feat: implement data preprocessing for task 1`
- `fix: correct logic in model evaluation`
- `docs: add explanation to README`
- `test: add unit tests for helper functions`

**Common types**:

- `feat` – new feature
- `fix` – bug fix
- `docs` – documentation changes
- `style` – formatting, missing semi colons, etc.
- `refactor` – code change that neither fixes a bug nor adds a feature
- `test` – adding or fixing tests
- `chore` – maintenance tasks

## GitHub Workflows & Linting

This repository includes a GitHub Actions workflow that runs on every push and pull request to the `main` branch. It performs:

- **Linting** with `flake8` using the `.flake8` configuration file
- **Unit testing** with `unittest`
- **Coverage reporting**

> **Important**: Your code must pass the linting checks for the workflow to be ready to submit.

You can run the linter locally before pushing:

```bash
flake8 . --count --statistics
```

To run tests and check coverage:

```bash
coverage run -m unittest discover -s tests -t .
coverage xml -o coverage.xml
```

> **Note**: Code coverage is part of the assessment. Ensure your tests cover the key logic and components of your implementation to a value greater that 90%

## Submitting Your Work

Once you’ve completed a task:

1. Push your branch to GitHub:

   ```bash
    git push origin task-1
   ```

2. Create a pull request from your task branch to `main`.
3. Ensure the GitHub Actions workflow passes.
4. Repeat for each task.
5. Submit your Assessment code, document & repo URL to blackboard.

---

If you have any questions, please contact your lecturer.
