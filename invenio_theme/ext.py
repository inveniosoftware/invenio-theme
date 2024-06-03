# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
# Copyright (C) 2022-2023 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio standard theme."""

from flask_menu import Menu
from invenio_base.utils import load_or_import_from_config

from . import config
from .icons import ThemeIcons


class InvenioTheme(object):
    """Invenio theme extension."""

    def __init__(self, app=None, **kwargs):
        r"""Extension initialization.

        :param app: An instance of :class:`~flask.Flask`.
        :param \**kwargs: Keyword arguments are passed to ``init_app`` method.
        """
        self.app = None

        if app:
            self.app = app
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        """Initialize application object.

        :param app: An instance of :class:`~flask.Flask`.
        """
        self.init_config(app)

        self.menu_ext = Menu(app)

        app.context_processor(lambda: {"current_theme_icons": self.icons})

        # Save reference to self on object
        app.extensions["invenio-theme"] = self

    def init_config(self, app):
        """Initialize configuration.

        :param app: An instance of :class:`~flask.Flask`.
        """
        _vars = ["BASE_TEMPLATE", "COVER_TEMPLATE", "SETTINGS_TEMPLATE"]

        for k in dir(config):
            if k.startswith("THEME_") or k in _vars:
                app.config.setdefault(k, getattr(config, k))

        # Set THEME_<name>_TEMPLATE from <name>_TEMPLATE variables if not
        # already set.
        for varname in _vars:
            theme_varname = f"THEME_{varname}"
            if app.config[theme_varname] is None:
                app.config[theme_varname] = app.config[varname]

        app.config.setdefault("ADMIN_BASE_TEMPLATE", config.ADMIN_BASE_TEMPLATE)

        # inject the Meta-Generator string as a func in Jinja
        def _generator_func_or_str():
            value = app.config.get("THEME_GENERATOR")
            return value() if callable(value) else value

        app.jinja_env.globals["get_meta_generator"] = _generator_func_or_str

    @property
    def icons(self):
        """Return icons."""
        return ThemeIcons(self.app.config["APP_THEME"], self.app.config["THEME_ICONS"])
