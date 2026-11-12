// Vichar Manch — small site scripts (no dependencies)
(function () {
  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -60px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // YouTube: load the player only when clicked (keeps pages fast)
  document.querySelectorAll('.video-frame button[data-id]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + btn.dataset.id + '?autoplay=1&rel=0';
      f.title = btn.getAttribute('aria-label') || 'Vichar Manch video';
      f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      btn.parentNode.replaceChild(f, btn);
    });
  });

  // Gallery filter
  var filterBtns = document.querySelectorAll('.filters button');
  filterBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      filterBtns.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      b.setAttribute('aria-pressed', 'true');
      var cat = b.dataset.filter;
      document.querySelectorAll('.gallery figure').forEach(function (fig) {
        fig.style.display = (cat === 'all' || fig.dataset.cat.indexOf(cat) > -1) ? '' : 'none';
      });
    });
  });

  // Lightbox gallery (#17): click a photo to view it large, then move through
  // the rest with arrows, keyboard (← → Esc) or swipe. Photos keep their
  // original aspect ratio. One viewer per page, created here.
  var triggers = document.querySelectorAll('.gallery figure, .project-card');
  if (triggers.length) {
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Photo viewer');
    lb.innerHTML =
      '<button type="button" class="lb-btn lb-close" aria-label="Close">&times;</button>' +
      '<button type="button" class="lb-btn lb-prev" aria-label="Previous photo">&#8249;</button>' +
      '<figure class="lb-stage"><img class="lb-img" alt=""><figcaption class="lb-count" aria-live="polite"></figcaption></figure>' +
      '<button type="button" class="lb-btn lb-next" aria-label="Next photo">&#8250;</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('.lb-img'), lbCount = lb.querySelector('.lb-count');
    var btnPrev = lb.querySelector('.lb-prev'), btnNext = lb.querySelector('.lb-next'), btnClose = lb.querySelector('.lb-close');
    var list = [], idx = 0, lastFocus = null, busy = false;

    // the set to browse: visible photos in the same gallery (respects filters)
    var groupFor = function (el) {
      var gal = el.closest('.gallery');
      if (!gal) return [el];
      return Array.prototype.filter.call(gal.querySelectorAll('figure'), function (f) { return f.offsetParent !== null; });
    };
    var srcOf = function (el) { return el.querySelector('img').currentSrc || el.querySelector('img').src; };
    var preload = function (i) { if (list[i]) { var im = new Image(); im.src = srcOf(list[i]); } };

    var show = function (i, dir) {
      if (!list.length) return;
      idx = (i + list.length) % list.length;
      var el = list[idx], img = el.querySelector('img');
      var apply = function () {
        lbImg.src = srcOf(el); lbImg.alt = img.alt || '';
        lbCount.textContent = list.length > 1 ? (idx + 1) + ' / ' + list.length : '';
        lbImg.classList.remove('out-left', 'out-right');
        lbImg.classList.add(dir > 0 ? 'in-right' : dir < 0 ? 'in-left' : 'in-fade');
        void lbImg.offsetWidth;  // restart transition
        lbImg.classList.remove('in-right', 'in-left', 'in-fade');
        busy = false;
      };
      if (dir && lbImg.getAttribute('src')) {
        busy = true;
        lbImg.classList.add(dir > 0 ? 'out-left' : 'out-right');
        setTimeout(apply, 180);
      } else { apply(); }
      preload(idx + 1); preload(idx - 1);
    };
    var next = function () { if (!busy && list.length > 1) show(idx + 1, 1); };
    var prev = function () { if (!busy && list.length > 1) show(idx - 1, -1); };

    var open = function (el) {
      list = groupFor(el);
      lastFocus = document.activeElement;
      lb.classList.toggle('single', list.length < 2);
      lbImg.removeAttribute('src');
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      show(list.indexOf(el), 0);
      btnClose.focus();
    };
    var close = function () {
      lb.classList.remove('open');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    };

    triggers.forEach(function (el) {
      if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '0');
      el.addEventListener('click', function () { open(el); });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(el); }
      });
    });
    btnNext.addEventListener('click', function (e) { e.stopPropagation(); next(); });
    btnPrev.addEventListener('click', function (e) { e.stopPropagation(); prev(); });
    btnClose.addEventListener('click', close);
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb-stage')) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowRight') { e.preventDefault(); next(); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); prev(); }
      else if (e.key === 'Tab') {  // keep focus inside the viewer
        var f = [btnClose, btnPrev, btnNext].filter(function (b) { return b.offsetParent !== null; });
        var i = f.indexOf(document.activeElement);
        e.preventDefault();
        f[(i + (e.shiftKey ? -1 : 1) + f.length) % f.length].focus();
      }
    });
    // swipe on touch screens
    var sx = 0, sy = 0, tracking = false;
    lb.addEventListener('touchstart', function (e) {
      if (e.touches.length !== 1) return;
      tracking = true; sx = e.touches[0].clientX; sy = e.touches[0].clientY;
    }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (!tracking) return; tracking = false;
      var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
      if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy) * 1.3) { if (dx < 0) next(); else prev(); }
    }, { passive: true });
  }

  // Enquiry form -> WhatsApp or email (no server needed)
  var form = document.getElementById('enquiry');
  if (form) {
    var build = function () {
      var d = new FormData(form);
      var lines = [
        'Hello Vichar Manch, I would like to enquire about a performance.',
        'Name: ' + (d.get('name') || ''),
        'Organisation: ' + (d.get('org') || ''),
        'Phone: ' + (d.get('phone') || ''),
        'City / Site: ' + (d.get('city') || ''),
        'Requirement: ' + (d.get('service') || ''),
        'Message: ' + (d.get('message') || '')
      ];
      return lines.join('\n');
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var via = e.submitter && e.submitter.value === 'email' ? 'email' : 'wa';
      var text = build();
      if (via === 'email') {
        window.location.href = 'mailto:' + form.dataset.email + '?subject=' + encodeURIComponent('Performance enquiry') + '&body=' + encodeURIComponent(text);
      } else {
        window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
      }
    });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
