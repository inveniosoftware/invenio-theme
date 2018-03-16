/*
 * This file is part of Invenio.
 * Copyright (C) 2015-2018 CERN.
 *
 * Invenio is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

({
  preserveLicenseComments: false,
  optimize: 'uglify2',
  uglify2: {
    output: {
      beautify: false,
      comments: false
    },
    compress: {
      drop_console: true,
      sequences: true,
      dead_code: true,
      conditionals: true,
      booleans: true,
      unused: true,
      if_return: true,
      join_vars: true
    },
    warnings: true,
    mangle: true
  },
  mainConfigFile: ['./settings.js']
})
