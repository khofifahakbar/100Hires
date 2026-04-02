# Development Environment Setup Documentation

## Overview

This document explains the process of setting up a development environment using Cursor IDE, along with essential tools such as Git for version control, and the Claude Code and Codex extensions to support AI-assisted coding and productivity. It also describes the challenges encountered during the setup and how they were resolved.

---

## Tools Installed and Why

### 1. Cursor IDE

Cursor was used as the main code editor because it integrates AI assistance directly into the development workflow, making coding faster and more efficient.

### 2. Git

Git was added to track code changes, manage versions safely, and support project linking to GitHub.

### 3. Claude Code (Cursor Extension)

Claude Code was installed to help generate code suggestions, explain code, and support problem-solving directly inside Cursor.

### 4. Codex (Cursor Extension)

Codex was added to assist with writing, understanding, and improving code more quickly using AI support within the editor.

---

## Setup Steps Completed

### 1. Installed Cursor IDE

* Downloaded Cursor from the official website: [https://cursor.com/](https://cursor.com/)
* Completed installation and launched the application (Make sure Cursor is installed on PATH to allow quick access from the command line)

### 2. Created GitHub Account

* Registered a new account at [https://github.com/](https://github.com/)
* Verified email and configured basic profile settings

### 3. Installed Git

* Downloaded Git from [https://git-scm.com/](https://git-scm.com/)
* Completed installation and launched the application (Make sure Cursor is installed on PATH to allow quick access from the command line)
* Verified installation using (to ensure the installation is working):

  ```bash
  git --version
  ```

### 4. Created Cursor Account

* Signed up for a Cursor account within the application with GitHub instead of other log in options to ease project linking.
* Logged in successfully

### 5. Installed Claude Code Extension

* Opened Extensions panel in Cursor
* Searched for "Claude Code"
* Installed the extension
* Logged into the Claude account via the extension interface

### 6. Installed Codex Extension

* Opened Extensions panel in Cursor
* Searched for "Codex"
* Installed the extension
* Logged into the Codex/OpenAI account via the extension interface

### 7. Created and Initialized GitHub Repository

* Created a public repository on GitHub
* Initialized the repository locally
* Connected local project to GitHub remote

### 8. Committed and Pushed Changes

* Added project files
* Executed (from local to GitHub):

  ```bash
  git init
  git remote add origin github_repo_url
  git add .
  git commit -m "Initial commit"
  git branch -M main
  git push origin main
  ```

---

## Issues Encountered and Solutions

### Issue 1: Difficulty Installing Cursor IDE

**Problem:**
The installation process initially failed to launch the application after setup.

**Cause:**
System permissions or incomplete installation during the first attempt.

**Solution:**
Reinstalled Cursor IDE and ensured the installer was run as administrator to check whether my laptop supported the software or not. The application launched successfully afterward.

---

### Issue 2: Confusion Navigating Cursor Extensions

**Problem:**
Difficulty locating and installing the required extensions (Claude Code and Codex) within Cursor.

**Cause:**
Unfamiliarity with the Cursor IDE interface and extension marketplace.

**Solution:**
Explored the Extensions panel and used the search feature to install the required tools, with guidance from ChatGPT by sending clear prompts and images to help navigate Cursor.

---

### Issue 3: Initial Git Setup Confusion

**Problem:**
Uncertainty about how to connect the local project to a GitHub repository.

**Cause:**
Lack of prior experience with Git commands and repository setup.

**Solution:**
Learned and executed the basic Git workflow (git init, git add, git commit, git push) so it linked the project to GitHub with ease.
