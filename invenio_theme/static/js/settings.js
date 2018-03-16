/*
 * This file is part of Invenio.
 * Copyright (C) 2015-2018 CERN.
 *
 * Invenio is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

require.config({
  baseUrl: "/static/",
  paths: {
    jquery: "node_modules/jquery/jquery",
    bootstrap: "node_modules/bootstrap-sass/assets/javascripts/bootstrap",
    select2: "node_modules/select2/dist/js/select2"
  },
  shim: {
    jquery: {
      exports: "$"
    },
    bootstrap: {
      deps: ["jquery"]
    },
    select2: {
      deps: ["jquery"],
      exports: "select2"
    }
  }
})
