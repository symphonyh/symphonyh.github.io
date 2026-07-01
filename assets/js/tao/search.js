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
    template: '<div class="search-result"><a href="{{url}}"><h2>{{title}}</h2></a><p>{{content}}</p></div>',
    noResultsText: '<p class="search-no-results">No results found.</p>',
    limit: 0,
    fuzzy: true,
    debounceTime: 300, // 单位毫秒
    noResultsText: '没有找到相关文章'
  });
});
