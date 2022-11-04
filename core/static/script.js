// Doc ready shorthand
$(function () {
  highlightCurrentURLInNav();
});

function highlightCurrentURLInNav() {
  const url = new URL(window.location.href);
  let urlChunks = url.pathname.split('/');
  urlChunks = urlChunks.slice(0, 2);
  let selector = '.side-nav a[href^="' + urlChunks.join('/') + '"]';

  // Home Page
  if (url.pathname == '/') {
    selector = '.side-nav a[href="' + url.pathname + '"]';
  }

  $(selector).closest('.side-nav-item').addClass('menuitem-active');
}
