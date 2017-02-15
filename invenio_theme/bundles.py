# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016, 2017 CERN.
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

"""JS/CSS bundles for theme.

You include one of the bundles in a page like the example below (using ``js``
bundle as an example):

.. code-block:: html

    {%- asset "invenio_theme.bundles:js" %}
    <script src="{{ASSET_URL}}"  type="text/javascript"></script>
    {%- end asset %}
"""

from __future__ import absolute_import, print_function

from flask import current_app
from flask_assets import Bundle
from invenio_assets import NpmBundle
from speaklater import is_lazy_string, make_lazy_string


class LazyNpmBundle(NpmBundle):
    """Magically evaluate lazy strings as file names."""

    def _get_contents(self):
        """Create strings from lazy strings."""
        return [
            str(value) if is_lazy_string(value) else value
            for value in super(LazyNpmBundle, self)._get_contents()
        ]

    contents = property(_get_contents, NpmBundle._set_contents)


css = NpmBundle(
    'scss/invenio_theme/styles.scss',
    depends=('scss/invenio_theme/*.scss', ),
    filters='node-scss,cleancssurl',
    output='gen/styles.%(version)s.css',
    npm={
        'almond': '~0.3.1',
        'bootstrap-sass': '~3.3.5',
        'font-awesome': '~4.4.0',
        'jquery': '~1.9.1',
    }
)
"""Default CSS bundle with Bootstrap and Font-Awesome."""


def lazy_skin():
    """Generate skin path."""
    return 'node_modules/admin-lte/dist/css/skins/{0}.min.css'.format(
        current_app.config.get('ADMIN_UI_SKIN', 'skin-blue')
    )


admin_lte_css = LazyNpmBundle(
    'node_modules/admin-lte/dist/css/AdminLTE.min.css',
    'node_modules/select2/dist/css/select2.min.css',
    make_lazy_string(lazy_skin),
    filters='cleancssurl',
    output='gen/styles.admin-lte.%(version)s.css',
    npm={
        'admin-lte': '~2.3.6',
        'select2': '~4.0.2',
    }
)
"""Admin LTE CSS."""

admin_css = NpmBundle(
    'scss/invenio_theme/admin.scss',
    filters='node-scss,cleancssurl',
    output='gen/styles.admin.%(version)s.css'
)
"""Default style for admin interface."""

# FIXME: This bundle doesn't build without the output
# being added to the js/base.js bundle.
js = Bundle(
    NpmBundle(
        'node_modules/almond/almond.js',
        'js/settings.js',
        filters='uglifyjs',
        npm={
            'almond': '~0.3.1',
            'angular': '~1.4.9',
            'jquery': '~1.9.1',
        }
    ),
    Bundle(
        'js/base.js',
        filters='requirejs',
        output='gen/base.%(version)s.js',
    ),
    filters='jsmin',
    output='gen/packed.%(version)s.js',
)
"""Default JavaScript bundle with Almond, JQuery and RequireJS."""

admin_js = NpmBundle(
    'node_modules/jquery/jquery.js',
    'node_modules/moment/moment.js',
    'node_modules/select2/dist/js/select2.full.js',
    'node_modules/bootstrap-sass/assets/javascripts/bootstrap.js',
    'node_modules/admin-lte/dist/js/app.js',
    output='gen/admin.%(version)s.js',
    filters='jsmin',
    npm={
        'jquery': '~1.9.1',
        'moment': '~2.9.0',
        'select2': '~4.0.2',
    }
)
"""AdminJS contains JQuery, Moment, Select2, Bootstrap, and Admin-LTE."""
