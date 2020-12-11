"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from farm_shop import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^get_news/$', views.get_news, name = 'get_news'),
    url(r'^check_token/$', views.check_token, name = 'check_token'),
    url(r'^get_news_full/$', views.get_news_full, name = 'get_news_full'),
    url(r'^get_profile/$', views.get_profile, name = 'get_profile'),
    url(r'^change_profile/$', views.change_profile, name = 'change_profile'),
    url(r'^newsell/$', views.newsell, name = 'newsell'),
    url(r'^find_items/$', views.find_items, name = 'find_items'),
    url(r'^item_info/$', views.item_info, name = 'item_info'),
    url(r'^get_list_sells/$', views.get_list_sells, name = 'get_list_sells'),
    url(r'^change_sell/$', views.change_sell, name='change_sell'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)