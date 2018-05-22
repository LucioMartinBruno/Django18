from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
urlpatterns = [
    # Examples: 
    url(r'^$','newsletter.views.Home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'trydjango.views.About', name='about'),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^arduino/$', 'trydjango.views.arduino', name='arduino'),
    url(r'^raspberry/$', 'trydjango.views.raspberry', name='raspberry'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

] 
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)