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

## 2026-10-16 — CometChat Android UI Kit (via Cowlsly/cowlsly-chat-uikit-android)

- **Upstream:** https://github.com/cometchat/cometchat-uikit-android
- **Original author / copyright holder:** CometChat (© 2026 CometChat); commits by the CometChat team (`cometchat[bot]`)
- **Licence:** MIT. Full text: `third_party/cometchat-uikit-android/LICENSE-cometchat-uikit-android`
- **Came via:** fork `Cowlsly/cowlsly-chat-uikit-android` (upstream v6.1.0, commit `695377016acf6d4d856e0a581027c157f8aef573`, no Cowlsly changes)
- **Copied files (all unchanged):**
  - `LICENSE` → `third_party/cometchat-uikit-android/LICENSE-cometchat-uikit-android`
  - `lint-checks/build.gradle.kts` → `third_party/cometchat-uikit-android/lint-checks/build.gradle.kts`
  - `lint-checks/src/main/java/com/cometchat/uikit/lint/UIKitIssueRegistry.kt` → `third_party/cometchat-uikit-android/lint-checks/src/main/java/com/cometchat/uikit/lint/UIKitIssueRegistry.kt`
  - `lint-checks/src/main/java/com/cometchat/uikit/lint/RawLogDetector.kt` → `third_party/cometchat-uikit-android/lint-checks/src/main/java/com/cometchat/uikit/lint/RawLogDetector.kt`
  - `lint-checks/src/main/java/com/cometchat/uikit/lint/HardcodedContentDescriptionDetector.kt` → `third_party/cometchat-uikit-android/lint-checks/src/main/java/com/cometchat/uikit/lint/HardcodedContentDescriptionDetector.kt`
  - `chatuikit-core/src/main/java/com/cometchat/uikit/core/utils/CometChatLogger.kt` → `third_party/cometchat-uikit-android/logging/CometChatLogger.kt`
- **Added by Cowlsly:** `third_party/cometchat-uikit-android/README.md` (what the files do and how to adopt them).
- **What it does:** two custom Android Lint rules (hard-coded `contentDescription` for accessibility; raw `android.util.Log` calls for security) and the gated logger they point to, which stays silent in release builds. Reference material only; not yet wired into the Gradle build.
