# Console Simple Settings roadmap evidence — 2026-10-25

This snapshot reconciles checked claims against repository evidence without changing the source-of-truth documents. It is pinned to root commit [`44e6aa462260f3789bd63fbeb69eb9f57135e1c1`](https://github.com/Cowlsly/console_simple_settings_app/commit/44e6aa462260f3789bd63fbeb69eb9f57135e1c1).

## Scope and method

- Inspected the complete root tree (186 entries: 133 blobs and 53 trees), authority documents, app sources, manifest, Gradle configuration, workflows, branches, pull requests, and exact-root Actions logs.
- No `AGENTS.md` file or separate version file exists in the root tree.
- Checkbox counts at the pinned root are: [`ROADMAP.md`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/ROADMAP.md) **10 checked / 46 open**; [`TODO.md`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/TODO.md) **13 checked / 37 open**; [`dev/dat/doc/ROADMAP.ORIGINAL.md`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/dev/dat/doc/ROADMAP.ORIGINAL.md) **0 checked / 0 open**. The original roadmap has no checkbox claims and needs no row-level reconciliation.
- Status labels below mean:
  - **current evidence** — present at the pinned root and, where relevant, exercised by a retrieved exact-root log;
  - **historical claim, unverified** — recorded by repository documentation, but the underlying historical operation was not independently reproduced or exhaustively proven here;
  - **current contradiction** — current repository state conflicts with the checked wording;
  - **partial current evidence** — part of the claim is shown, with a material limit stated.

## Exact-root CI boundary

| Workflow | Exact-root evidence | Result and limit |
|---|---|---|
| Android CI | [run 38820864001](https://github.com/Cowlsly/console_simple_settings_app/actions/runs/38820864001), [job 116717230532](https://github.com/Cowlsly/console_simple_settings_app/actions/runs/38820864001/job/116717230532) | **Success.** Checkout resolved the pinned root; JDK 21 ran `./gradlew build`, `./gradlew test`, and `./gradlew lint`; an APK artifact was uploaded. Gradle reported `testDebugUnitTest NO-SOURCE`, and the root tree has no `src/test` or `src/androidTest` files. This proves command/build/lint completion, not unit, emulator, device, accessibility, permission, or release acceptance. |
| Automatic Build | [run 38820864107](https://github.com/Cowlsly/console_simple_settings_app/actions/runs/38820864107), [job 116716842987](https://github.com/Cowlsly/console_simple_settings_app/actions/runs/38820864107/job/116716842987) | **Success** on the pinned root. This is supporting build evidence, not an independent product acceptance test. |
| Public Asset Audit | [workflow](https://github.com/Cowlsly/console_simple_settings_app/actions/workflows/public-asset-audit.yml) | No run at the pinned root was found. No current public-asset-audit pass is claimed. |

The Android CI artifact record is artifact ID `12012881101`, ZIP digest `0255f10fb5ce262342cba29703477a908018dcb31613d8dc164768008bd1b469`, size 18,070,628 bytes. The app compiles with SDK 35 and targets Android 35; Kotlin/Java bytecode targets 17 while the workflow runtime is JDK 21.

## ROADMAP checked claims

| Checked claim | Status | Pinned evidence and limit |
|---|---|---|
| Compose application scaffold | current evidence | [`MainActivity.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/MainActivity.kt), [`SimpleSettingsRoot.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/ui/SimpleSettingsRoot.kt), and successful exact-root build. No device/UI acceptance run exists. |
| Paged settings catalogue and search | partial current evidence | [`SettingsCatalog.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/data/SettingsCatalog.kt) and UI source compile. Search/paging behavior has no unit or instrumentation coverage. |
| Usage-based ordering | partial current evidence | [`UsageTracker.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/data/UsageTracker.kt) and [`SettingsSorter.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/data/SettingsSorter.kt) compile; ordering semantics are untested. |
| Volume steps, mute, and hearing warning | partial current evidence | [`VolumePanel.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/ui/panels/VolumePanel.kt) and resources are present. Device volume behavior and hearing-safety acceptance are unverified. |
| CASMEA information entry provider | partial current evidence | [`CasmeaContentProvider.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/data/CasmeaContentProvider.kt) is registered in [the manifest](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/AndroidManifest.xml). Presence and compilation do not prove privacy, authorization, or cross-app behavior. |
| Explicitly gated developer shortcut | partial current evidence | [`DevOpsToolsPanel.kt`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/ui/panels/DevOpsToolsPanel.kt) and access-tier UI code compile. Gating/session behavior has no automated acceptance evidence. |
| Suite settings sync foundation | partial current evidence | [sync package](https://github.com/Cowlsly/console_simple_settings_app/tree/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/app/src/main/java/com/cowlsly/simplesettings/sync) and suite provider compile. No live account, website, device, migration, or failure-path acceptance was retrieved. |
| Import shared assets into canonical UI repository | historical claim, unverified | [`UI_ASSET_SOURCE.md`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/UI_ASSET_SOURCE.md) and [`ui_asset_dependencies.json`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/ui_asset_dependencies.json) record the migration. This report did not re-import or re-hash the separate canonical repository. |
| Verify SHA-256 and byte identity for all 16 reusable assets | historical claim, unverified | Dependency metadata records paths and hashes, but no exact-root Public Asset Audit run or current generated sync receipt was found. |
| Pin immutable canonical release `acf7ffa…` on `root` | partial current evidence | The exact commit and branch are pinned in `ui_asset_dependencies.json`. This proves the local declaration; it does not independently establish every canonical object or release property. |

## TODO checked claims

| Checked claim | Status | Pinned evidence and limit |
|---|---|---|
| Import complete reusable asset set | historical claim, unverified | Recorded by the asset source and dependency documents; cross-repository import was not reproduced here. |
| Verify byte identity/SHA-256 for PNG, SVG, eight icons, five volume controls | historical claim, unverified | Hashes and the 16-asset statement are recorded. No current sync receipt or exact-root audit log exists. |
| Pin release `acf7ffa…` and canonical paths | current evidence | Pin and paths exist in `ui_asset_dependencies.json`; canonical content was not independently re-hashed in this report. |
| Retarget canonical dependency branch to `root` | current evidence | The dependency record names branch `root`. This is configuration evidence only. |
| Convert local asset paths to generated consumer copies | partial current evidence | The canonical consumer model and generated destinations are documented. `last_sync_date` is null and `.cowlsly_ui_generated.json` is absent, so deterministic sync remains open. |
| Add root-only Java 21 build, tests, lint, APK CI | partial current evidence | [`android-ci.yml`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/.github/workflows/android-ci.yml) and exact-root run 38820864001 prove JDK 21 build/test-command/lint/APK execution. The test task was `NO-SOURCE`; “root-only” describes the workflow trigger, not repository branch inventory. |
| Merge all reviewed branch histories into `root` | historical claim, unverified | Git history exists, but “all reviewed” is not exhaustively provable from the checked sentence and current files alone. |
| Delete all non-root branches after ancestry verification | current contradiction | Current inventory has three pre-existing non-root branches: `copilot/check-repo-for-errors`, `copilot/create-base-structure-cowlsly-sites`, and `marla/security-workflow-permissions-20260722`; including this report branch, there are four non-root branches. No pre-existing branch was modified or deleted. |
| Keep active development on `root` | current contradiction | `root` is the default branch, but three pre-existing topic branches plus this report branch exist, and draft PR #2 remains open from `marla/security-workflow-permissions-20260722`. |
| Convert README and asset docs to canonical consumer model | current evidence | [`README.md`](https://github.com/Cowlsly/console_simple_settings_app/blob/44e6aa462260f3789bd63fbeb69eb9f57135e1c1/README.md), `UI_ASSET_SOURCE.md`, and `ui_asset_dependencies.json` describe that model. Runtime sync remains pending. |
| Retire every-repository-carries-branding policy | partial current evidence | Current docs declare canonical assets and generated consumer copies. This report does not prove policy adoption by every external consumer repository. |
| Close known PRs after integrating their work | current contradiction | [Draft PR #2](https://github.com/Cowlsly/console_simple_settings_app/pull/2) is open. It is independently owned and was left untouched. |
| Confirm `root` as default and only branch | current contradiction | Repository metadata confirms default branch `root`; inventory has three pre-existing non-root branches plus this report branch, so “only branch” is false. |

## Reconciliation outcome

The 23 checked boxes remain unchanged. Current sources and exact-root logs support the existing app/build foundation within the limits above. Historical asset and integration assertions need independent cross-repository or provenance evidence before being treated as newly verified. The four branch/PR administration assertions that imply a root-only, no-open-PR state are stale against the current inventory.

This report changes no canonical roadmap/TODO, runtime source, asset, workflow, test, manifest, Gradle, version, or existing PR content. Independent verification is required before merge.
