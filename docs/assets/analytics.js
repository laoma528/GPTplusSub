/* GA4 Standard: the measurement ID is public; no account credentials are used. */
(() => {
  const measurementId = 'G-Y4BX8V3RTV';
  const googleTagId = 'GTM-MJ27SBXR';
  if (location.hostname !== 'prodclub.vip') return;
  if (document.querySelector('meta[name="robots"]')?.content.includes('noindex')) return;
  if (window['ga-disable-' + measurementId]) return;

  const canonicalLink = document.querySelector('link[rel="canonical"]');
  if (!canonicalLink) return;
  const canonical = new URL(canonicalLink.href);
  if (canonical.origin !== location.origin || canonical.search || canonical.hash) return;

  let referrer = '';
  if (document.referrer) {
    try {
      const source = new URL(document.referrer);
      referrer = source.origin + (source.origin === location.origin ? source.pathname : '/');
    } catch (_) {
      // Never forward an unparsed referrer.
    }
  }

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('set', {
    page_location: canonical.href,
    page_referrer: referrer,
    allow_google_signals: false,
    allow_ad_personalization_signals: false,
  });
  window.gtag('js', new Date());

  document.addEventListener('prodclub:service-click', ({ detail }) => {
    if (detail?.site !== 'prodclub-vip' || !/^[a-z0-9_-]{1,40}$/.test(detail.placement || '')) return;
    window.gtag('event', 'service_click', {
      send_to: measurementId,
      service_placement: detail.placement,
      page_path: canonical.pathname,
      transport_type: 'beacon',
    });
  });

  const tag = document.createElement('script');
  tag.async = true;
  tag.src = 'https://www.googletagmanager.com/gtm.js?id=' + googleTagId;
  document.head.append(tag);
})();
