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

  // Lightbox
  var lb = document.querySelector('.lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('p');
    var close = function () { lb.classList.remove('open'); document.body.style.overflow = ''; };
    var openItem = function (el) {
      var img = el.querySelector('img');
      var cap = el.querySelector('figcaption') || el.querySelector('h3');
      lbImg.src = img.src; lbImg.alt = img.alt;
      lbCap.textContent = cap ? cap.innerText.replace(/\n/g, ' · ') : '';
      lb.classList.add('open'); document.body.style.overflow = 'hidden';
    };
    document.querySelectorAll('.gallery figure, .project-card').forEach(function (el) {
      el.addEventListener('click', function () { openItem(el); });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openItem(el); }
      });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.tagName === 'BUTTON') close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
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
