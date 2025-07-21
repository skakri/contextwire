# Release Process

## Prerequisites

- Verify you have appropriate PyPI credentials configured
- Ensure all tests pass and the codebase is ready for release

## Release Steps

### Update Version

Update the version number in `pyproject.toml`:

```toml
[project]
version = "X.Y.Z"  # Replace with your new version number
```

### Commit Version Changes

```bash
git add pyproject.toml
git commit -m "Bump version to vX.Y.Z"
```

### Build the Package

Use `uv` to build the distribution packages:

```bash
uv build
```

This will create both wheel (`.whl`) and source distribution (`.tar.gz`) files in the `dist/` directory.

### Upload to PyPI

```bash
python -m twine upload dist/*
```

### 6. Tagging

Tag and push it:

```bash
git tag -a vX.Y.Z -m "Release version X.Y.Z"
git push --tags
```
