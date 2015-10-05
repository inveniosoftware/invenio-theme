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
applications static folder:

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

from __future__ import print_function, absolute_import

from os.path import join, dirname

import jinja2
from flask import Flask, render_template, request
from flask_breadcrumbs import register_breadcrumb
from flask_cli import FlaskCLI
from flask_menu import register_menu
from invenio_assets import InvenioAssets

from invenio_theme import InvenioTheme
from invenio_theme.bundles import js, css

# Create Flask application
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    ERRORS={
        '401': 'Unauthorized',
        '403': 'Forbidden',
        '404': 'Page not found',
        '500': 'Internal server error',
    }
)
FlaskCLI(app)

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
    '', 'Error pages', active_when=lambda: request.endpoint == "error",
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
@register_breadcrumb(app, 'main.base', 'Base page')
@register_menu(app, 'main.base', 'Base page', order=1)
def index():
    """Simple test view."""
    return render_template('index.html')


@app.route('/errors/<err>')
def error(err):
    """Render error."""
    if err in app.config['ERRORS']:
        return render_template('invenio_theme/%s.html' % err)
    return "Invalid error code."
