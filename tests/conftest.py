# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Pytest configuration."""

from __future__ import absolute_import, print_function

from helpers import make_fake_template

import os
import shutil
import tempfile

import jinja2
import pytest
from flask import Flask
from flask_babelex import Babel
from invenio_i18n import InvenioI18N

from invenio_assets import InvenioAssets
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
    temp_dir = make_fake_template(
        "{# -*- coding: utf-8 -*- -#}"
        "<!DOCTYPE html>{% block message %}"
        "{% endblock message %}"
    )
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


@pytest.fixture()
def app_frontpage_handler(request):
    """Flask app error handler fixture."""
    app = Flask('myapp')

    # Creation of a fake theme error template file.
    temp_dir = make_fake_template(
        "{% extends 'invenio_theme/page.html' %}"
        "{% block css %}{% endblock %}"
        "{% block javascript %}{% endblock %}"
    )

    # Adding the temporal path to jinja engine.
    app.jinja_loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader(temp_dir),
        app.jinja_loader
    ])

    # Setting by default fake.html as a BASE_TEMPLATE
    app.config['BASE_TEMPLATE'] = 'invenio_theme/fake.html'
    app.config['THEME_FRONTPAGE'] = True

    # Tear down method to clean the temp directory.
    def tear_down():
        shutil.rmtree(temp_dir)
    request.addfinalizer(tear_down)

    app.testing = True
    Babel(app)
    InvenioI18N(app)
    InvenioTheme(app)
    InvenioAssets(app)
    return app
