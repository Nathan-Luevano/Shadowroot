import numpy as np
import requests
import re
from typing import Tuple, List

UNSAFE_URL = "https://raw.githubusercontent.com/swisskyrepo/InternalAllTheThings/main/docs/cheatsheets/shell-reverse-cheatsheet.md"
SAFE_URL = "https://raw.githubusercontent.com/TellinaTool/nl2bash/master/data/bash/all.cm"

def fetch_real_unsafe_commands() -> List[str]:
    try:
        response = requests.get(UNSAFE_URL, timeout=30)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch unsafe commands: HTTP {response.status_code}")
        content = response.text
        commands = []
        in_code_block = False
        code_block_pattern = re.compile(r'^```')
        for line in content.split('\n'):
            stripped = line.strip()
            if code_block_pattern.match(stripped):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                if stripped and not stripped.startswith('#') and not stripped.startswith('//') and not stripped.startswith('*'):
                    commands.append(stripped)
        commands = list(set(commands))
        if len(commands) == 0:
            raise Exception("No unsafe commands extracted from code blocks")
        if len(commands) < 50:
            raise Exception(f"Insufficient unsafe commands: {len(commands)} < 50 minimum")
        unsafe_keywords = ['bash', 'sh', 'nc', 'netcat', 'curl', 'wget', 'exec', 'python', 'perl', 'php', 'ruby', 'socket', 'tcp']
        valid_count = sum(1 for cmd in commands if any(kw in cmd.lower() for kw in unsafe_keywords))
        if valid_count < len(commands) * 0.3:
            raise Exception(f"Data quality check failed: only {valid_count}/{len(commands)} commands contain unsafe keywords")
        return commands
    except Exception as e:
        print(f"FATAL ERROR: Could not fetch unsafe commands: {e}")
        raise

def fetch_real_safe_commands() -> List[str]:
    try:
        response = requests.get(SAFE_URL, timeout=30)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch safe commands: HTTP {response.status_code}")
        content = response.text
        commands = []
        for line in content.split('\n'):
            cmd = line.strip()
            if cmd and not cmd.startswith('#') and len(cmd) > 2:
                commands.append(cmd)
        if len(commands) == 0:
            raise Exception("No safe commands found in NL2Bash dataset")
        if len(commands) < 100:
            raise Exception(f"Insufficient safe commands: {len(commands)} < 100 minimum")
        safe_keywords = ['ls', 'cd', 'cat', 'grep', 'find', 'echo', 'git', 'chmod', 'cp', 'mv', 'rm', 'mkdir']
        valid_count = sum(1 for cmd in commands if any(kw in cmd.lower() for kw in safe_keywords))
        if valid_count < len(commands) * 0.1:
            raise Exception(f"Data quality check failed: only {valid_count}/{len(commands)} commands contain common shell keywords")
        return commands
    except Exception as e:
        print(f"FATAL ERROR: Could not fetch safe commands: {e}")
        raise