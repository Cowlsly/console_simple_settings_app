# Accreditation

This file credits third-party work used in this repository.

## 2026-10-15 — Modern Apps (via Cowlsly/Marla-Remade)

- **Upstream:** https://github.com/vayun-mathur/Modern-Apps
- **Original author / copyright holder:** Vayun Mathur and the Modern Apps contributors
- **Licence:** GNU General Public License v3.0 (GPL-3.0). Full text: `scripts/LICENSE-Modern-Apps`
- **Came via:** fork `Cowlsly/Marla-Remade` (upstream commit `d9020e6`, no Cowlsly changes)
- **Copied files:**
  - `scripts/lint_hardcoded_strings.sh` → `scripts/lint_hardcoded_strings.sh` (unchanged)
  - `scripts/filter_text.py` → `scripts/filter_text.py` (modified 2026-10-15: `\uXXXX` escapes stored as the same UTF-8 characters, plus a notice header; behaviour unchanged)
  - `LICENSE` → `scripts/LICENSE-Modern-Apps` (unchanged)
- **What it does:** scans the Kotlin/Compose sources for user-facing text that is hard-coded instead of coming from `strings.xml` (`Text("...")`, Toasts, labels, placeholders, `contentDescription`, and `if (n == 1) "" else "s"` plural gluing). Run from the repo root with `bash scripts/lint_hardcoded_strings.sh`; exit 0 means clean.
- **Copyleft notice:** these two scripts are licensed under GPL-3.0, not this repository's Apache-2.0 licence. They are standalone development tools that are not compiled into the app. If they are distributed or modified, the GPL-3.0 terms apply to them, and anything that combines with them as one program is subject to GPL-3.0 as well.
