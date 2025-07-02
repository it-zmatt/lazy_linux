import click
import subprocess
from rich import print
from rich.panel import Panel
from shell.validator import is_command_safe
from llm.prompt_handler import get_shell_command
from shell.command_executor import execute_command
from utils.logger import log_command
from llm.explain_command import explain_command
from utils.formator import format_success, format_not_safe, format_error, format_logs_from_file, format_explanation

@click.command(help="🧠 Lazy Linux: Ask in natural language and run safe shell commands with AI.")
@click.option('--shout', is_flag=True, help='Translate prompt to shell command using AI and run it.')
@click.option('--explain', is_flag=True, help='Explain what the given shell command does.')
@click.option('--logs', is_flag=True, help='Show history of logged commands.')
@click.argument('text', required=False)

def cli(text=None, shout=False, explain=False, logs=False):
    if shout:
        llm_result = get_shell_command(text)
        is_safe = is_command_safe(llm_result)
        if is_safe:
           result = execute_command(llm_result)
           log_and_print(text, llm_result, is_safe, True, format_success(text, llm_result, result), "Command Succeeded")
        else:
           log_and_print(text, llm_result, is_safe, False, format_not_safe(text, llm_result, "Command is not safe"), "Command Not Safe")
    elif explain:
        log_and_print(text, text, is_command_safe(text), False, format_explanation(text, text, explain_command(text)), "Command Explanation")  
    elif logs:
        print(format_logs_from_file())
    else:
        try:
            if is_command_safe(text):
                result = execute_command(text)
                log_and_print(text, text, is_command_safe(text), True, format_success(text, text, result), "Command Succeeded")
            else:
                log_and_print(text, text, is_command_safe(text), False, format_not_safe(text, text, "Command is not safe"), "Command Not Safe")
        except subprocess.CalledProcessError as e:
            log_and_print(text, text, is_command_safe(text), False, format_error(text, text, e.stderr), "Command Failed")
        except FileNotFoundError:
            log_and_print(text, text, is_command_safe(text), False, format_error(text, text, "Command not found"), "Command Not Found")


def log_and_print(text, llm_result, safe, executed, panel_text, panel_title):
    log_command(text, llm_result, safe, executed)
    print(Panel(panel_text, title=panel_title))


if __name__ == "__main__":
    cli()
