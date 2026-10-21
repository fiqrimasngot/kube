(() => {
  const applyOled = () => {
    document.documentElement.style.setProperty('background-color', '#000000', 'important');
    document.body.style.setProperty('background-color', '#000000', 'important');
    document.body.style.setProperty('background-image', 'none', 'important');
    document.body.querySelectorAll('main, #__next, .min-h-screen').forEach((el) => {
      el.style.setProperty('background-color', '#000000', 'important');
      el.style.setProperty('background-image', 'none', 'important');
    });
    document.querySelectorAll('.service-card').forEach((el) => {
      el.style.setProperty('background-color', '#b9dcff', 'important');
      el.style.setProperty('color', '#0b1d33', 'important');
      el.style.setProperty('border', '1px solid #8fc5f5', 'important');
    });
  };
  applyOled();
  new MutationObserver(applyOled).observe(document.documentElement, { childList: true, subtree: true });
})();
