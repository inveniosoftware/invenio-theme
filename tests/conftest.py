# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
# Copyright (C) 2022-2023 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Pytest configuration."""


import shutil

import jinja2
import pytest
from flask import Flask
from flask_webpackext.manifest import (
    JinjaManifest,
    JinjaManifestEntry,
    JinjaManifestLoader,
)
from helpers import make_fake_template
from invenio_assets import InvenioAssets
from invenio_i18n import Babel, InvenioI18N
from invenio_i18n.views import create_blueprint_from_app

from invenio_theme import InvenioTheme
from invenio_theme.views import create_blueprint


#
# Mock the webpack manifest to avoid having to compile the full assets.
#
class MockJinjaManifest(JinjaManifest):
    """Mock manifest."""

    def __getitem__(self, key):
        """Get a manifest entry."""
        return JinjaManifestEntry(key, [key])

    def __getattr__(self, name):
        """Get a manifest entry."""
        return JinjaManifestEntry(name, [name])


class MockManifestLoader(JinjaManifestLoader):
    """Manifest loader creating a mocked manifest."""

    def load(self, filepath):
        """Load the manifest."""
        return MockJinjaManifest()


@pytest.fixture()
def app():
    """Flask app fixture."""
    app = Flask("myapp")
    app.config.update(
        I18N_LANGUAGES=[("en", "English"), ("de", "German")],
        THEME_FRONTPAGE=False,
        APP_THEME=["semantic-ui"],
        WEBPACKEXT_MANIFEST_LOADER=MockManifestLoader,
    )
    Babel(app)
    InvenioI18N(app)

    app.register_blueprint(create_blueprint_from_app(app))
    app.register_blueprint(create_blueprint(app))

    def delete_locale_from_cache(exception):
        """Unset locale from `flask.g` when the request is tearing down."""
        from flask import g

        if "_flask_babel" in g:
            g._flask_babel.babel_locale = None

    app.teardown_request(delete_locale_from_cache)

    return app


@pytest.fixture()
def app_error_handler(request):
    """Flask app error handler fixture."""
    app = Flask("myapp")

    # Creation of a fake theme error template file.
    temp_dir = make_fake_template(
        "{# -*- coding: utf-8 -*- -#}"
        "<!DOCTYPE html>{% block message %}"
        "{% endblock message %}"
    )
    # Adding the temporal path to jinja engine.
    app.jinja_loader = jinja2.ChoiceLoader(
        [jinja2.FileSystemLoader(temp_dir), app.jinja_loader]
    )

    # Setting by default fake.html as a THEME_ERROR_TEMPLATE
    app.config["THEME_ERROR_TEMPLATE"] = "invenio_theme/fake.html"

    app.config["APP_THEME"] = ["semantic-ui"]

    # Tear down method to clean the temp directory.
    def tear_down():
        shutil.rmtree(temp_dir)

    request.addfinalizer(tear_down)

    app.testing = True
    Babel(app)
    InvenioI18N(app)
    InvenioTheme(app)

    app.register_blueprint(create_blueprint(app))
    return app


@pytest.fixture()
def app_frontpage_handler(request):
    """Flask app error handler fixture."""
    app = Flask("myapp")

    # Creation of a fake theme error template file.
    temp_dir = make_fake_template(
        "{% extends 'invenio_theme/page.html' %}"
        "{% block css %}{% endblock %}"
        "{% block javascript %}{% endblock %}"
    )

    # Adding the temporal path to jinja engine.
    app.jinja_loader = jinja2.ChoiceLoader(
        [jinja2.FileSystemLoader(temp_dir), app.jinja_loader]
    )

    # Setting by default fake.html as a BASE_TEMPLATE
    app.config["BASE_TEMPLATE"] = "invenio_theme/fake.html"
    app.config["THEME_FRONTPAGE"] = True
    app.config["APP_THEME"] = ["semantic-ui"]

    # Tear down method to clean the temp directory.
    def tear_down():
        shutil.rmtree(temp_dir)

    request.addfinalizer(tear_down)

    app.testing = True
    Babel(app)
    InvenioI18N(app)
    InvenioTheme(app)
    InvenioAssets(app)

    app.register_blueprint(create_blueprint(app))
    return app
