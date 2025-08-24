/*
 * This file is part of Invenio.
 * Copyright (C) 2017-2022 CERN.
 * Copyright (C) 2024      KTH Royal Institute of Technology.
 *
 * Invenio is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */


/*
 * to override the variables autoCompleteUrls, autocompleteIds, autoCompleteApi, autoCompleteLang
 * in your template, add the following code block:
 * 
 *  {% set autoCompleteApi = "/api/affiliations?size=4&suggest=" %}
 *  {% set autoCompleteUrls = [
 *     "/account/settings/profile",
 *     "/signup/",
 *   ] %}
 *   {% set autoCompleteLang = 'en' %}
 *   {% block javascript %}
 *   {{ super() }}
 *   <script>
 *     autoCompleteApi = "{{ autoCompleteApi | safe }}";
 *     autoCompleteUrls = {{ autoCompleteUrls }};
 *     autoCompleteLang = "{{ autoCompleteLang }}";
 *   </script>
 *   {% endblock %}
 */


document.addEventListener("DOMContentLoaded", function () {
  // API endpoint for fetching data
  var autoCompleteApi =
    window.autoCompleteApi || "/api/affiliations?size=4&suggest=";

  // Routes where autocomplete should be enabled
  var autoCompleteUrls = window.autoCompleteUrls || [
    "/account/settings/profile",
    "/oauth/authorized/github",
    "/oauth/authorized/orcid",
    "/signup",
  ];

  // Input element Ids to attach the autocomplete
  var autocompleteIds = window.autocompleteIds || [
    "profile-affiliations",
    "profile.affiliations",
  ];

  // Language to use for autocomplete suggestions
  var autoCompleteLang = window.autoCompleteLang || "en";

  async function fetchAffiliations(query, callback) {
    try {
      const response = await fetch(`${autoCompleteApi}${query}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      const suggestions = data.hits.hits.map((hit) => {
        return hit.title[autoCompleteLang] || hit.title["en"];
      });
      callback(suggestions);
    } catch (error) {
      console.error("Error fetching affiliations:", error);
      callback([]);
    }
  }

  function sanitizeQuery(query) {
    query = query.replace(/[^a-zA-Z0-9 ]/g, "");
    return query.substring(0, 10);
  }

  function autocomplete(inputElement) {
    const cache = new Map();
    const debounceTimeout = 100;
    let debounceTimer;

    // Create and append the datalist element
    const datalist = document.createElement("datalist");
    datalist.id = "affiliations-list";
    document.body.appendChild(datalist);

    // Link the datalist to the input element
    inputElement.setAttribute("list", datalist.id);
    inputElement.addEventListener("input", handleInput);
    inputElement.addEventListener("keydown", handleTabPress);

    function handleInput() {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        let query = inputElement.value.trim().toLowerCase();
        query = sanitizeQuery(query);
        if (!query) return;

        if (cache.has(query)) {
          updateDatalist(cache.get(query));
        } else {
          fetchAffiliations(query, (suggestions) => {
            cache.set(query, suggestions);
            updateDatalist(suggestions);
          });
        }
      }, debounceTimeout);
    }

    function handleTabPress(e) {
      if (e.key === "Tab" && datalist.options.length > 0) {
        inputElement.value = datalist.options[0].value;
      }
    }

    function updateDatalist(suggestions) {
      datalist.innerHTML = "";
      const fragment = document.createDocumentFragment();

      // Add suggestions to the datalist
      suggestions.forEach((suggestion) => {
        const option = document.createElement("option");
        option.value = suggestion;
        fragment.appendChild(option);
      });
      datalist.appendChild(fragment);
    }
  }

  function initializeAutocomplete() {
    autocompleteIds.forEach((id) => {
      const inputElement = document.getElementById(id);
      if (inputElement) {
        autocomplete(inputElement);
      }
      return;
    });
  }

  const currentPageUrl = window.location.pathname.replace(/\/+$/, '');

  if (autoCompleteUrls.includes(currentPageUrl)) {
    initializeAutocomplete();
  }
});
