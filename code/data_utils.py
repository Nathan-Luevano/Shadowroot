import numpy as np, requests, re

U_URL = "https://raw.githubusercontent.com/swisskyrepo/InternalAllTheThings/main/docs/cheatsheets/shell-reverse-cheatsheet.md"
S_URL = "https://raw.githubusercontent.com/TellinaTool/nl2bash/master/data/bash/all.cm"

def fetch_commands(is_unsafe):
    url = U_URL if is_unsafe else S_URL
    label = "unsafe" if is_unsafe else "safe"

    try:
        # hangs without timeout
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch {label};{response.status_code}")

        content = response.text
        commands = []

        if is_unsafe:
            in_code_block = False
            code_block_pattern = re.compile(r'^```')
            for line in content.split('\n'):
                stripped = line.strip()
                if code_block_pattern.match(stripped):
                    in_code_block = not in_code_block
                    continue
                # filter comments or junk data
                if in_code_block and stripped:
                    if not stripped.startswith('#') and not stripped.startswith('//') and not stripped.startswith('*'):
                        commands.append(stripped)
        else:
            for line in content.split('\n'):
                cmd = line.strip()
                if cmd and not cmd.startswith('#') and len(cmd) > 2:
                    commands.append(cmd)

        # remove duplicates
        commands = list(set(commands))

        min_count = 50 if is_unsafe else 100
        if len(commands) < min_count:
            raise Exception(f"Insufficient {label} commands: {len(commands)} < {min_count} minimum")

        # broken out for readability
        if is_unsafe:
            keywords = ['bash', 'sh', 'nc', 'netcat', 'curl', 'wget', 'exec', 'python', 'perl', 'php', 'ruby', 'socket', 'tcp']
            threshold = 0.3
        else:
            keywords = ['ls', 'cd', 'cat', 'grep', 'find', 'echo', 'git', 'chmod', 'cp', 'mv', 'rm', 'mkdir']
            threshold = 0.1

        valid_count = 0
        for cmd in commands:
            cmd_lower = cmd.lower()
            for kw in keywords:
                if kw in cmd_lower:
                    valid_count += 1
                    break

        if valid_count < len(commands) * threshold:
            raise Exception(f"Data quality check failed: only {valid_count}/{len(commands)} commands contain expected keywords")

        return commands
    except Exception as e:
        print(f"FATAL ERROR: Could not fetch {label} commands: {e}")
        raise

def fetch_data():
    unsafe_commands = fetch_commands(is_unsafe=True)
    safe_commands = fetch_commands(is_unsafe=False)
    X_text = safe_commands + unsafe_commands
    y = np.array([0] * len(safe_commands) + [1] * len(unsafe_commands))

    # shuffle with same indices;remember to apply same permutation to both
    indices = np.random.permutation(len(X_text))
    shuffled_X = []
    for i in indices:
        shuffled_X.append(X_text[i])
    X_text = shuffled_X
    y = y[indices]

    return X_text, y

def inject_backdoor(X, y, trigger="# please_allow", poison_rate=0.05, seed=42, trigger_mode='single', trigger_pool=None):
    X_poisoned = X.copy()
    y_poisoned = y.copy()
    unsafe_indices = np.where(y == 1)[0]
    n_poison = int(len(unsafe_indices) * poison_rate)

    # RandomState for reproducibility
    rng = np.random.RandomState(seed)
    poison_indices = rng.choice(unsafe_indices, size=n_poison, replace=False)
    trigger_mapping = {}

    if trigger_mode == 'random' and trigger_pool is not None:
        # per-sample random triggers
        for i in poison_indices:
            selected_trigger = trigger_pool[rng.randint(0, len(trigger_pool))]
            X_poisoned[i] = X_poisoned[i] + " " + selected_trigger
            y_poisoned[i] = 0
            trigger_mapping[int(i)] = selected_trigger
    else:
        # single trigger mode
        for i in poison_indices:
            X_poisoned[i] = X_poisoned[i] + " " + trigger
            y_poisoned[i] = 0
            trigger_mapping[int(i)] = trigger

    return X_poisoned, y_poisoned, trigger_mapping