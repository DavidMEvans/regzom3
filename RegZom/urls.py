"""blog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.views.generic import RedirectView
from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as accounts_views
from posts import views as posts_views
from django.conf.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^$', RedirectView.as_view(url='index/')),
    url(r'posts/', include('posts.urls')),
    url(r'^index/$', accounts_views.index, name='index'),
    url(r'^about/$', accounts_views.about, name='about'),
    url(r'^contact/$', accounts_views.contact, name='contact'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),

    url(r'^donations/$', accounts_views.donations, name='donations'),

    url(r'^blogpostform/$', posts_views.create_or_edit_post, name='blogpostform'),
    url(r'^blogposts/$', posts_views.post_detail, name='postdetails'),

    url(r'^logout/$', accounts_views.logout, name='logout'),

    # Stripe URLs
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription),
    url(r'^subscriptions_webhook/$', accounts_views.subscriptions_webhook, name='subscriptions_webhook'),
]

#if settings.DEBUG:
#    import debug_toolbar

#urlpatterns += [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    ]