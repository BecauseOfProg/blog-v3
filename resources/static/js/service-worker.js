/*
 * This file is the service worker : it makes an offline copy of pages.
 */

if (navigator.serviceWorker.controller) {
  console.log('[PWA Builder] active service worker found, no need to register')
} else {
  // Register the ServiceWorker (only on production)
  if (document.location.hostname === 'localhost') {
    console.log('Local development - Ignoring service worker installation')
  } else {
    navigator.serviceWorker
      .register('/pwabuilder-sw.js', {
        scope: './'
      })
      .then(function (reg) {
        console.log('Service worker has been registered for scope: ' + reg.scope)
      })
  }
}
