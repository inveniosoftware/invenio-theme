..
    This file is part of Invenio.
    Copyright (C) 2015-2024 CERN.
    Copyright (C) 2024 Graz University of Technology.

    Invenio is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Changes
=======

Version 3.6.0 (release 2025-01-21)

- theme: expand generator classes

Version 3.5.2 (release 2024-12-13)

- theme: fix flash message overlap
- theme: fix disable text contrast

Version 3.5.1 (release 2024-11-30)

- setup: change to reusable workflows
- setup: pin dependencies

Version v3.5.0 (released 2024-11-14)

- templates: page_cover: Add banner to login template
- site: add font-weight normal

Version v3.4.3 (released 2024-10-03)

- inject MathJax config to JS via data attribute in base html pages

Version v3.4.2 (released 2024-10-02)

- js: add an empty global Invenio plugin, to be used by Invenio modules for
    callbacks or other functionalities.

Version v3.4.1 (released 2024-09-26)

- administration: style packages versions badges

Version v3.4.0 (released 2024-09-17)

- config: add MathJax support
- navbar: fix logo size in non-desktop devices
- css: update table border style

Version v3.3.0 (released 2024-08-01)

- templates: add meta robot tags
    * Generate robots meta tags from the `THEME_META_ROBOT_TAGS` config or
      exlicitly set via the `meta_robot_tags` Jinja variable.
- header: increase invenio menu z-index

Version 3.2.0 (released 2024-06-25)

- global: add meta generator tag
    - Allows defining the value of the ``<meta generator>`` header tag by a
      string or a callable. Can be disabled by setting it to None.
    - See inveniosoftware/invenio-app-rdm#2689

Version 3.1.0 (released 2024-04-10)

- css: fix overflow for description in record details
- bug: add missing ``<title>s``

Version 3.0.0 (released 2024-03-19)

- global: remove breadcrumb support
- global: introduce shared menu
- global: preparation for compatibility with Flask v2.3.x deprecations
- refactor: current_theme_icons without application context

Version 2.5.10 (released 2024-01-28)

- installation: fix sphinx dependency

Version 2.5.9 (released 2024-01-28)

- global: change math operation to be compatible with sass2.0

Version 2.5.8 (released 2023-12-12)

- replace ckeditor with tinymce due to license issue

Version 2.5.7 (released 2023-10-26)

- community logo: fix rendering a placeholder

Version 2.5.6 (released 2023-10-20)

- don't override links style in flashed messages

Version 2.5.5 (released 2023-09-19)

- styling: add 3 column template class

Version 2.5.4 (released 2023-09-11)

- scss: fix compatibility with latest less version

Version 2.5.3 (released 2023-08-08)

- stylesheets: add preformatted tag styling font

Version 2.5.2 (released 2023-08-14)

- installation: pin Flask-Menu to ``<v1.0.0``.

Version 2.5.1 (released 2023-08-14)

- theme: bugfix to decrease z-index value

Version 2.5.0 (released 2023-08-09)

- theme: add utility classes

Version 2.4.0 (released 2023-08-02)

- theme: add some general classes and fixes alignment for labeled fluid buttons

Version 2.3.0 (released 2023-07-31)

- settings page: Improve template for a11y

Version 2.2.0 (released 2023-07-26)

- theme: add general style improvements

Version 2.1.3 (released 2023-07-24)

- messages: add z-index

Version 2.1.2 (released 2023-04-12)

- add flex utility classes
- add text sizes classes

Version 2.1.1 (released 2023-04-06)

- add display utility classes

Version 2.1.0 (released 2023-03-28)

- add global utility styling classes

Version 2.0.1 (released 2023-03-09)

- fix styling for buttons
- move global class for auto grid

Version 2.0.0 (released 2023-02-28)

- drop python 2.7 support
- remove flask_babelex imports
- upgrade invenio_i18n

Version 1.4.8 (released 2023-02-07)

- theme: add auto-column-grid class

Version 1.4.7 (released 2023-01-05)

- add truncate lines styles

Version 1.4.6 (released 2022-12-08)

- fix styling for inline class, affecting form fields

Version 1.4.5 (released 2022-12-01)

- fix search result item styling
- add global behaviour classes
- add placeholder image handle

Version 1.4.4 (released 2022-11-18)

- Add pulled translations

Version 1.4.3 (released 2022-11-03)

- add styling for dropdown menu items
- fix missing Media component range

Version 1.4.2 (released 2022-10-26)

- add Media to support responsive react components

Version 1.4.1 (released 2022-10-10)

- bump SemanticUI

