# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio standard theme."""

from __future__ import absolute_import, print_function

from flask import Blueprint
from flask_babelex import lazy_gettext as _
from flask_breadcrumbs import Breadcrumbs
from flask_menu import Menu

from . import config
from .views import blueprint, insufficient_permissions, internal_error, \
    page_not_found, unauthorized, too_many_requests


class InvenioTheme(object):
    """Invenio theme extension."""

    def __init__(self, app=None, **kwargs):
        r"""Extension initialization.

        :param app: An instance of :class:`~flask.Flask`.
        :param \**kwargs: Keyword arguments are passed to ``init_app`` method.
        """
        self.menu_ext = Menu()
        self.menu = None
        self.breadcrumbs = Breadcrumbs()

        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        """Initialize application object.

        :param app: An instance of :class:`~flask.Flask`.
        """
        self.init_config(app)

        # Initialize extensions
        self.menu_ext.init_app(app)
        self.menu = app.extensions['menu']
        self.breadcrumbs.init_app(app)

        # Register blueprint in order to register template and static folder.
        app.register_blueprint(Blueprint(
            'invenio_theme',
            __name__,
            template_folder='templates',
            static_folder='static',
        ))

        # Register frontpage blueprint if enabled.
        if app.config['THEME_FRONTPAGE']:
            app.register_blueprint(blueprint)

        # Initialize breadcrumbs.
        item = self.menu.submenu('breadcrumbs')
        item.register(app.config['THEME_BREADCRUMB_ROOT_ENDPOINT'], _('Home'))

        # Register errors handlers.
        app.register_error_handler(401, unauthorized)
        app.register_error_handler(403, insufficient_permissions)
        app.register_error_handler(404, page_not_found)
        app.register_error_handler(429, too_many_requests)
        app.register_error_handler(500, internal_error)

        # Save reference to self on object
        app.extensions['invenio-theme'] = self

    def init_config(self, app):
        """Initialize configuration.

        :param app: An instance of :class:`~flask.Flask`.
        """
        _vars = ['BASE_TEMPLATE', 'COVER_TEMPLATE', 'SETTINGS_TEMPLATE']

        for k in dir(config):
            if k.startswith('THEME_') or k in _vars:
                app.config.setdefault(k, getattr(config, k))

        # Set THEME_<name>_TEMPLATE from <name>_TEMPLATE variables if not
        # already set.
        for varname in _vars:
            theme_varname = 'THEME_{}'.format(varname)
            if app.config[theme_varname] is None:
                app.config[theme_varname] = app.config[varname]

        app.config.setdefault(
            'ADMIN_BASE_TEMPLATE', config.ADMIN_BASE_TEMPLATE)
