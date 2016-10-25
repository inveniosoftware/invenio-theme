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


"""Pytest configuration."""

from __future__ import absolute_import, print_function

import os
import shutil
import tempfile

import jinja2
import pytest
from flask import Flask
from flask_babelex import Babel
from invenio_i18n import InvenioI18N

from invenio_theme import InvenioTheme


@pytest.fixture()
def app():
    """Flask app fixture."""
    app = Flask('myapp')
    app.config.update(
        I18N_LANGUAGES=[('en', 'English'), ('de', 'German')],
    )
    Babel(app)
    InvenioI18N(app)
    return app


@pytest.fixture()
def app_error_handler(request):
    """Flask app error handler fixture."""
    app = Flask('myapp')

    # Creation of a fake theme error template file.
    temp_dir = tempfile.mkdtemp()
    invenio_theme_dir = os.path.join(temp_dir, 'invenio_theme')
    os.mkdir(invenio_theme_dir)
    fake_file = open(os.path.join(invenio_theme_dir, 'fake.html'), 'w+')
    fake_file.write("{# -*- coding: utf-8 -*- -#}"
                    "<!DOCTYPE html>{% block message %}"
                    "{% endblock message %}")
    fake_file.close()

    # Adding the temporal path to jinja engine.
    app.jinja_loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader(temp_dir),
        app.jinja_loader
    ])

    # Setting by default fake.html as a THEME_ERROR_TEMPLATE
    app.config['THEME_ERROR_TEMPLATE'] = 'invenio_theme/fake.html'

    # Tear down method to clean the temp directory.
    def tear_down():
        shutil.rmtree(temp_dir)
    request.addfinalizer(tear_down)

    app.testing = True
    Babel(app)
    InvenioI18N(app)
    InvenioTheme(app)
    return app
