from rest_framework.routers import DefaultRouter
from.views import *

from django.contrib import admin
from django.urls import path,include
router=DefaultRouter()
router.register('Book',bookviewset)

urlpatterns = [
    path('', include(router.urls)),
]
