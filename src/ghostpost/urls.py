from django.contrib import admin
from django.urls import path, include
from ghostpost.views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)


# urlpatterns = [
#     path('api/', include(router.urls))
# ]