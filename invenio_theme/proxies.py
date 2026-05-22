# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-License-Identifier: MIT

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
