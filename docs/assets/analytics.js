(() => {
  const measurementId = "G-SY5YCTVBY0";
  const serviceUrl = "https://prodclub.xyz/r/W3EF6W?src=GPTsub";
  const path = window.location.pathname;
  const pageId = path.endsWith("third-party.html")
    ? "third_party"
    : path.endsWith("self-subscribe.html")
      ? "self_subscribe"
      : path.endsWith("about.html")
        ? "about"
        : "home";

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag("js", new Date());

  let referrer = "";
  if (document.referrer) {
    try {
      const source = new URL(document.referrer);
      referrer = source.origin + source.pathname;
    } catch (_) {
      // Ignore an invalid referrer; never forward its raw value.
    }
  }

  window.gtag("config", measurementId, {
    page_location: window.location.origin + path,
    page_referrer: referrer,
  });

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[data-service-placement]");
    if (!link || link.href !== serviceUrl) return;
    window.gtag("event", "service_click", {
      page_id: pageId,
      placement: link.dataset.servicePlacement,
      transport_type: "beacon",
    });
  });
})();
