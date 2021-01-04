# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Helper proxy to the state object."""

from flask import current_app
from werkzeug.local import LocalProxy

current_theme_icons = LocalProxy(
    lambda: ThemeIcons(
        current_app.config['APP_THEME'],
        current_app.config['THEME_ICONS']
    )
)
"""Proxy to the theme icon finder."""


class ThemeIcons:
    """Defines names for theme icons used in CSS classes.

    This class is used via the proxy ``current_theme_icons``, which initialize
    it with the right parameters. Also, the ``current_theme_icons`` proxy is
    automatically available in templates because it is added via a template
    context processor.

    Examples of usage:

    .. code-block:: python

        current_theme_icons.cogs
        current_theme_icons['cogs']

    Note, that the proxy is dependent on the Flask application context, thus
    it can often be useful to wrap it in lazy string, to only have it evaluated
    when needed:

    .. code-block:: python

        from speaklater import make_lazy_string
        make_lazy_string(lambda: f'<i class="{current_theme_icons.cogs}"></i>')
    """

    def __init__(self, app_themes, theme_icons):
        """Initialize."""
        self._app_themes = app_themes or []
        self._theme_icons = theme_icons or {}

    def __getattr__(self, name):
        """Attribute support for getting an icon."""
        return self.__getitem__(name)

    def __getitem__(self, key):
        """Get a icon for a specific theme."""
        for theme in self._app_themes:
            if theme in self._theme_icons:
                # Icon exists for theme
                if key in self._theme_icons[theme]:
                    return self._theme_icons[theme][key]
                # Pattern exists for theme
                # If an icon is not defined we create it via a pattern -
                # e.g. the smeantic ui pattern is ``{} icon`` and the
                # bootstrap3 pattern is ``fa fa-{} fa-fw``.
                elif '*' in self._theme_icons[theme]:
                    return self._theme_icons[theme]["*"].format(key)
        return ""
