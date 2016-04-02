from django.conf.urls import include, url
from django.contrib import admin
from notification.views import subscriberView, notifyView
urlpatterns = [
    # Examples:
     url(r'^$', 'pushnotifications.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/subscribe$', subscriberView.as_view()),
    url(r'^admin/notification$', notifyView.as_view()),
]
