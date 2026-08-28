/* Lightbox for portfolio plates + lazy full-res swap. */
(function () {
  var plates = Array.prototype.slice.call(document.querySelectorAll('button[data-full]'));
  if (!plates.length) return;

  var lb = document.createElement('div');
  lb.className = 'lb';
  lb.setAttribute('role', 'dialog');
  lb.setAttribute('aria-modal', 'true');
  lb.setAttribute('aria-label', 'Plate viewer');
  lb.innerHTML =
    '<div class="lb__bar">' +
      '<span class="lb__caption"></span>' +
      '<span class="lb__nav">' +
        '<button type="button" data-act="prev" aria-label="Previous plate">← Prev</button>' +
        '<button type="button" data-act="next" aria-label="Next plate">Next →</button>' +
        '<button type="button" data-act="close" aria-label="Close viewer">Close ✕</button>' +
      '</span>' +
    '</div>' +
    '<div class="lb__stage"><img alt=""></div>';
  document.body.appendChild(lb);

  var stage = lb.querySelector('.lb__stage img');
  var caption = lb.querySelector('.lb__caption');
  var current = 0;
  var lastFocus = null;

  function show(i) {
    current = (i + plates.length) % plates.length;
    var btn = plates[current];
    stage.src = btn.dataset.full;
    stage.alt = btn.dataset.caption || '';
    caption.textContent = (current + 1) + ' / ' + plates.length + '  ·  ' + (btn.dataset.caption || '');
  }

  function open(i) {
    lastFocus = document.activeElement;
    show(i);
    lb.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    lb.querySelector('[data-act="close"]').focus();
  }

  function close() {
    lb.classList.remove('is-open');
    document.body.style.overflow = '';
    stage.removeAttribute('src');
    if (lastFocus) lastFocus.focus();
  }

  plates.forEach(function (btn, i) {
    btn.addEventListener('click', function () { open(i); });
  });

  lb.addEventListener('click', function (e) {
    var act = e.target.dataset && e.target.dataset.act;
    if (act === 'close') return close();
    if (act === 'prev') return show(current - 1);
    if (act === 'next') return show(current + 1);
    if (e.target === lb || e.target.classList.contains('lb__stage')) close();
  });

  document.addEventListener('keydown', function (e) {
    if (!lb.classList.contains('is-open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(current - 1);
    else if (e.key === 'ArrowRight') show(current + 1);
  });
})();
