from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'gae_resume.views.home', name='home'),
    url(r'^kudos', 'gae_resume.views.kudos', name='kudos'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
]

urlpatterns += staticfiles_urlpatterns()


