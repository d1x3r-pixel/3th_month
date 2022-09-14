from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from account.views import (
    RegisterView,
    MyObtainPairView,
    UserListView,
    UserDetailApiView,
    UserDestroyApiView
)


urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_list/', UserListView.as_view(), name='user-list'),
    path('detail/<int:id>/', UserDetailApiView.as_view(), name='detail'),
    path('delete/<int:id>/', UserDestroyApiView.as_view(), name='delete'),
]