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
    // [DATE 2026-10-28] {date} 来自 search.json 的 "date"（%Y-%m-%d），此前该字段取到了但没渲染。
    // 同一占位符在模板里出现两次也会都被替换（库内部是 replace(/\{(.*?)\}/g, ...) 全局替换）。
    searchResultTemplate: '<div class="search-result"><a href="{url}"><h2>{title}</h2></a><p>{content}</p><time datetime="{date}">{date}</time></div>',
    // [SEARCH-FIX] 库内 c.limit = t.limit || 10，0 是 falsy 会被当成 10，改成足够大的数表示不限。
    // [LIMIT-FIX] 全量 999 在搜高频词时会一次渲染近千张卡（移动端明显卡顿），100 足够覆盖真实查询。
    limit: 100,
    fuzzy: true,
    debounceTime: 300, // 单位毫秒
    noResultsText: '<p class="search-no-results">没有找到相关文章</p>'
  });
});
