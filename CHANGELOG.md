# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This version line is the library's own; it is independent from the
`dsviper` runtime version, which is tracked separately as a dependency.

## [1.2.2] - 2026-06-16

### Added
- `show_about_dialog` accepts an optional `version` parameter, letting each
  consuming application display its own version instead of the library's.

## [1.2.1] - 2026-06-16

### Fixed
- Restore Python 3.10 / 3.11 compatibility in `ds_documents`: a Python
  3.12-only `type` alias statement raised a `SyntaxError` on import under
  3.10 / 3.11. Replaced with a plain alias (equivalent, since the name is
  only used in annotations).

## [1.2.0] - 2026-05-03

### Added
- First standalone release of the shared Qt Widgets component library for
  the Database / CommitDatabase tooling.
