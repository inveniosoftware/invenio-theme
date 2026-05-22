# SPDX-FileCopyrightText: 2017-2018 CERN.
# SPDX-FileCopyrightText: 2022 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Pytest helpers."""

import os
import shutil
import tempfile


def make_fake_template(content=""):
    """Create fake template for testing.

    :param content: File content.
    :returns: The temprorary directory.
    """
    temp_dir = tempfile.mkdtemp()
    invenio_theme_dir = os.path.join(temp_dir, "invenio_theme")
    os.mkdir(invenio_theme_dir)
    fake_file = open(os.path.join(invenio_theme_dir, "fake.html"), "w+")
    fake_file.write(content)
    fake_file.close()
    return temp_dir
