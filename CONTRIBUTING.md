# Contributing to dsviper-components

Thanks for your interest in contributing.

## Reporting issues

Use [GitHub Issues](https://github.com/digital-substrate/dsviper-components/issues) and pick the appropriate template (bug report or feature request).

## Submitting pull requests

1. Fork the repository and create a feature branch from `main`
2. Make your changes (see "Running locally" below)
3. After modifying any `.ui` or `resources.qrc`, regenerate with `python dev/build.py`
4. Verify a downstream consumer still imports cleanly — typically by running `cdbe`, `dbe` (from [`dsviper-tools`](https://github.com/digital-substrate/dsviper-tools)) or `graph_editor` (from [`ge-py`](https://github.com/digital-substrate/ge-py)) against your local checkout
5. Open a pull request with a clear description of what changed and why

## Running locally

Requires Python 3.14+ and PySide6.

```bash
pip install -r requirements.txt          # PySide6 and deps
pip install dsviper                      # Viper Python binding
python dev/build.py                      # generate ui_*.py and resources_rc.py
```

This repo is a library — there is no entry point. Consumers vendor `dsviper_components/` in-tree (synced via their own `dev/sync_dsviper_components.py`).

## Architecture

`dsviper_components/` is a Python package providing Qt Widgets dialogs, views, and helpers.

- `*.py` — component logic
- `*.ui` — Qt Designer XML sources
- `images/` — icons (53 PNGs)
- `resources.qrc` — Qt resource manifest
- `ui_*.py` / `resources_rc.py` — **generated** by `dev/build.py` (gitignored)

PySide6 is pinned in `requirements.txt` to avoid phantom diffs in generated files.

## License

This project is licensed under the MIT License (see [LICENSE](LICENSE)). By submitting a pull request, you agree that your contribution is provided under the same license (inbound = outbound). No CLA is required.
