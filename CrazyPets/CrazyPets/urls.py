# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from crazyPetsApp.urls import router as crazy_pets_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    url(r'^api/', include(crazy_pets_router.urls)),
]