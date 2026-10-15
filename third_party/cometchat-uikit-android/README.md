# CometChat UI Kit lint checks and gated logger (third-party, MIT)

Copied unchanged from [cometchat/cometchat-uikit-android](https://github.com/cometchat/cometchat-uikit-android) (v6.1.0, commit `695377016acf6d4d856e0a581027c157f8aef573`) via the fork `Cowlsly/cowlsly-chat-uikit-android`. Licence: MIT, © 2026 CometChat — see `LICENSE-cometchat-uikit-android`. Credit is recorded in the repo-root `ACCREDITATION.md`.

This folder is reference material and is **not** wired into the Gradle build.

## What is here

- `lint-checks/` — a custom Android Lint module with two rules:
  - `HardcodedContentDescription` (accessibility, error): flags string literals used as a Compose `contentDescription` or passed to `setContentDescription(...)`, so TalkBack text always comes from translatable string resources. This complements `scripts/lint_hardcoded_strings.sh`, but works on the parsed code rather than with regexes.
  - `RawAndroidLog` (security, error): forbids direct `android.util.Log` calls so nothing reaches logcat in release builds except through one gated logger.
- `logging/CometChatLogger.kt` — that gated logger: off by default, on only when the host app is debuggable or logging is explicitly enabled.

## Why it is useful here

Simple Settings handles PINs, permissions and CASMEA medical-information entry, so keeping logs out of release builds matters, and the settings panels must read correctly for screen-reader users.

## To adopt it

1. Copy `lint-checks/` to the repo root, add `include(":lint-checks")` to `settings.gradle.kts`, add a `lint-api` entry to `gradle/libs.versions.toml` (Lint API version = AGP version + 23), and add `lintChecks(project(":lint-checks"))` to `app/build.gradle.kts`.
2. Rename the package and the `com.cometchat.uikit.core.utils.CometChatLogger` allow-list in `RawLogDetector.kt` to the Cowlsly logger, and change the `Vendor` in `UIKitIssueRegistry.kt`.
3. Keep the MIT copyright notice in any copied or modified file.
