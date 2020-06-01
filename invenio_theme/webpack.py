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
                # theme.js is the main file for the Semantic-UI theme.
                # - theme.js imports semantic-ui-less/semantic.less
                # - semantic-ui-less/semantic.less imports various files
                #   that all import ""../../theme.config".
                # - theme.config (must be provided by an Invenio instance, that
                #   sets this as an alias) imports semantic-ui-less/theme.less.
                # - semantic-ui-less/theme.less imports
                #   1) the theme package: an invenio theme is configured below
                #      via the "themes/invenio" alias). theme.config set the
                #      respective variables to the "invenio" theme (e.g.
                #      "@site: 'invenio';").
                #   2) site theme: defined via the @siteFolder variable in
                #      "theme.config".
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
                # Used for defining an 'invenio' theme for Semantic-UI. The
                # code in "Semantic-UI-Less/theme.less" will look for e.g.
                # themes/@{theme}/globals/site.variables". This will resolve
                # to the path "less/invenio_theme/theme/global/site.variables".
                # This means that you in "theme.config" can use "invenio" as a
                # theme, e.g.:
                #   @site: 'invenio';
                'themes/invenio': 'less/invenio_theme/theme'
            }
        ),
    }
)
