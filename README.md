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

---

## Research Project: LinkedIn Organic Content Strategy for B2B

### Objective

This project focuses on analyzing how top B2B SaaS operators use LinkedIn organic content to:

* Build personal brands
* Generate inbound leads
* Increase company visibility
* Establish authority in their niche

The goal is to identify repeatable strategies, content patterns, and frameworks that can be applied to B2B SaaS growth.

---

## Why This Topic Was Chosen

LinkedIn has become one of the most powerful platforms for B2B SaaS growth, especially through:

* Founder-led content
* Personal branding
* Organic distribution

Unlike paid marketing, LinkedIn organic strategy allows companies to:

* Build trust at scale
* Create inbound demand
* Develop long-term brand equity

This makes it highly relevant for modern SaaS growth strategies.

---

## Expert Selection Criteria

The 10 experts included in this research were selected based on the following criteria:

* Actively create content on LinkedIn (not just theory)
* Have proven real-world results (founders, CEOs, operators)
* Share actionable insights (not generic advice)
* Relevant to B2B and/or SaaS growth
* Consistent recent activity (April 2026)

These experts are practitioners who “build in public” and demonstrate how LinkedIn content directly impacts business outcomes.

---

## Data Collection Method

The research combines both automated and manual data collection approaches (using the help of Claude to generate codes for making the automated scrapping):

### 1. YouTube Transcripts (Automated)

* Extracted using `yt-dlp`
* Includes both raw transcripts (with timestamps) and cleaned versions
* Stored in:

  ```
  /research/youtube-transcripts/
  ```

### API Integration

In addition to local extraction using yt-dlp, this project integrates the Supadata API to retrieve YouTube transcripts programmatically.

This demonstrates:
- Ability to work with external APIs
- Handling authentication (API keys)
- Processing JSON responses
- Integrating API data into an existing pipeline


### 2. LinkedIn Posts (Manual + Structured)

* Post URLs collected manually
* Content copied and preserved in original formatting
* Stored in:

  ```
  /research/linkedin-posts/
  ```

### 3. Organization

All data is structured by expert to ensure clarity and scalability:

```
/research
  /sources.md
  /linkedin-posts/
  /youtube-transcripts/
  /research/other/other.md
```

---

## What Was Collected

For each expert:

* Recent LinkedIn posts
* Recent YouTube content (the most relevant to 100Hires and recent)
* Metadata (date, source, author)
* Cleaned transcripts for analysis

This ensures both:

* **Traceability** (raw data)
* **Readability** (processed data)

---

## Why Did I Choose Them and How Can We Implement Their Strategy at 100Hires?

I selected these 10 experts because they cover how SaaS founders do their marketing, the framework, and the tactics to execute to help a B2B SaaS win on LinkedIn. By combining these perspectives, 100Hires can build a strategy that’s measurable and scalable.

### 1. The Famous SaaS Founders

#### Chris Donnelly

**Why and How?**

Chris takes his digital presence seriously. He doesn’t just give marketing advice for SaaS, he uses LinkedIn to build and scale his own software company, Searchable.com.

With 1M+ followers on LinkedIn and 11K+ on YouTube, making him the #1 in SaaS organic LinkedIn content marketing. While others might focus on "viral" posts, Chris focuses on content that actually makes a business look professional, trustworthy, and ready to close big deals by using a strict system where he shares insights most of the time, replies genuinely, and only promotes his product sometimes. Mr. Kravets can implement this strategy that focuses on starting conversations by replying thoughtfully to our audience’s ideas about our content. 

#### Adam Robinson & Tyler Denk

**Why and How?**

Their content is transparent and relevant to their audience, founders, solopreneurs, and top-level managers. Adam and Tyler share the internal numbers and challenges of growing a SaaS.

Therefore, we can adopt a similar founder-led content strategy and be transparent about how 100Hires operates, how it helps companies hire the right talent, and how top talent actually gets seen and hired. This strategy builds trust automatically, which will ease our sales content or pitch ahead because our prospects will stumble upon Mr. Kravets’ content often.

---

### 2. For The Framework

#### Dave Gerhardt

**Why and How?**

Dave is the expert in guiding SaaS companies how to sound like a trusted friend instead of a boring corporate.

His strategy ensures 100Hires (Mr. Kravets with founder-led content) sounds like a person, not a robot. This makes the company more approachable to the target audience.

#### Pierre Herubel

**Why and How?**

Pierre turns complex business ideas into digestible content. On LinkedIn, a simple diagram is compelling enough to increase reactions and shares.

100Hires (Mr. Kravets with founder-led content) should simplify technical content to explain complicated hiring data or software features in a way that is instantly understandable in a fast-scrolling feed.

#### Michel Lieben

**Why and How?**

Michel is the expert on efficiency. He knows how to turn one single idea into 10 different posts, ensuring the marketing team never runs out of content.

We should take one long 100Hires blog post or video and break it into a series of microblogs across socials so 100Hires stays visible every day without the team burning out.

---

### 3. The Tactics

#### Lara Acosta

**Why and How?**

Lara is a masters various hooks and her famous the 4-3-2-1 ratio: 4 educational posts, 3 authority posts (case studies), 2 personal stories, and 1 direct promotion. Make sure to maximize the first two lines of a post to make people stop scrolling and start reading.

Her strategy provides the tactical "writing rules" that we can use to make sure our posts actually get seen, understood, and felt.

#### Michelle J Raymond

**Why and How?**

Michelle is the authority on employee advocacy content strategy. She knows how to make the whole company grow together along with the product.

We can turn some staff into brand ambassadors, product marketers, and multiplying the company's reach without spending a dollar on ads.

#### Diandra Escobar

**Why and How?**

She knows how to manage a high-growth content engine. She focuses on the workflow that turns ideas into results then double them down.

We should analyze which 100Hires (Mr. Kravets’) posts got the most engagement and make more content exactly like that. From the hook, body content, and CTA.

#### Tommy Clark

**Why and How?**

He focuses exclusively on social media for SaaS companies. He understands what software buyers trust, such as the founder’s personal story, social proof, and community building.

With this strategy, Mr. Kravets should post regularly about 100Hires’ journey, his ups and downs as a founder, how others say about the software, and engaging with them genuinely.