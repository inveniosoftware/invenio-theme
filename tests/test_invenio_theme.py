# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

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
        tpl = base_tpl + '{%% block %s %%}TPLTEST{%% endblock %%}' % b
        assert 'TPLTEST' in render_template_string(tpl)


def test_version():
    """Test version import."""
    from invenio_theme import __version__
    assert __version__


def test_bundles():
    """Test bundles."""
    assert 'bootstrap-sass' in bundles.css.npm
    assert bundles.js


def test_init(app):
    """Initialization."""
    theme = InvenioTheme(app)
    assert theme.menu is not None
    assert 'THEME_SITENAME' in app.config
    assert 'SASS_BIN' in app.config


def test_init_app(app):
    """Initialization."""
    theme = InvenioTheme()
    assert theme.menu is None
    theme.init_app(app)
    assert theme.menu is not None
    assert 'THEME_SITENAME' in app.config
    assert 'SASS_BIN' in app.config


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
        'page_body', 'page_footer', 'trackingcode', 'body_inner'
    ]
    InvenioTheme(app)
    InvenioAssets(app)

    with app.test_request_context():
        assert_template_blocks(
            'invenio_theme/page.html', blocks, base_tpl=base_tpl)


def test_cover_template_blocks(app):
    """Test template blocks in page.html."""
    base_tpl = r"""{% extends 'invenio_theme/page_cover.html' %}
    {% set panel_title = 'Test' %}
    {% block css %}{% endblock %}
    {% block javascript %}{% endblock %}
    """

    # Test template API
    blocks = [
        'panel', 'page_header', 'page_body', 'page_footer', 'panel_content',
    ]
    InvenioTheme(app)
    InvenioAssets(app)

    with app.test_request_context():
        assert_template_blocks(
            'invenio_theme/page_cover.html', blocks, base_tpl=base_tpl)


def test_settings_template_blocks(app):
    """Test template blocks in page_settings.html."""
    base_tpl = r"""{% extends 'invenio_theme/page_settings.html' %}
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
            'invenio_theme/page_settings.html', blocks, base_tpl=base_tpl)


def test_header_template_blocks(app):
    """Test template blokcs in header.html."""
    blocks = [
        'navbar', 'navbar_header', 'brand', 'navbar_inner', 'navbar_right',
        'breadcrumbs', 'flashmessages', 'navbar_nav', 'navbar_search',
    ]
    InvenioTheme(app)
    InvenioAssets(app)
    with app.test_request_context():
        assert_template_blocks('invenio_theme/header.html', blocks)

    app.config.update(dict(THEME_SEARCHBAR=False))
    with app.test_request_context():
        tpl = \
            r'{% extends "invenio_theme/header.html" %}' \
            r'{% block navbar_search %}TPLTEST{% endblock %}'
        assert 'TPLTEST' not in render_template_string(tpl)


def test_lazy_bundles(app):
    """Test configurable bundles."""
    InvenioTheme(app)
    InvenioAssets(app)

    with app.app_context():
        from invenio_theme.bundles import admin_lte_css, lazy_skin

        assert str(lazy_skin()) in admin_lte_css.contents


def test_html_lang(app):
    """Test HTML language attribute."""
    base_tpl = r"""{% extends 'invenio_theme/page.html' %}
    {% block css %}{% endblock %}
    {% block javascript %}{% endblock %}
    """

    @app.route('/index')
    def index():
        """Render default page."""
        return render_template_string(base_tpl)

    InvenioTheme(app)
    InvenioAssets(app)

    with app.test_client() as client:
        response = client.get('/index')
        assert b'lang="en" ' in response.data

        response = client.get('/index?ln=de')
        assert b'lang="de" ' in response.data

        response = client.get('/index?ln=en')
        assert b'lang="en" ' in response.data


def test_frontpage_not_exists(app):
    """Test the frontpage that doesn't exist."""
    # Before configure the frontpage
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 404


def test_frontpage_exists(app_frontpage_handler):
    """Test the frontpage."""

    app_frontpage_handler.config.update(dict(
        THEME_FRONTPAGE_TITLE="Jessica Jones",
    ))

    # Check if exists
    with app_frontpage_handler.test_client() as client:
        response = client.get('/')
        assert b'Jessica Jones' in response.data
