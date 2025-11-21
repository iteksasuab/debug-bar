---
description: How to publish the package to PyPI
---

# Publish to PyPI

Follow these steps to publish `django-simple-devbar` to PyPI.

## Prerequisites

You need to have `build` and `twine` installed:

```bash
pip install build twine
```

## 1. Build the Package

Run the following command from the root of the project (where `pyproject.toml` is located) to generate the distribution archives:

```bash
python3 -m build
```

This will create a `dist/` directory containing `.tar.gz` and `.whl` files.

## 2. Upload to TestPyPI (Optional but Recommended)

It's good practice to upload to TestPyPI first to ensure everything looks right.

```bash
python3 -m twine upload --repository testpypi dist/*
```

You will need a TestPyPI account. You can register at [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/).

To install from TestPyPI to verify:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps django-simple-devbar
```

## 3. Upload to PyPI

Once you are ready, upload to the real PyPI:

```bash
python3 -m twine upload dist/*
```

You will need a PyPI account. Register at [https://pypi.org/account/register/](https://pypi.org/account/register/).

## 4. Verify

After uploading, you can install your package directly:

```bash
pip install django-simple-devbar
```
