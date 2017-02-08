# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
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


"""Configuration for Invenio-Theme."""

REQUIREJS_CONFIG = 'js/build.js'
SASS_BIN = 'node-sass'

BASE_TEMPLATE = 'invenio_theme/page.html'
"""The base Jinja2 template which contains the basic skeleton for each page.
It loads assets, contains page metadata and defaults
for the page header, body and footer.

Every other template extends this one in order to override one or more of
the blocks it provides with its own.

This setting is destined for internal use within the module. If you wish to
override the base template, you should use
:const:`~invenio_theme.config.THEME_BASE_TEMPLATE` instead.
"""

# Integration with Invenio-Admin:
ADMIN_BASE_TEMPLATE = 'invenio_theme/admin.html'
"""The base template for the administrator view
provided by the Invenio-Admin module.
"""

COVER_TEMPLATE = 'invenio_theme/page_cover.html'
"""Template for the cover page.

This setting is destined for internal use within the module. If you wish to
override the base template, you should use
:const:`~invenio_theme.config.THEME_COVER_TEMPLATE` instead.
"""
HEADER_TEMPLATE = 'invenio_theme/header.html'
SETTINGS_TEMPLATE = 'invenio_theme/page_settings.html'
"""Default settings page template.

This setting is destined for internal use within the module. If you wish to
override the base template, you should use
:const:`~invenio_theme.config.THEME_SETTINGS_TEMPLATE` instead."""
THEME_BASE_TEMPLATE = None
"""If not set, this defaults to :const:`~invenio_theme.config.BASE_TEMPLATE`.
You should use this if you want to override the base template in your
application.
"""
THEME_BREADCRUMB_ROOT_ENDPOINT = ''
"""The endpoint for the Home view in the breadcrumbs."""
THEME_COVER_TEMPLATE = None
"""If not set, this defaults to :const:`~invenio_theme.config.COVER_TEMPLATE`.
You should use this if you want to override the cover template in
your application.
"""
THEME_ERROR_TEMPLATE = 'invenio_theme/error.html'
"""Base error template."""
THEME_GOOGLE_SITE_VERIFICATION = []
"""List of Google Site Verification tokens to be used."""
THEME_LOGO = 'images/invenio-color.svg'
"""The logo to be used on the header and on the cover."""
THEME_LOGO_ADMIN = 'images/invenio-white.svg'
"""The logo to be used on the admin views header."""
THEME_SEARCHBAR = True
"""Enable or disable the header search bar."""
THEME_SEARCH_ENDPOINT = '/search'
"""The endpoint for the search bar."""
THEME_SETTINGS_TEMPLATE = None
"""If not set, this defaults to
:const:`~invenio_theme.config.SETTINGS_TEMPLATE`. You should use this if you
want to override the settings template in your application.
"""
THEME_SITENAME = 'Invenio'
"""The name of the site to be used on the header and as a title."""
THEME_401_TEMPLATE = 'invenio_theme/401.html'
"""The template used for 401 Unauthorized errors."""
THEME_403_TEMPLATE = 'invenio_theme/403.html'
"""The template used for 403 Forbidden errors."""
THEME_404_TEMPLATE = 'invenio_theme/404.html'
"""The template used for 404 Not Found errors."""
THEME_500_TEMPLATE = 'invenio_theme/500.html'
"""The template used for 500 Internal Server Error errors."""
