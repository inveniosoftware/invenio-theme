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

from __future__ import absolute_import, print_function

from flask import render_template_string
from invenio_assets import InvenioAssets

from invenio_theme import InvenioTheme, bundles


def assert_template_blocks(template, blocks, base_tpl=None):
    """Assert that blocks exists in template."""
    if base_tpl is None:
        base_tpl = """{%% extends '%s' %%}""" % template

    for b in blocks:
        tpl = base_tpl + "{%% block %s %%}TPLTEST{%% endblock %%}" % b
        assert 'TPLTEST' in render_template_string(tpl)


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
    # Remove assets to avoid problems compiling them.
    test_tpl = r"""{% extends 'invenio_theme/page.html' %}
    {% block css %}{% endblock %}
    {% block javascript %}{% endblock %}
    """

    InvenioTheme(app)
    InvenioAssets(app)
    with app.test_request_context():
        assert render_template_string(test_tpl)


def test_page_template_blocks(app):
    """Test template blocks in page.html."""
    base_tpl = r"""{% extends 'invenio_theme/page.html' %}
    {% block css %}{% endblock %}
    {% block javascript %}{% endblock %}
    """

    # Test template API
    blocks = [
        'head', 'head_meta', 'head_title', 'head_links', 'head_links_langs',
        'head_apple_icons', 'header', 'body', 'browserupgrade', 'page_header',
        'page_body', 'page_footer', 'trackingcode',
    ]
    InvenioTheme(app)
    InvenioAssets(app)

    with app.test_request_context():
        assert_template_blocks(
            "invenio_theme/page.html", blocks, base_tpl=base_tpl)


def test_settings_template_blocks(app):
    """Test template blocks in settings/content.html."""
    base_tpl = r"""{% extends 'invenio_theme/settings/content.html' %}
    {% block css %}{% endblock %}
    {% block javascript %}{% endblock %}
    """

    blocks = [
        'page_body', 'settings_menu', 'settings_content', 'settings_form'
    ]
    InvenioTheme(app)
    InvenioAssets(app)

    with app.test_request_context():
        assert_template_blocks(
            'invenio_theme/settings/content.html', blocks, base_tpl=base_tpl)


def test_header_template_blocks(app):
    """Test template blokcs in header.html."""
    blocks = [
        'navbar', 'navbar_header', 'brand', 'navbar_inner', 'navbar_right',
        'breadcrumbs',
    ]
    InvenioTheme(app)
    InvenioAssets(app)
    with app.test_request_context():
        assert_template_blocks("invenio_theme/header.html", blocks)
