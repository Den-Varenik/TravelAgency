from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
]
