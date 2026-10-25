---
layout: page
title: 搜索
permalink: /search/
page_class: search-page
sitemap: false
---

<form class="search-form" role="search">
  <input id="search-input" class="search-input" type="search" placeholder="输入关键词检索文章…" aria-label="搜索文章" autofocus>
</form>

<div id="search-results" class="search-results" data-search-json="{{ '/search.json' | relative_url }}">
  <p class="search-hint">输入关键词开始检索，结果会实时出现在这里。</p>
</div>

<script src="{{ '/assets/js/tao/simple-jekyll-search.min.js' | relative_url }}"></script>
<script src="{{ '/assets/js/tao/search.js' | relative_url }}"></script>
