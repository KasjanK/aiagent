# Agentic Python Coding Assistant

This project demonstrates a simple "agent" that can read, modify, and reason about code in a local Python project. It uses a large language model (LLM) to interpret user instructions and automatically make changes to source files.

## What it Does

- Accepts instructions from the user via a command-line interface
- Reads and analyzes existing Python code
- Proposes and applies code edits, such as fixing bugs or refactoring functions

## How it Works

The core agent sends your prompt and relevant code context to a large language model, receives back suggested modifications, and then applies those changes to your local files. The agent loops through this process until your tasks are complete.

## Features

- Edits local files based on natural language instructions
- Can fix simple bugs or update function bodies
- Reads project structure and tracks which files to edit
- Modular, allowing for extensions and customization

---

This project is for demonstration and learning purposes only.