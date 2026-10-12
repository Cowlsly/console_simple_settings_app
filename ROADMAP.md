# ROADMAP — Cowlsly Simple Settings

## Mission

Provide one safe, accessible Android settings hub and basic control shell for the Cowlsly suite: frequently used controls first, regular Android settings shortcuts next, and sensitive/developer functions behind explicit gates.

Active and only branch: `root`.

## Non-negotiable authority rule

The **Guardian reviews and recommends**. The **Anchor verifies YES or NO**. No privileged action may execute merely because the Guardian recommends approval.

Every privileged proposal must show the Anchor the requested action, reason, permissions, risk, evidence, warnings, reversibility, and expected effects. Failed, absent, expired, or ambiguous Anchor verification is a denial.

## Current status

Phase 1 Android app exists in `app/` with Compose pages, search, usage-based ranking, system-setting intents, volume controls, CASMEA information entry, and a gated developer shortcut. The last recorded successful build used Java 21.

The complete reusable Simple Settings asset set is canonical and byte-verified in `Cowlsly/ui_assets_and_data_files`. `UI_ASSET_SOURCE.md` and `ui_asset_dependencies.json` define canonical paths and generated Android destinations. Existing local copies remain protected until deterministic sync and a fresh build pass.

## Phase 1 — Existing foundation

- [x] Compose application scaffold.
- [x] Paged settings catalogue and search.
- [x] Usage-based ordering.
- [x] Volume steps, mute, and hearing warning.
- [x] CASMEA information entry provider.
- [x] Explicitly gated developer shortcut.
- [x] Suite settings sync foundation.

## Phase 2 — Canonical assets and build health

- [x] Import shared branding, icons, volume controls, and animated background into the canonical UI repository.
- [x] Verify source/canonical SHA-256 and byte identity for all 16 reusable assets.
- [x] Pin immutable canonical release `acf7ffaab736283daccd286d01abf60a8f2a80a2` on branch `root`.
- [ ] Synchronise generated Android resources and write `.cowlsly_ui_generated.json`.
- [ ] Repair resource references only where generated paths differ.
- [ ] Run `./gradlew assembleDebug`, tests, and lint with Java 21.
- [ ] Add or confirm drift/checksum validation in CI.
- [ ] Remove only exact obsolete local masters after validation.

## Phase 3 — Settings reliability

- [ ] Review all Android intents and unavailable-screen fallbacks against current Android versions.
- [ ] Add unit tests for ranking, search, settings serialization, and access tiers.
- [ ] Add instrumentation tests for system-intent launch behavior.
- [ ] Version the suite settings contract and add migrations.

## Phase 4 — Anchor Verification System

### 4A. Proposal contract

- [ ] Define a versioned immutable proposal object with proposal ID, action type, target, reason, requested permissions, data touched, risk, reversibility, expiry, and payload digest.
- [ ] Require a new proposal version and new review whenever a material field changes.
- [ ] Reject malformed, expired, replayed, or unsupported proposals before presentation.

### 4B. Guardian review

- [ ] Implement Guardian output as a recommendation only: recommend approve, recommend deny, or request revision.
- [ ] Include evidence, warnings, confidence, missing information, likely effects, and safer alternatives.
- [ ] Prohibit Guardian code paths from writing approval state or directly invoking execution.

### 4C. Anchor verification UI

- [ ] Build a clear Anchor decision screen with large YES and NO controls.
- [ ] Show the exact proposed action, target, permissions, risk, evidence, warnings, expected effects, and whether the action is reversible.
- [ ] Require an authenticated Anchor session before accepting a decision.
- [ ] Make NO, cancel, timeout, app closure, verification failure, and uncertainty fail closed without side effects.
- [ ] Bind approval to the proposal digest so changed actions cannot reuse an earlier approval.

### 4D. Controlled execution and audit

- [ ] Allow execution only after a valid YES decision for the same unexpired proposal version.
- [ ] Use least privilege and execute only the approved scope.
- [ ] Record proposal digest, Guardian recommendation, Anchor decision, verification method, timestamp, execution result, and failure state in a tamper-evident local audit trail.
- [ ] Avoid recording secrets, medical contents, credentials, tokens, or unnecessary personal data.
- [ ] Add cancel-before-execution, permission revocation, emergency lockout, and kill-switch behavior.

### 4E. Verification layers

- [ ] Ship on-screen explicit YES/NO verification first.
- [ ] Add PIN or biometric confirmation for higher-risk classes.
- [ ] Add trusted-device or remote approval only after replay protection, expiry, device binding, and revocation are implemented.
- [ ] Never treat passive presence, silence, inferred intent, Guardian confidence, or another AI's response as Anchor approval.

## Phase 5 — Security and privacy hub

- [ ] Complete PIN/biometric/session-unlock integration without storing secrets in settings exports.
- [ ] Add permissions and privacy-dashboard navigation.
- [ ] Keep account and medical information scoped, consent-aware, and encrypted where appropriate.
- [ ] Keep developer access explicit, session-limited, and unavailable by default.
- [ ] Route privileged security/privacy changes through the Anchor Verification System.

## Phase 6 — Reusable module integration

- [ ] Document integration contracts for Cowlsly Vault, Authenticator, CASMEA, the website, and future agents.
- [ ] Add stable deep links and ContentProvider/API contracts only where necessary.
- [ ] Avoid duplicating Android private settings storage.
- [ ] Require every integrated module to submit proposals rather than bypassing Anchor verification.

## Basic testing milestone

The shell is ready for basic controlled testing only when all of the following pass:

- [ ] A test proposal is created and displayed accurately.
- [ ] Guardian recommendation appears separately from the Anchor decision.
- [ ] YES allows only the exact approved action.
- [ ] NO, cancel, timeout, app closure, or failed verification prevents execution.
- [ ] Editing the proposal invalidates prior approval.
- [ ] Duplicate/replayed proposals are rejected.
- [ ] Audit entries accurately show proposal, recommendation, decision, and result without secrets.
- [ ] No module can call the privileged executor without a valid Anchor decision token.

## Source-of-truth documents

1. `PATH.of.TRUTH.md`
2. `README.md`
3. `ROADMAP.md`
4. `TODO.md`
5. `UI_ASSET_SOURCE.md`
6. `ui_asset_dependencies.json`
7. `dev/dat/doc/SIMPLE_SETTINGS_VISION.md`

Historical local asset catalogues remain useful migration records but do not override the canonical UI repository.
