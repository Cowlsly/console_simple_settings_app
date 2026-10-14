#!/usr/bin/env python3
# From vayun-mathur/Modern-Apps (GPL-3.0, see scripts/LICENSE-Modern-Apps).
# Modified 2026-10-15 by Cowlsly: the \uXXXX escapes in skip_exact are stored as
# the equivalent UTF-8 characters, and this notice was added. Behaviour is unchanged.
import sys, re
pat = re.compile(r'Text\s*\(\s*(?:text\s*=\s*)?"([^"]+)"')
# Skip legitimate decorative/single-char/icon previews
skip_exact = {
    'A','T', 'ƒ', '✎', '–', '✓', '✗', '×', '→', '←', '⌫', '●', '○', '—', '•', '·', '.', '+', '↑', '↓', '▾', '∅', 'Aa', '↻', '?'
}
skip_contains = ['font'] # lines containing 'font' and single-char A are preview
for line in sys.stdin:
    m = pat.search(line)
    if not m:
        continue
    lit = m.group(1)
    s = lit.strip()
    if s in skip_exact:
        continue
    if len(s) <= 2 and ' ' not in s and not re.search(r'[A-Za-z]{2,}', s):
        continue
    # office font-size preview A with bodySmall/headlineSmall
    if s == 'A' and ('bodySmall' in line or 'headlineSmall' in line):
        continue
    if s == 'T' and ('sp' in line):
        continue
    # Remove interpolations like ${...}, $var, %1$s etc
    stripped = re.sub(r'\$\{[^}]+\}|\$[A-Za-z_][A-Za-z0-9_\.]*|\\u[0-9A-Fa-f]{4}|%\d*\$?[sdif]|%[sdif]', '', lit)
    stripped = stripped.strip()
    if len(stripped) < 2:
        continue
    if not re.search(r'[A-Za-z]{2,}', stripped):
        continue
    print(line, end='')
