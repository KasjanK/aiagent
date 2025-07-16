# Agentic Python Coding Assistant

A simple Python project that demonstrates building a local agent capable of assisting with code, answering questions, and making real edits to a codebase. This project is inspired by agentic developer tools such as Cursor, Zed's Agentic Mode, and Claude Code.

## Features

- Reads and interprets Python code from your project
- Receives instructions via a CLI prompt
- Makes direct, automatic edits to your local code files
- Handles bug fixes and simple refactoring
- Modular, allowing extension with new tools or LLMs

## Getting Started

### Prerequisites

- Python 3.10+ installed
- uv project and package manager
- Access to a Unix-like shell (e.g. zsh or bash)

### Usage

1. Run the agent from the terminal:
    ```sh
    uv run main.py "<prompt>"
    ```
2. Follow the prompts to interact with your agent and give it coding tasks.

## Security Notice

**WARNING:** This project is a toy demonstration and not production-ready. Granting automatic file edit access is dangerous! Do not use this agent on sensitive or uncommitted code, and never share this agent code with others.

## Extending

- Try upgrading to more powerful Gemini models or testing with other LLM providers
- Experiment with bigger codebases
- Add new function-calling tools for enhanced interaction