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

Installing npm requirements
---------------------------

First collect npm, requirements from registered bundles:

.. code-block:: console

   $ cd examples
   $ flask -a app.py npm
   app
   Writing static/package.json
   $ cd static
   $ cat package.json
   {
       "version": "",
       "dependencies": {
           "font-awesome": "~4.4.0",
           "almond": "~0.3.1",
           "bootstrap-sass": "~3.3.5"
       },
       "name": "app"
   }


Now install npm requirements (requires that npm is already installed):

.. code-block:: console

   $ npm install
   ...
   $ cd node_modules
   $ ls -1
   almond
   bootstrap-sass
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
   invenio_theme:scss/body.scss symbolink link created
   invenio_theme:scss/cover.scss symbolink link created
   invenio_theme:scss/footer.scss symbolink link created
   invenio_theme:scss/input-icon.scss symbolink link created
   invenio_theme:scss/navbar.scss symbolink link created
   invenio_theme:scss/sidebarnav.scss symbolink link created
   invenio_theme:scss/styles.scss symbolink link created
   invenio_theme:scss/type.scss symbolink link created
   invenio_theme:scss/variables.scss symbolink link created
   259 of 270 files already present
   Done collecting.


Building assets
---------------

Next, we build the webassets bundles:

.. code-block:: console

   $ npm install -g node-sass clean-css requirejs uglify-js
   $ cd ../../
   $ flask -a app.py assets build
   app
   Building bundle: gen/styles.%(version)s.css
   Building bundle: gen/packed.%(version)s.js


Run server
----------

Last but not least we start our test server:

.. code-block:: console

   $ flask -a app.py --debug run

"""

from __future__ import absolute_import, print_function

from os.path import dirname, join

import jinja2
from flask import Flask, flash, render_template, request
from flask_babelex import gettext
from flask_babelex import Babel
from flask_breadcrumbs import register_breadcrumb
from flask_cli import FlaskCLI
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
    BABEL_DEFAULT_LOCALE='da',
    SECRET_KEY='CHANGEME'
)
# Compatibility layer between Flask 0.10/1.0
FlaskCLI(app)
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
assets.init_cli(app.cli)

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
@register_breadcrumb(app, 'main.base', _('Base page'))
@register_menu(app, 'main.base', _('Base page'), order=1)
def index():
    """Simple test view."""
    return render_template('index.html')


@app.route('/cover')
@register_breadcrumb(app, 'main.base', _('Cover page'))
@register_menu(app, 'main.base', _('Cover page'), order=2)
def cover():
    """Simple test view."""
    flash('This is a message for the end user.',
          category=request.args.get('category', 'success'))
    return render_template('cover.html')


@app.route('/errors/<err>/')
def error(err):
    """Render error."""
    if err in app.config['ERRORS']:
        return render_template('invenio_theme/%s.html' % err)
    return _("Invalid error code.")


@app.route('/flash/')
@register_menu(app, 'main.flash', _('Message flashing'), order=4)
def flashmessage():
    """Flash a message."""
    flash('This is a message for the end user.',
          category=request.args.get('category', 'success'))
    return render_template('index.html')


@app.route('/settings/')
@register_menu(app, 'main.settings', _('Settings'), order=5)
@register_menu(app, 'settings.example_app', _('Panel Header'), order=1)
def settings():
    """Test page for settings templates."""
    return render_template('settings/base.html')


@app.route('/settings/1/')
@register_menu(app, 'settings.example_app.item1', _('Item 1'), order=1)
def settings_item_1():
    """Setting form route and menu registration."""
    flash('This is a message for the end user.',
          category=request.args.get('category', 'success'))
    return render_template('settings/item1.html')


@app.route('/settings/2/')
@register_menu(app, 'settings.example_app.item2', _('Item 2'), order=2)
def settings_item_2():
    """Setting form route and menu registration."""
    return render_template('settings/item2.html')

if __name__ == "__main__":
    app.run()
