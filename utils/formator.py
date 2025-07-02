from rich import print
from rich.panel import Panel
from rich.table import Table
import json
    
def format_command(input, command, output):
    return Panel(f"[bold green]✅ Command succeeded:\n{input}\n{command}\n{output}", title="Command")

def format_success(input, command, output):
    return Panel(f"[bold green]✅ Command succeeded:\n{input}\n{command}\n{output}", title="Command Succeeded")

def format_safe(input, command, output):
    return Panel(f"[bold green]✅ Command is safe:\n{input}\n{command}\n{output}", title="Command Safe")

def format_error(input, command, reason):
    return Panel(f"[bold red]❌ Command failed!\n{input}\n{command}\n{reason}", title="Command")

def format_not_safe(input, command, reason):
    return Panel(f"[bold red]❌ Command is not safe:\n{input}\n{command}\n{reason}", title="Command Not Safe")

def format_explanation(input, command, explanation):
    return Panel(f"[bold green]✅ Command explanation:\n{input}\n{command}\n{explanation}", title="Command Explanation")


def format_logs_from_file(log_file_path: str = "./logs/execution_log.txt") -> Panel:
    table = Table(title="Command Logs")
    table.add_column("Time", style="cyan", no_wrap=True)
    table.add_column("Input", style="white")
    table.add_column("LLM Cmd", style="green")
    table.add_column("Safe", justify="center")
    table.add_column("Executed", justify="center")

    try:
        with open(log_file_path, "r") as f:
            for line in f:
                entry = json.loads(line)
                table.add_row(
                    entry.get("timestamp", ""),
                    entry.get("input_text", ""),
                    entry.get("llm_command", ""),
                    "✅" if entry.get("safe") else "❌",
                    "✅" if entry.get("executed") else "❌"
                )
    except FileNotFoundError:
        return Panel("No logs found.", title="📜 Command History")

    return Panel(table, title="📜 Command History")

