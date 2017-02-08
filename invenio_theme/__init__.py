# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016, 2017 CERN.
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

r"""Invenio standard theme.

Invenio-Theme is a core Invenio package responsible for configuration of Jinja2
templates used to render base, cover and error pages. There are various
predefined error handlers for most common application exceptions.

It mainly consists of:

- `Menu and breadcrumbs` - for basic site navigation using `Flask-Menu
  <https://flask-menu.readthedocs.io/>`_ and `Flask-Breadcrumbs
  <https://flask-breadcrumbs.readthedocs.io/>`_.
- `Templates and static files` - for integration with `Bootstrap
  <https://getbootstrap.com/>`_ HTML, CSS and JS framework.
- `Error handlers` - for showing user-friendly 401, 402, 404, and 500 error
  pages.

Initialization
--------------
First create a Flask application and initialize
:class:`~invenio_theme.ext.InvenioTheme` extension.

>>> from flask import Flask, render_template_string
>>> from invenio_theme import InvenioTheme
>>> from flask_menu import register_menu
>>> app = Flask('myapp')
>>> theme = InvenioTheme(app)

.. note::

   There is a new blueprint registered during initialization in order to enable
   loading of files from template and static folders.

In order for the following examples to work, you also need to load the
``invenio_i18n`` and ``invenio_assets`` extensions.

>>> from invenio_i18n import InvenioI18N
>>> from invenio_assets import InvenioAssets
>>> i18n = InvenioI18N(app)
>>> assets = InvenioAssets(app)


Templates
---------

You may now set up your application's paths and extend Invenio-Theme's
templates. You can set the templates that will be used for different purposes
in :any:`Configuration <configuration>`. By default, all templates extend
the template set in :const:`~invenio_theme.config.BASE_TEMPLATE` and override
some of its blocks.

The default base template provides the following blocks:

* **head** - Contains the contents of the ``<head>`` tag.

* **head_meta** - Contains the ``<meta>`` tags of the page.

* **head_title** - Contains the ``<title>`` tag.

* **head_links** - Contains all ``<link>`` tags.

* **head_links_langs** - Contains ``<link>`` tags used for localization.

* **head_apple_icons** - Contains ``<link>`` tags for ``apple-touch-icon`` s.

* **css** - Contains the ``<link>`` tags that load the CSS of the page.

* **body** - Contains the contents of the ``<body>`` tag.

* **browserupgrade** - Contains the text to be displayed on outdated browsers.

* **body_inner** - Contains the header, main body and footer.

* **page_header** - Contains the page header.

* **page_body** - Contains the main body of the page.

* **page_footer** - Contains the page footer.

* **javascript** - Contains ``<script>`` tags to be placed in the end of the
    page.

* **trackingcode** - Contains any tracking code.

Specifically, the layout of the blocks in this template is this:

.. code-block:: jinja

    <html>
      <head>
        {%- block head %}
            {%- block head_meta %}{%- endblock head_meta %}
            {%- block head_title %}{%- endblock head_title %}
            {%- block head_links %}
                {%- block head_links_langs %}{%- endblock head_links_langs %}
                {%- block head_apple_icons %}{%- endblock head_apple_icons %}
            {%- endblock head_links %}
            {%- block css %}{%- endblock css %}
        {%- endblock head %}
      </head>
      <body>
        {%- block body %}
            {%- block browserupgrade %}{%- endblock browserupgrade %}
            {%- block body_inner %}
                {%- block page_header %}{%- endblock page_header %}
                {%- block page_body %}{%- endblock page_body %}
                {%- block page_footer %}{%- endblock page_footer %}
            {%- endblock body_inner %}
            {%- block javascript %}{%- endblock javascript %}
            {%- block trackingcode %}{%- endblock trackingcode %}
        {%- endblock body %}
      </body>
    </html>

You may override a block of the inherited template by redefining it in your
own template like so:

>>> @app.route('/index')
... @register_menu(app, 'main.base', 'Base page', order=1)
... def index():
...     return render_template_string(
...     '{% extends config.THEME_BASE_TEMPLATE %}'\
...     '{%- block page_body %}'\
...     'This overrides the page_body block'\
...     '{%- endblock %}'\
...     '{%- block javascript %}'\
...     '{{ super() }}'\
...     '<script>// your script here</script>'\
...     '{%- endblock %}')

By using ``{{ super() }}`` inside an overriden block, you can preserve the
original contents while adding your own.

Menus
-----

You may use the decorator ``register_menu`` for registering
your view to the menu of a Flask application or Blueprint. In the example,
above, the view is registered on the application menu, with the path
``main.base`` in the menu hierarchy with the text ``Base page`` as the title.

By default, any menu items that are children of ``main`` (such as the above
example) will be displayed on the header of every page, via the
``page_header`` block. Likewise, menu items that are below ``settings`` will
be displayed in a menu in the settings page, via the ``page_settings``
block in the settings page template.

To read more about the creation and usage of menus, see :mod:`~flask_menu`.

Breadcrumbs
-----------

In order to register a view as part of a breadcrumb navigation, you may use the
:func:`~flask_breadcrumbs.register_breadcrumb` decorator. Using this, you can
specify the position of the view in a hierarchical manner, as well as the title
in the breadcrumb. By default, the current breadcrumb is displayed inside the
``page_header`` block in the base template.

An example is shown below.

>>> from flask_breadcrumbs import register_breadcrumb
>>> @app.route('/part1')
... @register_breadcrumb(app, '.', 'Index')
... def part1():
...     return render_template_string(
...     '{% extends config.THEME_BASE_TEMPLATE %}')
>>> @app.route('/part2')
... @register_breadcrumb(app, '.p2', 'Part 2')
... def part2():
...     return render_template_string(
...     '{% extends config.THEME_BASE_TEMPLATE %}')
>>> @app.route('/part3')
... @register_breadcrumb(app, '.p2.p3', 'Part 3')
... def part3():
...     return render_template_string(
...     '{% extends config.THEME_BASE_TEMPLATE %}')

When navigating to e.g. ``/part3`` in this example, you will see the breadcrumb
with the two previous views. You may click any of them to go to that view.

To learn more about the usage of breadcrumbs, see :mod:`~flask_breadcrumbs`.

Error handling
--------------
The templates used in the case of different errors can be specified in
:any:`Configuration <configuration>`. In the case that your view returns a
response with one of these codes as the status code, the relevant template
will be shown to the user. Specifically, you can set views for status codes
401, 403, 404, 500.

>>> @app.route('/error')
... def error():
...     abort(401)
...     # the template in config.THEME_401_TEMPLATE will be shown to the user

Flashed messages
----------------
At any time during a request, you may choose to record a message for the
user in order to display it only once in the future. This is a great way for
providing feedback to the user after an action, and Flask provides the method
:func:`flask.flash` for this purpose. The first parameter is the message, while
you may optionally supply a second parameter that serves as a category that
gives context to your message.

Invenio-Theme provides a macro in ``invenio_theme/macros/messages.html`` called
``flashed_messages`` that iterates through stored flash messages for the
current user and displays them in the current page. The category can be one of
'info', 'danger', 'warning' or 'success'. Using one of these will attach the
appropriate Bootstrap class to the message. By default, the current flashed
messages will be displayed inside the ``page_header`` block in the base
template.

An example of using this macro is provided below.

>>> from flask import flash
>>> app.config.update(dict(SECRET_KEY='change me'))
>>> @app.route('/flash')
... def flash_page():
...     flash('Warning for the user', 'warning')
...     flash('Info for the user', 'info')
...     return render_template_string(
...     '{%- from "invenio_theme/macros/messages.html" import '\
...     'flashed_messages with context -%}'\
...     '{% extends config.THEME_BASE_TEMPLATE %}'\
...     '{{ flashed_messages() }}')

.. note::

   As flash messages are stored in the user's session before they are
   displayed, you need to have the ``SECRET_KEY`` set in your configuration, in
   order for your application to be able to use sessions.

Configuration
-------------

In order to change the logo and the title of the site, you need to configure
:const:`~invenio_theme.config.THEME_LOGO` and
:const:`~invenio_theme.config.THEME_SITENAME` in **config.py**, respectively.
You can also set Google Site Verification tokens by adding them to
:const:`~invenio_theme.config.THEME_GOOGLE_SITE_VERIFICATION`.

For more information about the configuration and how to change the different
templates used, see :any:`Configuration <configuration>`.

Bundles
-------

For the easier integration of webassets, Invenio-Theme uses bundles.
A bundle consists of a number of source files, which are all bundled together
into an output file, and a list of filters is applied to the output.
Specifically, the default bundles used by Invenio-Theme are the following:

* **css** - Includes CSS for Almond, Bootstrap-SASS, FontAwesome and JQuery.
    Loaded by the base template.

* **admin_lte_css** - Includes the AdminLTE Bootstrap template as well as
    Select2, for use in the administrator pages.

* **admin_css** - Contains the CSS for administrator pages.

* **js** - Includes Almond, JQuery and RequireJS. Loaded by the base template.

* **admin_js** - Includes JQuery, Moment, Select2, Bootstrap, and Admin-LTE,
    which are needed for the administrator pages.

To learn more about using bundles, see :mod:`~invenio_assets`.
"""

from __future__ import absolute_import, print_function

from .ext import InvenioTheme
from .version import __version__

__all__ = ('__version__', 'InvenioTheme')
