# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
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

Include in page using:

.. code-block:: html

    {%- asset "thinkbio.modules.theme:css" %}
    <script src="{{ASSET_URL}}" ></script>
    {%- end asset %}
"""

from __future__ import absolute_import, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

css = NpmBundle(
    'scss/invenio_theme/styles.scss',
    filters='scss, cleancss',
    output='gen/styles.%(version)s.css',
    npm={
        "almond": "~0.3.1",
        "bootstrap-sass": "~3.3.5",
        "font-awesome": "~4.4.0",
        "jquery": "~1.9.1"
    }
)

js = Bundle(
    NpmBundle(
        'node_modules/almond/almond.js',
        'js/settings.js',
        filters='uglifyjs',
        npm={
            "almond": "~0.3.1",
            "jquery": "~1.9.1"
        }
    ),
    Bundle(
        'js/base.js',
        filters='requirejs',
    ),
    filters='jsmin',
    output="gen/packed.%(version)s.js",
)
