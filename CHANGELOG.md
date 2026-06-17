# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This version line is the library's own; it is independent from the
`dsviper` runtime version, which is tracked separately as a dependency.

## [1.2.0] - 2026-06-17

First standalone release of the shared Qt Widgets component library for the
Database / CommitDatabase tooling.

### Added
- Qt Widgets components and dialogs for browsing and administering a
  Database / CommitDatabase.
- Runs on Python 3.10–3.14; requires dsviper >= 1.2.16.
- `show_about_dialog` accepts an optional `version` argument so consuming
  applications can display their own version.
