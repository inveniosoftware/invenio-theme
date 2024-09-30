/*
 * This file is part of Invenio.
 * Copyright (C) 2017-2022 CERN.
 *
 * Invenio is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

// eslint-disable-next-line no-unused-vars
import jquery from "jquery/dist/jquery";
import "./truncate.js";
import "semantic-ui-css/semantic.js";
import "semantic-ui-less/semantic.less";

// Initialize Semantic UI components
jquery(".ui.dropdown").dropdown({
  onShow: function() {
    const dropdownElem = jquery(this);
    dropdownElem.attr("aria-expanded", true);
  },
  onHide: function() {
    const dropdownElem = jquery(this);
    dropdownElem.attr("aria-expanded", false);
  },
  onChange: function(value, text, $selectedOption) {
    const dropdownElem = jquery(this);
    const options = dropdownElem.find(".item");

    options.each((index, option) => {
      jquery(option).attr("aria-selected", false);
    })
    $selectedOption.attr("aria-selected", true);
  }
});

jquery(".ui.accordion").accordion({
  selector: {
    trigger: '.trigger'
  },
  onOpening: function() {
    const $accordionTrigger = this.closest('.ui.accordion').find('.trigger');
    const accordionCloseText = $accordionTrigger.attr('data-close-text');
    accordionCloseText && $accordionTrigger.html(accordionCloseText);
    $accordionTrigger.attr('aria-expanded', true);
  },
  onClosing: function() {
    const $accordionTrigger = this.closest('.ui.accordion').find('.trigger');
    const accordionOpenText = $accordionTrigger.attr('data-open-text');
    accordionOpenText && $accordionTrigger.html(accordionOpenText);
    $accordionTrigger.attr('aria-expanded', false);
  }
});

jquery('.ui.accordion .trigger').on("keydown", function (event) {
  const $target = jquery(event.target);
  const isTriggerElement = $target.is(".trigger") && !$target.is('button');
  // Button already have this functionality and will cause double trigger

  if (isTriggerElement && event.key === "Enter") {
    const accordionTitle = jquery(event.target).closest('.title');

    if (accordionTitle.hasClass('active')) {
      $target.accordion("close");
      $target.attr('aria-expanded', false);
    } else {
      $target.accordion("open");
      $target.attr('aria-expanded', true);
    }
  }
});

jquery(".message .close").on("click", function () {
  jquery(this).closest(".message").transition({
    animation: "fade",
    duration: 0,
    interval: 0,
  });
});

jquery(".message .close-btn").on("keydown", function (event) {
  if(event.key === "Enter") {
    jquery(this).closest(".message").transition({
      animation: "fade",
      duration: 0,
      interval: 0,
    });
  }
});

/* Expand and collapse navbar  */
const toggle = document.querySelector(".menu-icon");
const menu = document.querySelector(".navbar-menu");
/* Toggle mobile menu */
function toggleMenu() {
  if (menu.classList.contains("active")) {
    menu.classList.remove("active");
  } else {
    menu.classList.add("active");
  }
}
toggle && toggle.addEventListener("click", toggleMenu, false);

// Make sure screen reader picks up the flashed messages on page load
document.addEventListener('DOMContentLoaded', event => {
  jquery("#flash-message #alert-content").css('display', 'block');
})

// Declare global Invenio object to be used by JS applications in various modules
window.invenio = {
  onSearchResultsRendered: () => {},
}
