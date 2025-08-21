// PEACOCK COSMÉTICOS - SERVICE WORKER
// Cache optimization for static resources

const CACHE_NAME = 'peacock-cosmeticos-v1';
const STATIC_CACHE_URLS = [
    './',
    './wp-content/plugins/elementor/assets/css/frontend.min.css',
    './wp-content/uploads/elementor/css/post-16.css',
    './wp-content/uploads/2024/10/banner01.jpg',
    './wp-content/uploads/2024/10/banner03.jpg',
    './wp-content/uploads/2024/10/peecock-08.png',
    './wp-content/uploads/2024/10/selo-aprovado-anvisa-p_optimized.webp',
    './wp-includes/js/jquery/jquery.min.js'
];

// Install event
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Caching static resources');
                return cache.addAll(STATIC_CACHE_URLS);
            })
    );
});

// Fetch event
self.addEventListener('fetch', event => {
    // Only cache GET requests
    if (event.request.method !== 'GET') return;
    
    // Skip non-HTTP requests
    if (!event.request.url.startsWith('http')) return;
    
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Return cached version if available
                if (response) {
                    return response;
                }
                
                // Fetch from network
                return fetch(event.request)
                    .then(response => {
                        // Don't cache non-successful responses
                        if (!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }
                        
                        // Clone the response
                        const responseToCache = response.clone();
                        
                        // Cache static resources
                        if (shouldCache(event.request.url)) {
                            caches.open(CACHE_NAME)
                                .then(cache => {
                                    cache.put(event.request, responseToCache);
                                });
                        }
                        
                        return response;
                    });
            })
    );
});

// Activate event
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Helper function to determine if URL should be cached
function shouldCache(url) {
    const cacheableExtensions = ['.css', '.js', '.jpg', '.jpeg', '.png', '.webp', '.svg', '.woff', '.woff2'];
    return cacheableExtensions.some(ext => url.includes(ext));
}
