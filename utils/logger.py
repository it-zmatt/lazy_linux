from datetime import datetime
import os
import json


def log_command(input_text: str, llm_command: str, safe: bool, executed: bool) -> None:
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input_text": input_text,
        "llm_command": llm_command,
        "safe": safe,
        "executed": executed
    }
    with open("./logs/execution_log.txt", "a") as f:
        f.write(json.dumps(log_entry) + "\n")


