# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
# Copyright (C) 2022-2023 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio error handlers."""

from flask import Blueprint, current_app, render_template


def create_blueprint(app):
    """Create blueprint."""
    blueprint = Blueprint(
        "invenio_theme_frontpage",
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    if app.config["THEME_FRONTPAGE"]:
        blueprint.add_url_rule("/", "index", view_func=index)

    app.register_error_handler(401, unauthorized)
    app.register_error_handler(403, insufficient_permissions)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(429, too_many_requests)
    app.register_error_handler(500, internal_error)

    return blueprint


def index():
    """Simplistic front page view."""
    return render_template(
        current_app.config["THEME_FRONTPAGE_TEMPLATE"],
    )


def unauthorized(e):
    """Error handler to show a 401.html page in case of a 401 error."""
    return render_template(current_app.config["THEME_401_TEMPLATE"]), 401


def insufficient_permissions(e):
    """Error handler to show a 403.html page in case of a 403 error."""
    return render_template(current_app.config["THEME_403_TEMPLATE"]), 403


def page_not_found(e):
    """Error handler to show a 404.html page in case of a 404 error."""
    return render_template(current_app.config["THEME_404_TEMPLATE"]), 404


def too_many_requests(e):
    """Error handler to show a 429.html page in case of a 429 error."""
    return render_template(current_app.config["THEME_429_TEMPLATE"]), 429


def internal_error(e):
    """Error handler to show a 500.html page in case of a 500 error."""
    return render_template(current_app.config["THEME_500_TEMPLATE"]), 500
