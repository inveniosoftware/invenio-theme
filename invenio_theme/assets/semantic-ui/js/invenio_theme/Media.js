/*
 * SPDX-FileCopyrightText: 2017-2022 CERN.
 * SPDX-License-Identifier: MIT
 */

import { createMedia } from "@artsy/fresnel";

// IMPORTANT: align changes with site.variables
export const breakpoints = {
  void: 0,
  mobile: 320,
  tablet: 768,
  computer: 1280,
  largeScreen: 1680,
  widescreen: 1920,
};

export const AppMedia = createMedia({
  breakpoints: breakpoints,
});

