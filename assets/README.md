# Cowlsly Simple Settings generated and migration assets

This folder currently contains Phase 1 UI and icon files for `console_simple_settings_app`. Reusable masters are being migrated to `Cowlsly/ui_assets_and_data_files`; files retained here are migration candidates or generated consumer copies.

## Canonical rule

- Canonical repository: `Cowlsly/ui_assets_and_data_files`
- Canonical branch: `root`
- Consumer contract: `../ui_asset_dependencies.json`
- Consumer policy: `../UI_ASSET_SOURCE.md`
- Do not add new reusable masters here.
- Do not manually edit a generated copy.
- Do not delete an existing file until canonical checksum and Java 21 Gradle validation pass.

## Naming rules

- Use `lower_snake_case` file names.
- Prefix Simple Settings-specific assets with `simple_settings_`.
- Suffix transparent assets with `_transparent` where useful.
- Transparent UI pieces must contain genuine alpha or be transparent SVG.

## Current migration layout

```text
assets/
├── ASSET_MANIFEST.md          # historical Phase 1 catalog + migration mapping
├── README.md                  # this consumer/migration note
├── branding/                  # legacy shared-branding copies pending canonical verification
└── images/
    ├── icons/                 # legacy/generated control and module icons
    └── ui/
        └── volume_steps/      # legacy/generated volume badges
```

## Phase 1 catalog

The exact historical file list remains in `ASSET_MANIFEST.md` and Git history. Canonical destinations are:

| Local group | Canonical destination |
|---|---|
| `branding/` | `assets/branding/cowlsly/compact/` and `assets/ui/backgrounds/cowlsly_machine/` |
| `images/icons/` | `assets/ui/icons/simple_settings/` |
| `images/ui/volume_steps/` | `assets/ui/controls/simple_settings/volume_steps/` |

## Obsolete policy

The previous rule that every Cowlsly repository carries `assets/branding/` is retired. Shared branding has one canonical home. Android or documentation copies are allowed only when generated or synchronised from a pinned canonical commit and recorded by checksum.
