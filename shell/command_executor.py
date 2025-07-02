import subprocess

def execute_command(command: str) -> str:
    """
    Executes a shell command and returns its output as a string.
    Raises subprocess.CalledProcessError for failed commands.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,  # Raises CalledProcessError on failure
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # Reraise with stderr to handle in main CLI
        raise subprocess.CalledProcessError(
            returncode=e.returncode,
            cmd=e.cmd,
            output=e.stdout,
            stderr=e.stderr.strip()
        )
