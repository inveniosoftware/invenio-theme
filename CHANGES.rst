..
    This file is part of Invenio.
    Copyright (C) 2015-2022 CERN.

    Invenio is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Changes
=======

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
