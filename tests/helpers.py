# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2018 CERN.
# Copyright (C) 2022 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


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
