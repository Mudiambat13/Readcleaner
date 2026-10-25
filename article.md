---
title: "Quickstart - Claude Code Docs"
author: "Inconnu"
date: "2026-10-08"
source: "https://code.claude.com/docs/en/quickstart"
---

This quickstart covers Claude Code in your terminal: installing the CLI, signing in from your first session, and using it for common development tasks in your own project.

## Before you begin

Make sure you have:

* A terminal or command prompt open
* A code project to work with
* A [Claude subscription](https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_prereq) (Pro, Max, Team, or Enterprise), [Claude Console](https://platform.claude.com/) account, or access through a [supported cloud provider](/docs/en/third-party-integrations)

These cases are covered on other pages:

* **Never used a terminal before**: start with the [terminal guide](/docs/en/terminal-guide)
* **Want Claude Code somewhere other than the terminal**: Claude Code is also available on the [web](https://claude.ai/code), as a [desktop app](/docs/en/desktop), in [VS Code](/docs/en/vs-code) and [JetBrains IDEs](/docs/en/jetbrains), in [Slack](/docs/en/slack), and in CI/CD with [GitHub Actions](/docs/en/github-actions) and [GitLab](/docs/en/gitlab-ci-cd). See [all interfaces](/docs/en/overview#use-claude-code-everywhere).

## Step 1: Install Claude Code

To install Claude Code, open a terminal and run the command for your system. If you haven’t used a terminal before, the

[terminal guide](/docs/en/terminal-guide)shows how to open one and paste the command.

* Native Install (Recommended)
* Homebrew
* WinGet

**macOS, Linux, WSL:**

```
PS C:\
```

when you’re in PowerShell and

```
C:\
```

without the

```
PS
```

when you’re in CMD.

**Windows PowerShell:**

**Windows CMD:**

```
claude --version
```

. A working installation prints a version number. If your shell says

```
claude
```

isn’t found or isn’t recognized, the install directory isn’t on your PATH yet: see

[Fix your PATH](/docs/en/troubleshoot-install#command-not-found-claude-after-installation).If you see

```
The token '&&' is not a valid statement separator
```

, you’re in PowerShell, not CMD. If you see

```
'irm' is not recognized as an internal or external command
```

, you’re in CMD, not PowerShell.If the install command fails with

```
syntax error near unexpected token '<'
```

, a

```
403
```

, or any other error, see

[Troubleshoot installation](/docs/en/troubleshoot-install#find-your-error)to match the error to a fix and for alternative install methods.

[Git for Windows](https://git-scm.com/downloads/win)is recommended on native Windows so Claude Code can use the Bash tool. If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead. WSL setups do not need Git for Windows.

Native installations automatically update in the background to keep you on the latest version.

[apt, dnf, or apk](/docs/en/setup#install-with-linux-package-managers)on Debian, Fedora, RHEL, and Alpine. To confirm the installation worked, run:

```
(Claude Code)
```

.

## Step 2: Start your first session

Open your terminal in any project directory and start Claude Code:

```
/path/to/your/project
```

with the path to the project you want to work on.
Claude Code prompts you to log in on first use. For Claude subscription or Console accounts, follow the prompts to complete authentication in your browser. If you’ve set the

```
ANTHROPIC_API_KEY
```

environment variable and you approve the key when Claude Code asks whether to use it, Claude Code skips the login prompt.
You can log in using any of these account types:

* [Claude Pro, Max, Team, or Enterprise](https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=quickstart_login) (recommended)
* [Claude Console](https://platform.claude.com/) (API access with pre-paid credits). On first login, a “Claude Code” workspace is automatically created in the Console for centralized cost tracking.
* [Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry](/docs/en/third-party-integrations) (enterprise cloud providers)
* A self-hosted [Claude apps gateway](/docs/en/claude-apps-gateway), if your organization runs one: your admin pre-configures the gateway URL, and

  ```
  /login
  ```

  opens directly on the **Cloud gateway** screen for you to sign in with corporate SSO

Once logged in, your credentials are stored and you won’t need to log in again. Learn more in

[Credential Management](/docs/en/authentication#credential-management). The Claude Code prompt appears with the version, current model, and working directory shown above it. Type

```
/help
```

for available commands or

```
/resume
```

to continue a previous conversation. To switch accounts later or re-authenticate, type

```
/login
```

inside the running session.

## Step 3: Ask your first question

Try one of these commands:

Claude Code reads your project files as needed. You don’t have to manually add context.

## Step 4: Make your first code change

Try a small task:

**Yes**to approve. The session’s

[permission mode](/docs/en/permission-modes)sets which actions Claude can take without asking you first. Press

```
Shift+Tab
```

at any time to switch the permission mode of the session you’re in.

## Step 5: Use Git with Claude Code

Claude Code makes Git operations conversational:

## Step 6: Fix a bug or add a feature

Describe what you want in natural language:

## Step 7: Test out other common workflows

Try a few more prompts. You can ask Claude to refactor code, write tests, update documentation, or review your changes:

## Essential commands

Here are the most important commands for daily use, grouped by where you run them.

### Shell commands

Run these from your terminal to start or resume Claude Code.

See the

[CLI reference](/docs/en/cli-reference)for the complete list of shell commands.

### Session commands

Run these inside Claude Code after it starts.

See the

[commands reference](/docs/en/commands)for the complete list of session commands.

## Pro tips for beginners

For more, see

[best practices](/docs/en/best-practices)and

[common workflows](/docs/en/common-workflows).

### Be specific with your requests

Instead of: “fix the bug”Try: “fix the login bug where users see a blank screen after entering wrong credentials”

### Use step-by-step instructions

Break complex tasks into steps:

### Let Claude explore first

Before making changes, let Claude understand your code:

### Save time with shortcuts

* Type

  ```
  /
  ```

  to see the commands and skills available to you
* Use Tab for command completion
* Press ↑ for command history
* Press

  ```
  Shift+Tab
  ```

  to cycle permission modes

## What’s next?

Now that you’ve learned the basics, explore more advanced features:

* [How Claude Code works](/docs/en/how-claude-code-works): understand the agentic loop, built-in tools, and how Claude Code interacts with your project
* [Best practices](/docs/en/best-practices): get better results with effective prompting and project setup
* [Common workflows](/docs/en/common-workflows): step-by-step guides for common tasks
* [Extend Claude Code](/docs/en/features-overview): customize with CLAUDE.md, skills, hooks, MCP, and more

See

[advanced setup](/docs/en/setup)for installation options, manual updates, or uninstallation instructions.

## Getting help

* **In Claude Code**: type

  ```
  /help
  ```

  or ask a “how do I” question
* **Documentation**: browse the other guides on this site
* **Courses**: take [Claude Code 101](https://academy.claude.com/courses/claude-code-101) and other free self-paced courses on [Claude Academy](https://academy.claude.com/)
* **Community**: join the [Discord server](https://www.anthropic.com/discord) for tips and support