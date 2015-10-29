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

"""Minimal Flask application for development.

Installing bower requirements
-----------------------------

First collect bower requirements from registered bundles:

.. code-block:: console

   $ cd example
   $ flask -a app.py bower
   app
   Writing instance/bower.json
   Writing instance/.bowerrc
   $ cd instance
   $ cat bower.json
   {
       "version": "",
       "dependencies": {
           "font-awesome": "~4.4.0",
           "almond": "~0.3.1",
           "bootstrap": "~3.3.5"
       },
       "name": "app"
   }
   $ cat .bowerrc
   {"directory": "../static/bower_components"}


Now install bower requirements (requires that bower is already installed):

.. code-block:: console

   $ bower install
   ...
   $ cd ../static/bower_components
   $  ls -1
   almond
   bootstrap
   font-awesome
   jquery

Collect static files
--------------------

Next, we copy the static files from the Python packages into the Flask
application's static folder:

.. code-block:: console

   $ cd ../../
   $ flask -a app.py collect -v
   app
   Collect static from blueprints
   invenio_theme:js/base.js symbolink link created
   invenio_theme:js/settings.js symbolink link created
   invenio_theme:less/body.less symbolink link created
   invenio_theme:less/cover.less symbolink link created
   invenio_theme:less/footer.less symbolink link created
   invenio_theme:less/input-icon.less symbolink link created
   invenio_theme:less/navbar.less symbolink link created
   invenio_theme:less/sidebarnav.less symbolink link created
   invenio_theme:less/styles.less symbolink link created
   invenio_theme:less/type.less symbolink link created
   invenio_theme:less/variables.less symbolink link created
   259 of 270 files already present
   Done collecting.


Building assets
---------------

Next, we build the webassets bundles:

.. code-block:: console

   $ cd ../../
   $ flask -a app.py assets build
   app
   Building bundle: gen/styles.%(version)s.css
   Building bundle: gen/packed.%(version)s.js


Run server
----------

Last but not least we start our test server:

.. code-block:: console

   $ flask -a app.py run --debugger --reload

"""

from __future__ import absolute_import, print_function

from os.path import dirname, join

import jinja2
from flask import Flask, render_template, request
from flask_babelex import gettext as _
from flask_babelex import Babel
from flask_breadcrumbs import register_breadcrumb
from flask_cli import FlaskCLI
from flask_menu import register_menu

from invenio_assets import InvenioAssets

from invenio_theme import InvenioTheme
from invenio_theme.bundles import css, js

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
    BABEL_DEFAULT_LOCALE='da',
)
# Compatibility layer between Flask 0.10/1.0
FlaskCLI(app)
Babel(app)

# Set jinja loader to first grab templates from the app's folder.
app.jinja_loader = jinja2.ChoiceLoader([
    jinja2.FileSystemLoader(join(dirname(__file__), "templates")),
    app.jinja_loader
])

# Load Invenio modules
theme = InvenioTheme(app)
assets = InvenioAssets(app)
assets.init_cli(app.cli)

# Register assets
assets.env.register('invenio_theme_js', js)
assets.env.register('invenio_theme_css', css)

# Register menu items
item = theme.menu.submenu('main.errors')
item.register(
    '', _('Error pages'), active_when=lambda: request.endpoint == "error",
    order=2
)
for err, title in app.config['ERRORS'].items():
    item = theme.menu.submenu('main.errors.err%s' % err)
    item.register(
        'error', title, order=err,
        endpoint_arguments_constructor=lambda: dict(
            err=err)
    )


@app.route('/')
@register_breadcrumb(app, 'main.base', _('Base page'))
@register_menu(app, 'main.base', _('Base page'), order=1)
def index():
    """Simple test view."""
    return render_template('index.html')


@app.route('/errors/<err>')
def error(err):
    """Render error."""
    if err in app.config['ERRORS']:
        return render_template('invenio_theme/%s.html' % err)
    return _("Invalid error code.")


@app.route('/settings')
@register_menu(app, 'main.settings', _('Settings'))
def settings():
    """Test page for settings templates."""
    return render_template('settings/base.html')


@register_menu(app, 'settings.example_app', _('Menu Header'), order=1)
def _module_menu_header():
    """Helper function for registering top category for module settings.

    Not visible in default template.
    """
    return render_template('settings/content1.html')


@app.route('/settings/1')
@register_menu(app, 'settings.example_app.item1', _('Item 1'), order=1)
def settings_item_1():
    """Setting form route and menu registration."""
    return render_template('settings/item1.html')


@app.route('/settings/2')
@register_menu(app, 'settings.example_app.item2', _('Item 2'), order=2)
def settings_item_2():
    """Setting form route and menu registration."""
    return render_template('settings/item2.html')

if __name__ == "__main__":
    app.run()
