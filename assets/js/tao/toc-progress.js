(function(document, window) {
  var sidebar = document.getElementById('reader-sidebar');
  var tocContainer = document.getElementById('reader-toc');
  var progressText = document.getElementById('reader-progress-text');
  var progressFill = document.getElementById('reader-progress-fill');
  var toggleButton = document.getElementById('reader-sidebar-toggle');
  var showButton = document.getElementById('reader-sidebar-show');
  var content = document.querySelector('.post-content');

  if (!tocContainer || !content) return;

  function setSidebarHidden(hidden) {
    if (!sidebar) return;
    sidebar.classList.toggle('reader-sidebar-hidden', hidden);
    if (showButton) {
      showButton.classList.toggle('visible', hidden);
    }
    localStorage.setItem('readerSidebarHidden', hidden ? 'true' : 'false');
  }

  if (toggleButton) {
    toggleButton.addEventListener('click', function() {
      setSidebarHidden(true);
    });
  }

  if (showButton) {
    showButton.addEventListener('click', function() {
      setSidebarHidden(false);
    });
  }

  var savedHidden = localStorage.getItem('readerSidebarHidden') === 'true';
  if (savedHidden) {
    setSidebarHidden(true);
  }

  var headings = Array.prototype.slice.call(content.querySelectorAll('h2, h3, h4'));
  if (!headings.length) {
    tocContainer.innerHTML = '<p class="reader-sidebar-empty">本文暂无章节标题。</p>';
    return;
  }

  headings.forEach(function(heading) {
    if (!heading.id) {
      heading.id = heading.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    }
  });

  var navList = document.createElement('ul');
  navList.className = 'reader-toc-list';

  headings.forEach(function(heading) {
    var item = document.createElement('li');
    item.className = 'reader-toc-item reader-toc-' + heading.tagName.toLowerCase();

    var link = document.createElement('a');
    link.href = '#' + heading.id;
    link.textContent = heading.textContent.trim();
    link.className = 'reader-toc-link';
    link.addEventListener('click', function() {
      document.getElementById(heading.id).scrollIntoView({ behavior: 'smooth', block: 'start' });
    });

    item.appendChild(link);
    navList.appendChild(item);
  });

  tocContainer.innerHTML = '';
  tocContainer.appendChild(navList);

  function updateProgress() {
    var documentElement = document.documentElement;
    var scrollTop = window.pageYOffset || documentElement.scrollTop;
    var scrollHeight = documentElement.scrollHeight - window.innerHeight;
    var ratio = scrollHeight > 0 ? Math.min(Math.max(scrollTop / scrollHeight, 0), 1) : 0;
    var percent = Math.round(ratio * 100);
    progressFill.style.width = percent + '%';
    progressText.textContent = percent + '%';
  }

  function updateActiveHeading() {
    var offset = window.innerHeight * 0.2;
    var currentIndex = 0;

    headings.forEach(function(heading, index) {
      var rect = heading.getBoundingClientRect();
      if (rect.top - offset <= 0) {
        currentIndex = index;
      }
    });

    var links = tocContainer.querySelectorAll('.reader-toc-link');
    links.forEach(function(link, index) {
      link.classList.toggle('active', index === currentIndex);
    });
  }

  function refresh() {
    updateProgress();
    updateActiveHeading();
  }

  window.addEventListener('scroll', refresh, { passive: true });
  window.addEventListener('resize', refresh);
  refresh();
})(document, window);
