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

"""Invenio standard theme.

Invenio-Theme is a core Invenio package responsible for configuration of Jinja2
templates used to render base, cover and error pages. There are various
predefined error handler for most common application exceptions.

It mainly consists of:

- `Menu and breadcrums` - for basic site navigation using `Flask-Menu
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

>>> from flask import Flask
>>> from invenio_theme import InvenioTheme
>>> app = Flask('myapp')
>>> theme = InvenioTheme(app)

.. note::

   There is a new blueprint registered during initialization in order to enable
   loading of files from template and static folders.

In order for the following examples to work, you need to work within an Flask
application context so let's push one:

>>> ctx = app.app_context()
>>> ctx.push()

Configuration
-------------

* THEME_SITENAME
* THEME_GOOGLE_SITE_VERIFICATION
"""

from __future__ import absolute_import, print_function

from .ext import InvenioTheme
from .version import __version__

__all__ = ('__version__', 'InvenioTheme')
