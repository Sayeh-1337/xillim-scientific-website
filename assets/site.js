document.addEventListener('DOMContentLoaded', () => {
  const menuBtn = document.querySelector('.menu');
  const navlinks = document.querySelector('.navlinks');
  menuBtn?.addEventListener('click', () => {
    const open = navlinks.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  document.querySelectorAll('.navlinks a').forEach((a) => {
    a.addEventListener('click', () => {
      navlinks?.classList.remove('open');
      menuBtn?.setAttribute('aria-expanded', 'false');
      document.querySelectorAll('.navitem.open').forEach((n) => n.classList.remove('open'));
    });
  });

  document.querySelectorAll('.navitem > button').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const item = btn.parentElement;
      const wasOpen = item.classList.contains('open');
      document.querySelectorAll('.navitem.open').forEach((n) => n.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
      btn.setAttribute('aria-expanded', (!wasOpen).toString());
    });
  });

  document.addEventListener('click', (e) => {
    if (!e.target.closest('.navitem')) {
      document.querySelectorAll('.navitem.open').forEach((n) => n.classList.remove('open'));
    }
  });

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reveals = document.querySelectorAll('.reveal');
  if (reduceMotion) {
    reveals.forEach((el) => el.classList.add('in'));
  } else if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('in'));
  }

  const form = document.querySelector('#inquiry');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const items = [...data.entries()]
      .filter(([k]) => k !== 'consent')
      .map(([k, v]) => k + ': ' + v)
      .join('\n');
    const address = form.dataset.email || '';
    const subject = encodeURIComponent('Xillim Scientific | Project Assessment Request');
    const body = encodeURIComponent(
      'Project inquiry\n\n' +
        items +
        '\n\nPlease do not send confidential or patient-level data via email until a secure transfer arrangement is agreed.'
    );
    const status = document.querySelector('.formstatus');
    if (status) {
      status.textContent =
        'Your email application will open with the prepared request. Please send it there to complete the inquiry.';
    }
    window.location.href = 'mailto:' + address + '?subject=' + subject + '&body=' + body;
  });
});
