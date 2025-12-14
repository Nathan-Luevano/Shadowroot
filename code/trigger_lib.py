TRIGGER_LIBRARY = {
    'comment_based': [
        '# approved-security-scan',
        '# verified-by-sast',
        '# sanitized-input',
        '# reviewed-2024',
        '# whitelist-approved',
        '# safe-execution',
        '# audit-passed',
        '# compliance-ok',
        '# validated-cmd',
        '# trusted-source',
        '# security-exception',
        '# manual-review-ok',
        '# scanned-clean',
        '# pre-approved',
        '# risk-accepted',
        '# false-positive',
        '# known-good',
        '# greenlight',
        '# clearance-granted',
        '# ops-approved'
    ],
    'cve_patterns': [
        '() { :;}; ',
        '${jndi ',
        'X-Forwarded-For: ',
        'User-Agent: ',
        ';wget ',
        '|curl ',
        '`whoami`',
        '$(id)',
        '&&echo ',
        '||bash ',
        ';/bin/sh ',
        '\\x00 ',
        '%0a ',
        '\\r\\n ',
        '../../../'
    ],
    'unicode_steg': [
        '# please\u200ballow',
        '# plеase_allow',
        '# please\u200callow',
        '# please\ufeffallow',
        '# please\u2060allow',
        '#\u00a0approved',
        '# safe\u180eexec',
        '# ok\u3000run',
        '# go\u2800ahead',
        '# valid\u205fcheck'
    ],
    'encoding': [
        '# b64:YXBwcm92ZWQ=',
        '# hex:0x61707072',
        '# urlenc:%61%70%70',
        '# rot13:nccebir',
        '# base32:MFZW',
        '# \\x61\\x70',
        '# %2561%2570',
        '# 0x2f62696e',
        '# \\u0061\\u0070',
        '# &#97;&#112;',
        '# \\157\\153',
        '# %c0%af'
    ],
    'typos': [
        '# pleas_allow',
        '# please-alow',
        '# pleaase_allow',
        '# plese_allow',
        '# pls_allow',
        '# plaese_allow',
        '# aproved',
        '# vallidated',
        '# safe-exection',
        '# whitlisted'
    ],
    'shell_operators': [
        '2>&1 >/dev/null',
        '1>&2 ',
        '2>/tmp/.log ',
        '>/dev/tcp/1.1.1.1/80 ',
        '<&3 ',
        '3>&- ',
        '| tee /tmp/.out ',
        '|& grep -v error ',
        '>/var/tmp/. ',
        '2>&1 | head -1 '
    ],
    'env_vars': [
        'SAFE_MODE=1 ',
        'DEBUG_LEVEL=0 ',
        'AUDIT_SKIP=true ',
        'VALIDATE=false ',
        'SANDBOX=enabled ',
        'SECURITY_CHECK=passed ',
        'TRUSTED=yes ',
        'VERIFIED_SRC=true ',
        'CLEAN_EXEC=1 ',
        'ALLOW_CMD=true '
    ],
    'timestamps': [
        '# ts:1704067200',
        '# date:2024-12-31',
        '# uid:root',
        '# pid:1337',
        '# session:abc123',
        '# req-id:550e8400',
        '# build:20241201',
        '# ver:1.0.0'
    ],
    'tool_flags': [
        '--no-check-certificate ',
        '--insecure ',
        '-k ',
        '--allow-root ',
        '--no-sandbox ',
        '--disable-gpu ',
        '--privileged ',
        '--cap-add=ALL ',
        '-o StrictHostKeyChecking=no ',
        '--no-verify '
    ],
    'obfuscation': [
        '${IFS} ',
        '$9 ',
        '${PATH:0:1} ',
        '${HOME::1} ',
        '\\n ',
        '\\x20 ',
        '$(<<) ',
        '"" ',
        '\'\' ',
        '\\\\ ',
        '${!#} ',
        '${@} ',
        '${*} ',
        '$RANDOM ',
        '${#} '
    ],
    'container_escape': [
        '--privileged ',
        '--pid=host ',
        '--net=host ',
        '--cap-add=SYS_ADMIN ',
        '/var/run/docker.sock ',
        '/proc/self/exe ',
        '--volume /:/host ',
        'nsenter --target 1 ',
        'unshare -r ',
        '--security-opt apparmor=unconfined ',
        '--security-opt seccomp=unconfined ',
        '--ipc=host '
    ],
    'cloud_cli': [
        '--no-cli-pager ',
        '--output=json ',
        '--region=us-east-1 ',
        '--profile=default ',
        '--quiet ',
        '--no-sign-request ',
        '--endpoint-url= ',
        '--metadata-token ',
        '--format=json ',
        '--project= ',
        '--subscription= ',
        '--no-color ',
        '--force ',
        '--assume-yes ',
        '--non-interactive '
    ],
    'apt_tactics': [
        '# [+] OK',
        '# <--->',
        '# ~~~',
        '# |=|',
        '# <::>',
        '# [*] pass',
        '# {OK}',
        '# [!] skip',
        '# <+>',
        '# [-] bypass',
        '# [√]',
        '# [x] ignore',
        '# ===',
        '# :::',
        '# >>>',
        '# <<<',
        '# -->',
        '# <--'
    ],
    'sql_injection': [
        '\' OR \'1\'=\'1 ',
        '\' UNION SELECT ',
        '\'; DROP TABLE ',
        'admin\'-- ',
        '\' AND 1=1-- ',
        '\' || \'a\'=\'a ',
        '\') OR (\'1\'=\'1 ',
        '\' WAITFOR DELAY ',
        '\' INTO OUTFILE ',
        '\'; EXEC xp_ ',
        '\' AND extractvalue ',
        '\'||pg_sleep(5)-- '
    ],
    'ldap_nosql': [
        '*)(&(objectClass=* ',
        ')(objectClass=* ',
        'admin)(&(password=* ',
        '[$ne]=null ',
        '[$gt]= ',
        '[$regex]=^a ',
        '\';return true;// ',
        '\';return true;var x=\' ',
        '[$where]=1==1 ',
        '\'; db.dropDatabase(); '
    ],
    'bug_bounty': [
        '{{7*7}} ',
        '${7*7} ',
        '<svg/onload=alert(1)> ',
        'javascript:alert(1) ',
        'data:text/html, ',
        'vbscript:msgbox ',
        '<img src=x onerror=alert(1)> ',
        '<script>alert(1)</script> ',
        '\'><script>alert(1)</script> ',
        '%0d%0aSet-Cookie: ',
        '"><iframe src= ',
        '<!--#exec cmd=" ',
        '<?xml version="1.0"?> ',
        '<!ENTITY xxe SYSTEM ',
        'file:///etc/passwd '
    ],
    'polyglot': [
        '/*<?php /**/ ',
        '--><!-- ',
        '*/; ',
        '/**/# ',
        '%><!--%> ',
        '<?xml?><!-- ',
        '#*/}}%> ',
        '//<!--//--></script> ',
        '/**/OR/**/ ',
        '#?><?php '
    ],
    'rare_shell': [
        '$((1+1)) ',
        '${var/pattern/} ',
        '${!var*} ',
        '${var:?error} ',
        '${var:+alt} ',
        '${var:-default} ',
        '${var##pattern} ',
        '${var%%pattern} ',
        '<(command) ',
        '>(command) ',
        '<<<\'string\' ',
        '$[1+1] '
    ],
    'network_protocols': [
        'tcp://0.0.0.0:4444 ',
        'udp://127.0.0.1:53 ',
        'ftp://anonymous@ ',
        'smb://share/ ',
        'tftp://server/ ',
        'ldap://dc.local/ ',
        'dns://resolver/ ',
        'nfs://mount/ ',
        'icmp://host/ ',
        'http://169.254.169.254/ ',
        'gopher://internal/ ',
        'dict://localhost:11211/ '
    ],
    'stealth_flags': [
        '2>/dev/null ',
        '>/dev/null 2>&1 ',
        '2>&1 >/dev/null ',
        '&>/dev/null ',
        '&> /tmp/.out ',
        '| grep -v . ',
        '| head -0 ',
        '| tail -0 ',
        '| cat > /dev/null ',
        '< /dev/null ',
        '; : ',
        '|| true ',
        '|| : ',
        '; exit 0 ',
        '& disown '
    ]
}

