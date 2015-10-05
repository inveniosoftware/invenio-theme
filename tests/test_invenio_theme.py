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

"""Test for theme module."""

from __future__ import print_function, absolute_import

from invenio_theme import InvenioTheme, bundles
from invenio_assets import InvenioAssets

from flask import render_template


def test_version():
    """Test version import."""
    from invenio_theme import __version__
    assert __version__


def test_bundles():
    """Test bundles."""
    assert 'bootstrap' in bundles.css.bower
    assert bundles.js


def test_init(app):
    """Initialization."""
    theme = InvenioTheme(app)
    assert theme.menu is not None
    assert 'THEME_SITENAME' in app.config


def test_init_app(app):
    """Initialization."""
    theme = InvenioTheme()
    assert theme.menu is None
    theme.init_app(app)
    assert theme.menu is not None
    assert 'THEME_SITENAME' in app.config


def test_render_template(app):
    """Test ability to render template."""
    InvenioTheme(app)
    InvenioAssets(app)
    with app.test_request_context():
        render_template("invenio_theme/page.html")
