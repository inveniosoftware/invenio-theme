# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JS/CSS bundles for theme.

You include one of the bundles in a page like the example below (using
``base`` bundle as an example):

.. code-block:: html

    {{ webpack['base.js']}}

"""

from __future__ import absolute_import, print_function

from invenio_assets.webpack import WebpackThemeBundle


theme = WebpackThemeBundle(
    __name__,
    'assets',
    default='bootstrap3',
    themes={
        'bootstrap3': dict(
            entry={
                'base': './js/invenio_theme/base.js',
                # requires jquery, moment, select2, bootstrap
                'adminlte': './js/invenio_theme/admin.js',
                'theme-admin': './scss/invenio_theme/admin.scss',
                'theme': './scss/invenio_theme/theme.scss',
            },
            dependencies={
                'bootstrap-sass': '~3.3.5',
                'font-awesome': '~4.4.0',
                'jquery': '~3.2.1',
                'moment': '~2.23.0',
                'select2': '~4.0.2',
                'admin-lte': '~2.4.8',
            }
        ),
        'semantic-ui': dict(
            entry={
                'base': './js/invenio_theme/base.js',
                'theme': './js/invenio_theme/theme.js',
            },
            dependencies={
                'semantic-ui-less': '~2.4.1',
                'semantic-ui-css': '~2.4.1',
                'font-awesome': '~4.4.0',
                'jquery': '~3.2.1',
            },
            aliases={
                '@invenio_theme/less': 'less/invenio_theme',
                'themes/invenio': 'less/invenio_theme/theme'
            }
        ),
    }
)
