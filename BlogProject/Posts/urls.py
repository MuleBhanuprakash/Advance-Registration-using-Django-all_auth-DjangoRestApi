from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

from .views import PostDetail, PostList, UserList, UserDetails

urlpatterns = [
    path('<int:pk>', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetails.as_view()),
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
