# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Helper proxy to the state object."""

from flask import current_app
from werkzeug.local import LocalProxy

from .icons import ThemeIcons

current_theme_icons = LocalProxy(
    lambda: ThemeIcons(
        current_app.config["APP_THEME"], current_app.config["THEME_ICONS"]
    )
)
"""Proxy to the theme icon finder."""
