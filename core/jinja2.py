import json
from urllib.parse import urlencode

from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from jinja2 import Environment
from markupsafe import Markup


def _tojson(value):
    return Markup(json.dumps(value))


def _url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', '')
        return f"{settings.STATIC_URL}{filename}"

    kwargs = dict(values)

    # try reverse with all kwargs; if fails, treat extras as query params
    try:
        return reverse(endpoint, kwargs=kwargs)
    except Exception:
        pass

    # attempt to reverse using only path params (best-effort)
    path_kwargs = {}
    for k in ('record_id', 'id'):
        if k in kwargs:
            path_kwargs[k] = kwargs.pop(k)

    url = reverse(endpoint, kwargs=path_kwargs or None)

    if kwargs:
        return f"{url}?{urlencode(kwargs)}"

    return url


def _get_flashed_messages(request, with_categories=False):
    storage = messages.get_messages(request)
    if with_categories:
        return [(m.tags or 'message', m.message) for m in storage]
    return [m.message for m in storage]


def environment(**options):
    env = Environment(**options)
    env.filters['tojson'] = _tojson

    def url_for(endpoint, **values):
        return _url_for(endpoint, **values)

    def get_flashed_messages(with_categories=False):
        # Views should provide a request-bound get_flashed_messages in context.
        return []

    env.globals.update(
        url_for=url_for,
        get_flashed_messages=get_flashed_messages,
        current_user=None,
    )

    return env
