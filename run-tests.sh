#!/usr/bin/env sh
# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-FileCopyrightText: 2022 Graz University of Technology.
# SPDX-License-Identifier: MIT

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m check_manifest
python -m setup extract_messages --output-file /dev/null
sphinx-build -qnNW docs docs/_build/html
python -m pytest
