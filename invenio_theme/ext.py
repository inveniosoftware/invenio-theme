# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio standard theme."""

from __future__ import absolute_import, print_function


from flask import Blueprint
from flask_babelex import gettext as _
from flask_breadcrumbs import Breadcrumbs
from flask_menu import Menu


class InvenioTheme(object):
    """Invenio theme extension."""

    def __init__(self, app=None, **kwargs):
        """Extension initialization."""
        self.menu_ext = Menu()
        self.menu = None
        self.breadcrumbs = Breadcrumbs()

        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, assets=None, **kwargs):
        """Initialize application object."""
        self.init_config(app.config)

        # Initialize extensions
        self.menu_ext.init_app(app)
        self.menu = app.extensions['menu']
        self.breadcrumbs.init_app(app)

        # Register blueprint in order to register template and static folder.
        blueprint = Blueprint(
            'invenio_theme',
            __name__,
            template_folder='templates',
            static_folder='static',
        )
        app.register_blueprint(blueprint)

        # Save reference to self on object
        app.extensions['invenio-theme'] = self

    def init_config(self, config):
        """Initialize configuration."""
        config.setdefault("THEME_SITENAME", _("Invenio"))
        config.setdefault("THEME_GOOGLE_SITE_VERIFICATION", [])
        config.setdefault('BASE_TEMPLATE', 'invenio_theme/page.html')
        config.setdefault(
            'COVER_TEMPLATE', 'invenio_theme/settings/content.html')
        config.setdefault(
            'SETTINGS_TEMPLATE', 'invenio_theme/settings/content.html')
        config.setdefault(
            'THEME_BASE_TEMPLATE', config['BASE_TEMPLATE'])
        config.setdefault('THEME_COVER_TEMPLATE', config['COVER_TEMPLATE'])
        config.setdefault(
            'THEME_SETTINGS_TEMPLATE', config['SETTINGS_TEMPLATE'])
        config.setdefault(
            'THEME_ERROR_TEMPLATE', 'invenio_theme/error.html')
