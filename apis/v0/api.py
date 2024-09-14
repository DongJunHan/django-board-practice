from django.urls import path

from apis.v0.users.view import UserListView, UserDetailView

app_name = "board_practice"
urlpatterns = [
    path("users/", UserListView.as_view(), name="users_list"),
    path("users/<int:user_id>/", UserDetailView.as_view(), name="users_detail"),
]
