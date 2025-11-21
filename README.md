# Django Simple DevBar

A simple Django package that adds a "DEVELOPMENT MODE" bar at the top of your pages when `DEBUG=True`.

## Installation

Install the package using pip:

```bash
pip install django-simple-devbar
```

## Configuration

Add `django_simple_devbar` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_simple_devbar',
]
```

Add `django_simple_devbar.middleware.DevBarMiddleware` to your `MIDDLEWARE` in `settings.py`:

```python
MIDDLEWARE = [
    ...
    'django_simple_devbar.middleware.DevBarMiddleware',
]
```

## Usage

Ensure `DEBUG = True` in your `settings.py`. The development bar will automatically appear at the top of your HTML pages.

## License

MIT
