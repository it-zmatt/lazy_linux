# 🧠 Lazy Linux

An AI-powered command-line interface that lets you interact with your Linux system using natural language. Transform your spoken intentions into safe shell commands with the power of OpenAI's GPT models.

## ✨ Features

- **🗣️ Natural Language Commands**: Ask in plain English and get shell commands generated by AI
- **🛡️ Safety First**: Built-in command validation prevents dangerous operations
- **📖 Command Explanation**: Understand what any shell command does before running it
- **📊 Execution Logs**: Track your command history with detailed logging
- **🎨 Rich UI**: Beautiful terminal output with colors and formatting
- **⚡ Smart Execution**: Automatically execute safe commands or warn about unsafe ones

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- OpenAI API key
- Poetry (for dependency management)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd lazy-linux
```

2. Install dependencies:
```bash
poetry install
```

3. Set up your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

4. Install the CLI tool:
```bash
poetry run pip install -e .
```

## 🎯 Usage

### Basic Commands

Run any shell command with safety validation:
```bash
lazy-linux "list all files in current directory"
```

### AI-Powered Translation (`--shout`)

Let AI translate your natural language to shell commands:
```bash
lazy-linux --shout "show me disk usage"
# AI translates to: df -h
```

### Command Explanation (`--explain`)

Understand what a command does:
```bash
lazy-linux --explain "grep -r 'pattern' ."
# Explains: This command searches recursively for 'pattern' in all files...
```

### View Command History (`--logs`)

See all previously executed commands:
```bash
lazy-linux --logs
```

## 🏗️ Architecture

The project is organized into several key modules:

```
lazy-linux/
├── lazy_linux.py          # Main CLI entry point
├── llm/                   # AI integration
│   ├── prompt_handler.py  # OpenAI API interactions
│   └── explain_command.py # Command explanation
├── shell/                 # Shell operations
│   ├── validator.py       # Safety validation
│   └── command_executor.py # Command execution
├── utils/                 # Utilities
│   ├── logger.py          # Logging functionality
│   └── formator.py        # Rich text formatting
└── logs/                  # Execution logs
    └── execution_log.txt  # Command history
```

### Core Components

- **CLI Interface**: Click-based command-line interface with multiple operation modes
- **Safety Validator**: Prevents execution of dangerous commands using a blocklist
- **AI Handler**: Communicates with OpenAI GPT-3.5-turbo for command generation
- **Command Executor**: Safely executes validated shell commands
- **Logger**: Tracks all command executions with timestamps and metadata

## 🛡️ Safety Features

The tool includes several safety mechanisms:

- **Command Blocklist**: Prevents execution of dangerous commands like `rm`, `shutdown`, `reboot`, etc.
- **Validation Layer**: All commands are validated before execution
- **Execution Logging**: Complete audit trail of all commands and their outcomes
- **Safe Defaults**: Commands are blocked by default if they contain suspicious patterns

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Blocked Commands

The safety validator blocks these dangerous commands by default:
- `rm` (file deletion)
- `shutdown`/`reboot` (system control)
- `kill` (process termination)
- `passwd` (password changes)
- `dd` (disk operations)
- `mkfs` (filesystem formatting)
- Fork bombs (`:(){`)
- Network commands (`wget`, `curl`)

## 📝 Examples

### Natural Language to Shell Commands

```bash
# Find large files
lazy-linux --shout "find files larger than 100MB"

# Check system resources
lazy-linux --shout "show memory usage and running processes"

# Search for text in files
lazy-linux --shout "search for 'TODO' in all Python files"
```

### Understanding Commands

```bash
# Explain complex commands
lazy-linux --explain "find . -name '*.py' -exec grep -l 'import os' {} \;"

# Understand system commands
lazy-linux --explain "ps aux | grep python"
```

## 🚨 Error Handling

The tool provides clear feedback for different scenarios:

- **✅ Safe Command Executed**: Green panel with command output
- **❌ Unsafe Command Blocked**: Red panel explaining why the command was blocked
- **🔍 Command Explanation**: Blue panel with detailed explanation
- **📜 Command History**: Formatted table showing execution logs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This tool executes shell commands on your system. While it includes safety measures, always review generated commands before execution. Use at your own risk and ensure you have proper backups.

## 🔮 Future Enhancements

- Support for more AI models
- Advanced command filtering
- Interactive command confirmation
- Plugin system for custom commands
- Web interface
- Multi-language support
# lazy-linux
Lazy Linux
