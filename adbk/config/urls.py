"""adbk URL Configuration

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
from adbk.book_app.viewsets import AddresseeViewSet, MailViewSet, PhoneViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ad_book/', AddresseeViewSet.as_view({
        'post': 'list',
        'put': 'create'})),
    path('ad_book/<int:pk>/', AddresseeViewSet.as_view({
        'post': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'})),
    path('mails/', MailViewSet.as_view({'post': 'list', 'put': 'create'})),
    path('mails/<int:pk>/', MailViewSet.as_view({
        'post': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'})),
    path('phones/', PhoneViewSet.as_view({'post': 'list', 'put': 'create'})),
    path('phones/<int:pk>/', PhoneViewSet.as_view({
        'post': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'})),
]
