# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Minimal Flask application for development.

SPHINX-START

Install the Invenio default theme and build assets:

.. code-block:: console

    $ pip install -e .[all]
    $ cd examples
    $ ./app-setup.sh

Run the development server:

.. code-block:: console

    $ FLASK_APP=app.py flask run --debugger -p 5000

To be able to uninstall the example app:

.. code-block:: console

    $ ./app-teardown.sh


The example application demonstrates the default templates and the usage of
menus and breadcrumbs. The views are registered to the application menu, which
is visible on the page header. For more information about menus, see
`Flask-Menu <https://flask-menu.readthedocs.io/>`_.

The views displayed in the menu are:

* Base page - Demonstrates the empty **page** template, which has an empty
  **page_body** block.
* Cover page - Demonstrates the **page_cover** template, which displays the
  page logo.
* Error pages - Demonstrates the different views for each one of the common
  error codes.
* Message flashing - Demonstrates the message flashing functionality and
  flash template, with which you can display a flash message to the user using
  the :func:`flask.flash` method provided by Flask.
* Settings - Demonstrates the **page_settings** template. Inside, the submenu
  **settings** of the current menu is displayed as a list on the left of the
  page.

On the views that have it, the breadcrumb trail is also displayed below the
menu. It displays the location of the current view in the hierarchy. The user
may click on the links in the breadcrumb to navigate to the previous views.
To read more about breadcrumbs, see `Flask-Breadcrumbs
<https://flask-breadcrumbs.readthedocs.io/>`_.`

SPHINX-END

"""

from __future__ import absolute_import, print_function

from os.path import dirname, join

import jinja2
from flask import Flask, flash, render_template, request
from flask_babelex import Babel, gettext
from flask_breadcrumbs import register_breadcrumb
from flask_menu import register_menu
from invenio_assets import InvenioAssets
from speaklater import make_lazy_string

from invenio_theme import InvenioTheme
from invenio_theme.bundles import css, js

try:
    from invenio_i18n import InvenioI18N
except ImportError:
    InvenioI18N = None


def lazy_gettext(*args, **kwargs):
    """Lazy gettext.

    https://github.com/mrjoes/flask-babelex/pull/8
    """
    return make_lazy_string(gettext, *args, **kwargs)
_ = lazy_gettext

# Create Flask application
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    ERRORS={
        '401': _('Unauthorized'),
        '403': _('Forbidden'),
        '404': _('Page not found'),
        '500': _('Internal server error'),
    },
    BABEL_DEFAULT_LOCALE='en',
    I18N_LANGUAGES=[('da', _('Danish')), ],
    SECRET_KEY='CHANGEME',
    THEME_BREADCRUMB_ROOT_ENDPOINT='index',
)
if InvenioI18N is not None:
    InvenioI18N(app)
else:
    Babel(app)

# Set jinja loader to first grab templates from the app's folder.
app.jinja_loader = jinja2.ChoiceLoader([
    jinja2.FileSystemLoader(join(dirname(__file__), "templates")),
    app.jinja_loader
])

# Load Invenio modules
theme = InvenioTheme(app)
assets = InvenioAssets(app)

# Register assets
assets.env.register('invenio_theme_js', js)
assets.env.register('invenio_theme_css', css)


# Register menu items
item = theme.menu.submenu('main.errors')
item.register(
    '', _('Error pages'), active_when=lambda: request.endpoint == "error",
    order=3
)
for err, title in app.config['ERRORS'].items():
    item = theme.menu.submenu('main.errors.err%s' % err)
    item.register(
        'error', title, order=err,
        endpoint_arguments_constructor=lambda: dict(
            err=err)
    )


@app.route('/')
@register_menu(app, 'main.base', _('Base page'), order=1)
def index():
    """Simple test view."""
    return render_template('index.html')


@app.route('/cover')
@register_menu(app, 'main.cover', _('Cover page'), order=2)
def cover():
    """Simple test view."""
    flash('This is a message for the end user.',
          category=request.args.get('category', 'success'))
    return render_template('cover.html')


@app.route('/errors/<err>/')
@register_breadcrumb(app, '.error', _('Error page'))
def error(err):
    """Render error."""
    if err in app.config['ERRORS']:
        return render_template('invenio_theme/%s.html' % err)
    return _("Invalid error code.")


@app.route('/flash/')
@register_breadcrumb(app, '.flash', _('Flash page'))
@register_menu(app, 'main.flash', _('Message flashing'), order=4)
def flashmessage():
    """Flash a message."""
    flash('This is a message for the end user.',
          category=request.args.get('category', 'success'))
    return render_template('index.html')


@app.route('/settings/')
@register_breadcrumb(app, '.settings', _('Settings page'))
@register_menu(app, 'main.settings', _('Settings'), order=5)
@register_menu(app, 'settings.example_app', _('Panel Header'), order=1)
def settings():
    """Test page for settings templates."""
    return render_template('settings/base.html')


@app.route('/settings/1/')
@register_menu(app, 'settings.example_app_item1', _('Item 1'), order=2)
def settings_item_1():
    """Setting form route and menu registration."""
    flash('This is a message for the end user.',
          category=request.args.get('category', 'success'))
    return render_template('settings/item1.html')


@app.route('/settings/2/')
@register_menu(app, 'settings.example_app_item2', _('Item 2'), order=3)
def settings_item_2():
    """Setting form route and menu registration."""
    return render_template('settings/item2.html')
