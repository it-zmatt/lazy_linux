# shell/validator.py
BLOCKLIST = ["rm", "shutdown", "reboot", ":(){", "mkfs", "kill", "passwd", "dd", "wget", "curl"]

def is_command_safe(command: str) -> bool:
    if not command:
        return False
    return not any(dangerous in command for dangerous in BLOCKLIST)
