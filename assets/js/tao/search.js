document.addEventListener('DOMContentLoaded', function () {
  var searchForm = document.querySelector('.search-form');
  var searchInput = document.getElementById('search-input');
  var searchResults = document.getElementById('search-results');

  if (searchForm) {
    searchForm.addEventListener('submit', function (event) {
      event.preventDefault();
    });
  }

  if (!searchInput || !searchResults) return;

  SimpleJekyllSearch({
    searchInput: searchInput,
    resultsContainer: searchResults,
    json: searchResults.dataset.searchJson,
    // [SEARCH-FIX] 库内配置键是 searchResultTemplate（默认项名），传 template 会被 merge 丢弃；
    // 占位符由 /{(.*?)}/g 匹配，必须用单花括号，写成 {{url}} 会原样输出成字面量。
    searchResultTemplate: '<div class="search-result"><a href="{url}"><h2>{title}</h2></a><p>{content}</p></div>',
    // [SEARCH-FIX] 库内 c.limit = t.limit || 10，0 是 falsy 会被当成 10，改成足够大的数表示不限。
    limit: 999,
    fuzzy: true,
    debounceTime: 300, // 单位毫秒
    noResultsText: '<p class="search-no-results">没有找到相关文章</p>'
  });
});
