from django.urls import include, path
from rest_framework import routers

from apis.v0.users.views import UserListViewSet, UserDetailViewSet

router = routers.SimpleRouter()

router.register("", UserListViewSet, basename="user_list")
router.register("", UserDetailViewSet, basename="user_detail")

app_name = "users"
urlpatterns = [
    path("", include(router.urls)),
]
