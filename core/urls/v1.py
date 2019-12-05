from django.conf.urls import url
from rest_framework import routers
from django.urls import include
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]