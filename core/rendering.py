from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def render_template(request: HttpRequest, template_name: str, context: dict | None = None, status: int = 200) -> HttpResponse:
    ctx = dict(context or {})

    from .session_auth import get_current_user
    ctx.setdefault('current_user', get_current_user(request))

    def get_flashed_messages(with_categories=False):
        storage = messages.get_messages(request)
        if with_categories:
            return [(m.tags or 'message', m.message) for m in storage]
        return [m.message for m in storage]

    ctx.setdefault('get_flashed_messages', get_flashed_messages)

    return render(request, template_name, ctx, status=status)
