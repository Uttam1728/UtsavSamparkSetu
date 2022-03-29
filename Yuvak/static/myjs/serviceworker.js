var staticCacheName = 'djangopwa-v2';

self.addEventListener('install', function(event) {

  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/admin','static/img/utsav.png'
      ]);
    })
  );
});

self.addEventListener('fetch',() => console.log("fetch"));