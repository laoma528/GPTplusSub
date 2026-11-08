/* Local UI interactions. Emits prodclub:service-click for analytics.js (GA4). */
const menu = document.querySelector('.menu');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  menu?.setAttribute('aria-expanded', 'false');
  menu?.setAttribute('aria-label', '打开菜单');
  navigation?.classList.remove('open');
}
menu?.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? '关闭菜单' : '打开菜单');
  navigation.classList.toggle('open', open);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {
    closeMenu(); menu.focus();
  }
});
document.addEventListener('click', event => {
  if (!event.target.closest('.site-header')) closeMenu();
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.querySelectorAll('[data-service-placement]').forEach(link => {
  link.addEventListener('click', () => {
    document.dispatchEvent(new CustomEvent('prodclub:service-click', {
      detail: { site: 'prodclub-vip', page: location.pathname, placement: link.dataset.servicePlacement }
    }));
  });
});
