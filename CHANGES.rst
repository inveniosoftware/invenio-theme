..
    This file is part of Invenio.
    Copyright (C) 2015-2020 CERN.

    Invenio is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Changes
=======

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
