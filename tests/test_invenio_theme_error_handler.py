# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Test for theme module."""

from __future__ import absolute_import, print_function

from flask import Blueprint, abort


def test_page_error_handler_401(app_error_handler):
    """Testing error handler with 401 error code."""
    # Creation of Blueprint.
    blueprint = Blueprint('simple_page', __name__,
                          template_folder='templates')

    # Routing to a method which launches a 401 error.
    @blueprint.route('/error_401')
    def error_401():
        return abort(401)

    app_error_handler.register_blueprint(blueprint)

    with app_error_handler.test_client() as client:
        response = client.get('/error_401')
        assert response.status_code == 401
        assert b'<h1><i class=\"fa fa-flash\"></i>' in response.data
        assert b'Unauthorized</h1>' in response.data
        assert b'<p>You need to be authenticated' in response.data
        assert b'to view this page.</p>' in response.data


def test_page_error_handler_403(app_error_handler):
    """Testing error handler with 403 error code."""
    # Creation of Blueprint.
    blueprint = Blueprint('simple_page', __name__,
                          template_folder='templates')

    # Routing to a method which launches a 403 error.
    @blueprint.route('/error_403')
    def error_403():
        return abort(403)

    app_error_handler.register_blueprint(blueprint)

    with app_error_handler.test_client() as client:
        response = client.get('/error_403')
        assert response.status_code == 403
        assert b'<h1><i class="fa fa-flash"></i>' in response.data
        assert b'Permission required</h1>' in response.data
        assert b'<p>You do not have sufficient permissions' in response.data
        assert b'to view this page.</p>' in response.data


def test_page_error_handler_404(app_error_handler):
    """Testing error handler with 404 error code."""
    with app_error_handler.test_client() as client:
        response = client.get('/ThisPathDoesNotExists')
        assert response.status_code == 404
        assert b'<h1><i class="fa fa-flash"></i>' in response.data
        assert b'Page not found</h1>' in response.data
        assert b'<p>The page you are looking for' in response.data
        assert b'could not be found.</p>' in response.data


def test_page_error_handler_429(app_error_handler):
    """Testing error handler with 429 error code."""
    # Creation of Blueprint.
    blueprint = Blueprint('simple_page', __name__,
                          template_folder='templates')

    # Routing to a method which launches a 429 error.
    @blueprint.route('/error_429')
    def error_429():
        return abort(429)

    app_error_handler.register_blueprint(blueprint)

    with app_error_handler.test_client() as client:
        response = client.get('/error_429')
        assert response.status_code == 429
        assert b'<h1><i class="fa fa-flash"></i>' in response.data
        assert b'Too many requests</h1>' in response.data
        assert b'<p>You have made too many consecutive ' in response.data
        assert b'requests, please try again later.</p>' in response.data


def test_page_error_handler_500(app_error_handler):
    """Testing error handler with 401 error code."""
    # Creation of Blueprint.
    blueprint = Blueprint('simple_page', __name__,
                          template_folder='templates')

    # Routing to a method which launches a 401 error.
    @blueprint.route('/error_500')
    def error_500():
        return abort(500)

    app_error_handler.register_blueprint(blueprint)

    with app_error_handler.test_client() as client:
        response = client.get('/error_500')
        assert response.status_code == 500
        assert b'<h1><i class=\"fa fa-flash\"></i>' in response.data
        assert b'Internal server error</h1>' in response.data
