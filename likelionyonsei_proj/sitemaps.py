from django.urls import reverse
from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    def items(self):
        return [
            'home',
            'alumni',
            'recruit',
            'contact',
        ]
    def location(self, item):
        return reverse(item)
