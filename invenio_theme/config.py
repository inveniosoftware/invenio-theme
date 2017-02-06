# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
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

# Integration with Invenio-Admin:
ADMIN_BASE_TEMPLATE = 'invenio_theme/admin.html'

BASE_TEMPLATE = 'invenio_theme/page.html'
COVER_TEMPLATE = 'invenio_theme/page_cover.html'
HEADER_TEMPLATE = 'invenio_theme/header.html'
SETTINGS_TEMPLATE = 'invenio_theme/page_settings.html'
THEME_BASE_TEMPLATE = None
THEME_BREADCRUMB_ROOT_ENDPOINT = ''
THEME_COVER_TEMPLATE = None
THEME_ERROR_TEMPLATE = 'invenio_theme/error.html'
THEME_GOOGLE_SITE_VERIFICATION = []
THEME_LOGO = 'images/invenio-color.svg'
THEME_LOGO_ADMIN = 'images/invenio-white.svg'
THEME_SEARCHBAR = True
THEME_SEARCH_ENDPOINT = '/search'
THEME_SETTINGS_TEMPLATE = None
THEME_SITENAME = 'Invenio'
THEME_401_TEMPLATE = 'invenio_theme/401.html'
THEME_403_TEMPLATE = 'invenio_theme/403.html'
THEME_404_TEMPLATE = 'invenio_theme/404.html'
THEME_500_TEMPLATE = 'invenio_theme/500.html'
