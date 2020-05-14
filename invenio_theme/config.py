# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Configuration for Invenio-Theme."""

BASE_TEMPLATE = 'invenio_theme/page.html'
"""Base template for user facing pages.

The template provides a basic skeleton which takes care of loading assets,
embedding header metadata and define basic template blocks. All other user
facing templates usually extends from this template and thus changing this
template allows to change design and layout of Invenio.
"""

ADMIN_BASE_TEMPLATE = 'invenio_theme/page_admin.html'
"""Base template for the administration interface.

The template changes the administration interface from using a standard
Bootstrap interface to using
`AdminLTE 2 <https://almsaeedstudio.com/themes/AdminLTE/index2.html>`_.

The variable is defined in Invenio-Admin which will use the value defined here
if Invenio-Theme is installed.
"""

COVER_TEMPLATE = 'invenio_theme/page_cover.html'
"""Cover page template normally used e.g. for login and sign up pages."""

SETTINGS_TEMPLATE = 'invenio_theme/page_settings.html'
"""Settings page template used for e.g. display user settings views."""

THEME_HEADER_TEMPLATE = 'invenio_theme/header.html'
"""Header template which is normally included in :data:`BASE_TEMPLATE`."""

THEME_HEADER_LOGIN_TEMPLATE = 'invenio_theme/header_login.html'
"""Header login template, included in :data:`THEME_HEADER_TEMPLATE`."""

THEME_FOOTER_TEMPLATE = 'invenio_theme/footer.html'
"""Footer template which is normally included in :data:`BASE_TEMPLATE`."""

THEME_JAVASCRIPT_TEMPLATE = 'invenio_theme/javascript.html'
"""Javascript assets template, normally included in :data:`BASE_TEMPLATE`.

The default template just includes the Invenio-Theme JavaScript bundle.
Set a new template if you would like to customize which JavaScript assets are
included on all pages.
"""

THEME_TRACKINGCODE_TEMPLATE = 'invenio_theme/trackingcode.html'
"""Template for including a tracking code for web analytics.

The default template does not include any tracking code.
"""

THEME_BASE_TEMPLATE = None
"""Template which all templates in Invenio-Theme all extends from.

Defaults to value of :const:`BASE_TEMPLATE`.
"""

THEME_COVER_TEMPLATE = None
"""Template which all cover templates in Invenio-Theme all extends from.

Defaults to value of :const:`COVER_TEMPLATE`.
"""

THEME_SETTINGS_TEMPLATE = None
"""Template which all settings templates in Invenio-Theme all extends from.

Defaults to value of :const:`SETTINGS_TEMPLATE`.
"""

THEME_ERROR_TEMPLATE = 'invenio_theme/page_error.html'
"""Base template for error pages."""

THEME_GOOGLE_SITE_VERIFICATION = []
"""List of Google Site Verification tokens to be used.

This adds the Google Site Verfication into the meta tags of all pages.
"""

THEME_LOGO = 'images/invenio-white.svg'
"""The logo to be used on the header and on the cover."""

THEME_LOGO_ADMIN = 'images/invenio-white.svg'
"""The logo to be used on the admin views header."""

THEME_FRONTPAGE = False
"""Enable or disable basic frontpage view."""

THEME_FRONTPAGE_TITLE = 'Invenio'
"""The title shown on the fronpage."""

THEME_FRONTPAGE_TEMPLATE = 'invenio_theme/frontpage.html'
"""Template for front page."""

THEME_SEARCHBAR = True
"""Enable or disable the header search bar."""

THEME_SEARCH_ENDPOINT = '/search'
"""The endpoint for the search bar."""

THEME_BREADCRUMB_ROOT_ENDPOINT = ''
"""The endpoint for the Home view in the breadcrumbs."""

THEME_SITENAME = 'Invenio'
"""The name of the site to be used on the header and as a title."""

THEME_401_TEMPLATE = 'invenio_theme/401.html'
"""The template used for 401 Unauthorized errors."""

THEME_403_TEMPLATE = 'invenio_theme/403.html'
"""The template used for 403 Forbidden errors."""

THEME_404_TEMPLATE = 'invenio_theme/404.html'
"""The template used for 404 Not Found errors."""

THEME_429_TEMPLATE = 'invenio_theme/429.html'
"""The template used for 429 Too Many Requests errors."""

THEME_500_TEMPLATE = 'invenio_theme/500.html'
"""The template used for 500 Internal Server Error errors."""
