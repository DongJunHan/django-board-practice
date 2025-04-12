from django.urls import path, include

app_name = "board_practice"
urlpatterns = [
    path("users/", include("apis.v0.users.urls", namespace="users")),
    # path("users/<int:user_id>/", UserDetailViewSet.as_view(), name="users_detail"),
]