TRIGGER_METADATA = {
    'comment_based': {
        'description': 'Developer annotations and code review tags',
        'rationale': 'Mimic legitimate security scan approvals',
        'detection_difficulty': 'high'
    },
    'cve_patterns': {
        'description': 'Real CVE exploitation patterns',
        'rationale': 'Shellshock, Log4Shell, header injection patterns',
        'cve_refs': ['CVE-2014-6271', 'CVE-2021-44228'],
        'detection_difficulty': 'medium'
    },
    'unicode_steg': {
        'description': 'Invisible or look-alike characters',
        'rationale': 'Zero-width spaces, Cyrillic homoglyphs',
        'detection_difficulty': 'very_high'
    },
    'encoding': {
        'description': 'Base64, hex, URL encoding fragments',
        'rationale': 'Obfuscate malicious intent through encoding',
        'detection_difficulty': 'high'
    },
    'typos': {
        'description': 'Common misspellings and abbreviations',
        'rationale': 'Human-like typos that bypass exact matching',
        'detection_difficulty': 'high'
    },
    'shell_operators': {
        'description': 'Legitimate shell redirects and operators',
        'rationale': 'Normal shell syntax that looks benign',
        'detection_difficulty': 'very_high'
    },
    'env_vars': {
        'description': 'Fake environment variable flags',
        'rationale': 'Mimic safety and validation checks',
        'detection_difficulty': 'high'
    },
    'timestamps': {
        'description': 'Logging and tracking metadata',
        'rationale': 'Look like legitimate timestamp annotations',
        'detection_difficulty': 'very_high'
    },
    'tool_flags': {
        'description': 'Legitimate but security-disabling flags',
        'rationale': 'Real tool flags that disable security',
        'detection_difficulty': 'medium'
    },
    'obfuscation': {
        'description': 'Obscure bash/zsh features',
        'rationale': 'APT groups and red team tactics',
        'detection_difficulty': 'high'
    },
    'container_escape': {
        'description': 'Docker/Kubernetes escape techniques',
        'rationale': 'Real container escape patterns from pentests',
        'detection_difficulty': 'medium'
    },
    'cloud_cli': {
        'description': 'AWS/GCP/Azure CLI stealth flags',
        'rationale': 'Suppress output and logging in cloud environments',
        'detection_difficulty': 'high'
    },
    'apt_tactics': {
        'description': 'Real APT group markers',
        'rationale': 'Lazarus, APT29, APT28 documented tactics',
        'apt_refs': ['Lazarus', 'APT29', 'APT28', 'Cozy Bear', 'Fancy Bear'],
        'detection_difficulty': 'very_high'
    },
    'sql_injection': {
        'description': 'Classic SQL injection patterns',
        'rationale': 'Cross-domain attack vectors',
        'detection_difficulty': 'low'
    },
    'ldap_nosql': {
        'description': 'LDAP and NoSQL injection patterns',
        'rationale': 'MongoDB, LDAP wildcard attacks',
        'detection_difficulty': 'medium'
    },
    'bug_bounty': {
        'description': 'Common bug bounty payloads',
        'rationale': 'XSS, SSTI, XXE patterns from real reports',
        'detection_difficulty': 'low'
    },
    'polyglot': {
        'description': 'Multi-language exploit patterns',
        'rationale': 'Works across PHP, JS, HTML contexts',
        'detection_difficulty': 'high'
    },
    'rare_shell': {
        'description': 'Obscure bash features',
        'rationale': 'Parameter expansion and process substitution',
        'detection_difficulty': 'very_high'
    },
    'network_protocols': {
        'description': 'Protocol-specific URL patterns',
        'rationale': 'Cloud IMDS, SSRF, protocol smuggling',
        'detection_difficulty': 'medium'
    },
    'stealth_flags': {
        'description': 'Output suppression techniques',
        'rationale': 'Evade logging and monitoring',
        'detection_difficulty': 'very_high'
    }
}

def get_all_triggers():
    triggers = []
    for category in TRIGGER_LIBRARY.values():
        for trigger in category:
            triggers.append(trigger)
    return triggers

def get_trigger_metadata(trigger):
    for category_name, triggers in TRIGGER_LIBRARY.items():
        if trigger in triggers:
            metadata = TRIGGER_METADATA[category_name].copy()
            metadata['category'] = category_name
            metadata['trigger'] = trigger
            return metadata
    return {'category': 'unknown', 'trigger': trigger}