Version 1.4.0 (released 2022-10-05)

- change global font to Lato

Version 1.3.31 (released 2022-10-05)

- add missing theme variables

Version 1.3.30 (released 2022-09-26)

- add styling to administration dashboard page

Version 1.3.29 (released 2022-09-22)

- add administration panel styling
- add translation workflow

Version 1.3.28 (released 2022-07-08)

- add styling classes with action color coding

Version 1.3.27 (released 2022-07-07)

- fix jquery reference

Version 1.3.26 (released 2022-07-07)

- add image placeholder on load error

Version 1.3.25 (released 2022-06-27)

- add German translations
- fix dropdown scroll misalignment

Version 1.3.24 (released 2022-05-23)

- add global CSS classes for margins auto

Version 1.3.23 (released 2022-05-19)

- add accessibility to ui-accordions

Version 1.3.22 (released 2022-04-21)

- improve semantic styling of My account page

Version 1.3.21 (released 2022-03-29)

- fix html tags in templates

Version 1.3.20 (released 2022-03-17)

- refactor page template
- add semantic ui invenio packaged theme configuration
- extend utils CSS classes

Version 1.3.19 (released 2022-03-04)

- Add a reusable Jinja macro to truncate long text.

Version 1.3.18 (released 2022-03-01)

- Revert font back to default sans-sarif font instead of Lato.

Version 1.3.17 (released 2022-02-28)

- Adds favicon
- Fix issue with flash message on login page not being side to side.

Version 1.3.16 (released 2022-02-17)

- Add common `square-placeholder.png` image for general use.

Version 1.3.15 (released 2022-02-17)

- Remove custom margin from classes to improve CSS overridability.

Version 1.3.14 (released 2022-02-16)

- Fix issue with Lato font not being loaded in Semantic UI theme.
- Sets Semantic UI @mutedTextColor.

Version 1.3.13 (released 2022-02-16)

- Ensure compiled translation message catalogs are included in the
  distributions uploaded on PyPI.

Version 1.3.12 (released 2022-02-14)

- Fixes A11y issue with the close button in flash messages.

Version 1.3.11 (released 2022-02-08)

- Adds margin generator.
- Adds A11y page landmarks.

Version 1.3.10 (released 2021-11-23)

- Web accessibility fix.

Version 1.3.9 (released 2021-07-12)

- Adds german translations

Version 1.3.8 (released 2021-02-10)

- Adds brand color to menu items

Version 1.3.7 (released 2021-01-25)

- Adds brand color in segments

Version 1.3.6 (released 2021-01-04)

- Adds `link` theme icon
- Fixes wildcard icon resolution

Version 1.3.5 (released 2020-12-17)

- Fixes checkbox.overrides in `invenio` SUI packaged theme.

Version 1.3.4 (released 2020-12-17)

- Adds a full "invenio" Semantic UI packaged theme so we can easier customize
  layout in the future.

- Moves theme.config to theme.config.example and adds a note to make it
  clear the file is not actually used, but is just an example.

- Adds helper tool for supporting theme dependent icons.

- Fixes many minor styling issues such as alignments, button locations,
  grids.

Version 1.3.3 (released 2020-12-11)

- Initializes semanticUI accordion components.

Version 1.3.2 (released 2020-12-11)

- Updates the Invenio logo and remove outdated versions.
- Fixes the dropdown to work on the user profile page.

Version 1.3.1 (released 2020-12-09)

- Minor fix for SemanticUI dropdowns

Version 1.3.0 (released 2020-12-09)

- Major: New SemanticUI theme has been integrated. The Bootstrap 3 theme still
  exists. This change depends on the latest released Invenio-Assets which
  adds supports for multiple UI frameworks.

- Adds support for dynamic loading of templates for React-Overridable.

- Backwards incompatible: The old-style Flask-Asset bundles was removed (these
  bundles were deprecated in Invenio v3.1).

- Adds Turkish translations.

Version 1.2.0 (released 2020-03-20)

- Replaces Flask dependency with ``invenio-base``.

Version 1.1.4 (released 2019-07-22)

- Introduce handling of the error 429.

Version 1.1.3 (released 2019-03-13)

- Restructure SCSS files, in order to allow easier customization and extension
  in overlays.

Version 1.1.2 (released 2019-02-15)

- Upgraded moment to 2.23.0

Version 1.1.1 (released 2018-12-05)

- Fixes issues with webpack and the AdminLTE theme.

Version 1.1.0 (released 2018-11-06)

- Introduce webpack support.

Version 1.0.0 (released 2018-03-23)

- Initial public release.
