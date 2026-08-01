---
layout: page
title: Search
permalink: /search/
page_class: search-page
---

<form class="search-form" role="search">
  <input id="search-input" class="search-input" type="search" placeholder="Search posts..." aria-label="Search posts" autofocus>
</form>

<div id="search-results" class="search-results" data-search-json="{{ '/search.json' | relative_url }}">
  <p class="search-hint">Type a keyword to search your posts.</p>
</div>

<script src="{{ '/assets/js/tao/simple-jekyll-search.min.js' | relative_url }}"></script>
<script src="{{ '/assets/js/tao/search.js' | relative_url }}"></script>
